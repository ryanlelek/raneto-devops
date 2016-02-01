Raneto DevOps
=============

Easily configure a remote machine to host your Raneto documentation.  
**Check out [AnsibleTutorials.com](http://www.ansibletutorials.com) for more DevOps scripts!**

# Note!
This repository is going to be sliced and diced into modules and then published to Ansible Galaxy.  
If you like what you see, I'd suggest following me on my profile and/or sending me an email instead of starring the repo.  

# Limitations
- Requires Mac OS X (Tested with v10.9 Mavericks)
- Tested only with Ubuntu v14.04

# Installation

## Local Applications
1. [VirtualBox v5.0.14](https://www.virtualbox.org/wiki/Downloads)
2. [Vagrant v1.8.1](https://www.vagrantup.com/downloads.html)
3. Vagrant Image: ubuntu/trusty64 (virtualbox, 20160122.0.0)
4. [Homebrew](http://brew.sh/)
5. Ansible v2.0.0.2 installed with Homebrew:  
`$ brew install ansible`

## Ansible Dependencies
`$ ansible-galaxy install -r roles.yml`  

# Usage

## 1) Start Vagrant (optional, good for testing)
From the project directory run:  
`$ vagrant up`.  

This will create a new VM on your local machine and configure it to run Raneto.  
That's all you need to do to deploy locally.  
**Check access with `$ curl -v -H "Host: devops.raneto.com" http://localhost:8888`**  
If you want to, [set the domain in /etc/hosts](http://ubuntuforums.org/showthread.php?t=3407) to point to 127.0.0.1 to access in a browser

## 2) Inventory Your Remote Machines
I'm using DigitalOcean as my provider, and suggest using them for the easiest compatibility.  

You can use other providers or machines of your own with little to no modifications.

DigitalOcean provides VPS machines for $5/month (1 CPU, 512MB).  
**Use coupon code `LINUX13` to get $10 Free** (I'm not affiliated with that code). 

No matter what provider you choose, set a DNS record for the hostname (myhost.mydomain.com) and replace the existing hostname in the `inventory/digitalocean` file.

## 3) Run Ansible

The following commands will configure and deploy Raneto to the machines you listed in your inventory file.
If you have any problems or questions, open an issue and I'll help you.

`$ ansible-playbook --inventory-file=inventory/ --ask-sudo-pass main.yml`

Here's a shorter version that does the same thing:  
`$ ansible-playbook -i inventory/ -K main.yml`

The default sudo password is `ansible`

## 4) Adding your Raneto repository
See the new [Raneto example](https://github.com/gilbitron/Raneto/tree/master/example) for how to structure your project.  
It's a good idea to start a new Git repository (public or private) and commit your documentation files to that repository instead of directly to a cloned copy of Raneto.  

To use your Raneto project's Git repository in this deployment process:  

1. edit `deploy.yml` and add your Git repo address  
2. edit `deploy.yml` and change the domain `devops.raneto.com` to your (sub)domain  

## 5) Change Sudo Password (optional, recommended)
Generate a password to be used on the machines:  

1. `$ brew install python`  
2. `$ pip install passlib`  
3. `$ python tools/password_hasher.py [new_password]`  

Put the output in file `group_vars/all`.  
__Note: Even if the password is the same, hashes will be different on each generation__

# Future
- Move from Upstart to systemd
- Support Debian, CentOS, etc. out of the box

# Troubleshooting

## I Keep Getting Redirected!
You might be accessing the machine via IP or a site domain that has not been configured. All non-configured domains (including IPs) are redirected.  

1. Don't use a browser, browsers will cache the redirect for a considerable amount of time. Use the terminal instead.
2. Run this command to diagnose. Make sure the "Host" header is being set to one of the configured domains.  
`$ curl -v -H "Host: devops.raneto.com" http://127.0.0.1:8888`

## Sudo Password
The default sudo password is **`ansible`**

## SSH Key Mismatch
You may need to remove the server's record in ~/.ssh/known_hosts if the server's ip/keys change (e.g. after rebuilding the server)

Remove Old Key:  
`$ ssh-keygen -R [ip-or-hostname]`

## Vagrant Usage

### Creating a Machine
`$ vagrant up`

### Run Provisioning Again (Redeploy)
`$ vagrant provision`

### Deleting a Machine
`$ vagrant destroy`

### SSH-ing into Vagrant:

1. `ssh vagrant@127.0.0.1 -p 2222`  
2. `vagrant ssh`
