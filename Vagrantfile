VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
 config.vm.box = "hashicorp/precise32"
 config.vm.network "forwarded_port", guest: 80, host: 8080
 config.vm.synced_folder "your-path/stenosaurus", "/var/sites/stenosaurus"
 config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
 end
end
