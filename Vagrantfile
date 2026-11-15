# One file builds all four FiveOps servers. Run: vagrant up
VMS = {
  "jenkins"    => { ip: "192.168.56.10", memory: 3072, cpus: 2 },
  "test"       => { ip: "192.168.56.11", memory: 1536, cpus: 1 },
  "prod"       => { ip: "192.168.56.12", memory: 1536, cpus: 1 },
  "monitoring" => { ip: "192.168.56.13", memory: 2048, cpus: 2 }
}

Vagrant.configure("2") do |config|
  config.vm.box = "bento/ubuntu-24.04"

  VMS.each do |name, spec|
    config.vm.define name do |node|
      node.vm.hostname = "fiveops-#{name}"
      node.vm.network "private_network", ip: spec[:ip]

      node.vm.provider "virtualbox" do |vb|
        vb.name   = "fiveops-#{name}"
        vb.memory = spec[:memory]
        vb.cpus   = spec[:cpus]
      end

      node.vm.provision "ansible_local" do |ansible|
        ansible.playbook        = "ansible/playbooks/site.yml"
        ansible.inventory_path = "ansible/inventory/vagrant/hosts.ini"
        ansible.limit          = name
      end
    end
  end
end
