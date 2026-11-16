import logging
import re

from flask import Blueprint, jsonify, request

from . import db
from .models import Customer, Ticket

bp = Blueprint("tickets", __name__)
log = logging.getLogger(__name__)
EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
STATUSES = {"open", "in_progress", "closed"}


def bad(message, code=400):
    return jsonify(error=message), code


@bp.post("/customers")
def create_customer():
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip().lower()
    if not name or not EMAIL.match(email):
        return bad("name and a valid email are required")
    if Customer.query.filter_by(email=email).first():
        return bad("email already registered", 409)
    customer = Customer(name=name, email=email)
    db.session.add(customer)
    db.session.commit()
    log.info("customer created id=%s", customer.id)  # never log emails
    return jsonify(id=customer.id, name=name, email=email), 201


@bp.post("/tickets")
def create_ticket():
    data = request.get_json(silent=True) or {}
    subject = str(data.get("subject", "")).strip()
    if not subject or not isinstance(data.get("customer_id"), int):
        return bad("customer_id and subject are required")
    if db.session.get(Customer, data["customer_id"]) is None:
        return bad("customer not found", 404)
    ticket = Ticket(customer_id=data["customer_id"], subject=subject[:200])
    db.session.add(ticket)
    db.session.commit()
    log.info("ticket created id=%s", ticket.id)
    return jsonify(ticket.to_dict()), 201


@bp.get("/tickets")
def list_tickets():
    query = Ticket.query
    status = request.args.get("status")
    if status:
        query = query.filter_by(status=status)
    return jsonify([t.to_dict() for t in query.order_by(Ticket.id)])


@bp.patch("/tickets/<int:ticket_id>")
def update_ticket(ticket_id):
    ticket = db.session.get(Ticket, ticket_id)
    if ticket is None:
        return bad("ticket not found", 404)
    status = (request.get_json(silent=True) or {}).get("status")
    if status not in STATUSES:
        return bad("status must be open, in_progress or closed")
    ticket.status = status
    db.session.commit()
    return jsonify(ticket.to_dict())
