
Vagrant.configure(2) do |config|

  # Virtual Machine Basics
  config.vm.box = "ubuntu/trusty64"
  config.vm.provider "virtualbox" do |v|
    # Lower to 512 to save resources
    v.memory = 1024
    v.cpus   = 1
  end

  # Create a Web VM
  config.vm.define "web.local" do |web|
    # Forward VM port 80 to localhost 8888
    # You'll access the site through http://127.0.0.1:8888
    config.vm.network "forwarded_port", guest: 80, host: 8888
  end

  # Provision Vagrant machine with Ansible
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "main.yml"
    ansible.groups   = {
      "vagrant" => ["web.local"], # Provider
      "web"     => ["web.local"], # Type
      "raneto"  => ["web.local"], # Project
      "parse"   => ["web.local"]  # Project
    }
  end

end
