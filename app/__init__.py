import logging
import os

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)
    if test_config:
        app.config.update(test_config)
    else:
        # The password arrives from the environment, never from code
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]

    db.init_app(app)
    from . import models  # noqa: F401  (registers the tables)
    from .tickets import bp
    app.register_blueprint(bp)
    with app.app_context():
        db.create_all()

    @app.get("/health")
    def health():
        # Healthy only if the database answers too
        try:
            db.session.execute(text("SELECT 1"))
        except Exception as exc:  # never log the message: it may hold a host
            app.logger.error("health: database unreachable (%s)",
                             type(exc).__name__)
            return jsonify(status="error", database="down"), 503
        return jsonify(status="ok")

    @app.get("/version")
    def version():
        return jsonify(version=os.environ.get("APP_VERSION", "dev"))

    if not app.testing:
        from prometheus_flask_exporter import PrometheusMetrics
        PrometheusMetrics(app)  # adds /metrics for Prometheus

    logging.basicConfig(level=logging.INFO)
    return app
