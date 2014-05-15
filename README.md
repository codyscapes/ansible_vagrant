Ansible Work enviroment automation
=========

A configuration management tool to set up a virtual development enviroment.

  - Will install uwsgi and nginx
  - Will set up the correct directories
  - Will start your server

Instructions
=========

#### Install Vagrant
> * <http://www.vagrantup.com/downloads.html/>

#### Install Ansible
> Ubuntu
>> ```sh
$ sudo apt-add-repository ppa:rquillo/ansible
$ sudo apt-get update
$ sudo apt-get install
```
> OSX
>> ```sh
>> $ brew update
>> $ brew install ansible
```

#### Clone git repository
>```sh
$ git clone https://github.com/JasonMannon/ansible-vagrant-automation.git
```

#### Run:
>```sh
$ cd ansible-vagrant-automation
$ vagrant up
```
> * visit <http://127.0.0.1:8080/> and you should see a welcome to nginx page
