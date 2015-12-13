# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|

  # VM will be ubuntu 14.04
  config.vm.box = "ubuntu/trusty64"

  # VM will be available to the host machine on port 8000 or at IP below
  config.vm.network "forwarded_port", guest: 80, host: 8000
  config.vm.network "private_network", ip: "192.168.33.10"

  # Run setup script
  config.vm.provision "shell", path: "bin/setup.sh"
end
