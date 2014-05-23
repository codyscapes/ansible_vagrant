Ansible Work enviroment automation
=========

A configuration management tool to set up a virtual development enviroment.

 Will Install 
  - pip
  - virtualenv
  - pyramid
  - pyramid-mako
  - python-dev
  - nginx
  - uwsgi

Instructions
=========

#### Install Vagrant
> * <http://www.vagrantup.com/downloads.html/>

#### Install Ansible
> Ubuntu
>> ```sh
$ sudo apt-add-repository ppa:rquillo/ansible
$ sudo apt-get update
$ sudo apt-get install ansible
```
> OSX
>> ```sh
>> $ brew update
>> $ brew install ansible
```

#### Clone git repository:
>```sh
$ git clone https://github.com/JasonMannon/ansible-vagrant-automation.git
```

> * Insert Stenosaurus directory into ansible-vagrant-automation directory
> * Copy /config/nginx.conf/ contents into /stenosaurus/config/nginx.conf
> * Open Vagrantfile and change 
>>```sh
config.vm.synced_folder "your-path/stenosaurus"
```
> with the path to your stenosaurus directory


#### Run:
>```sh
$ vagrant up
```
> * Let server load, "Takes a minute"
> * visit <http://127.0.0.1:8080/> and you should see the Stenosaurus homepage.
