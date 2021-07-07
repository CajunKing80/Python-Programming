EASY

/etc/ansible

Create an Ansible inventory file with the following devices

CSR1	{ ip address }
CSR2	{ ip address }
CSR3  	{ ip address }

MEDIUM

Modify the Ansible inventory file, and group the devices by device type. Also include 
global variables to include the ssh username and password. (This assumes that all devices
in the inventory are managed and configured with the same SSH username and password)

[all:vars]
ansible_user=ansible
ansible_ssh_pass=ansible

[iosxe]
CSR1
CSR2
CSR3

HARD

Using an emulator of choice, build a basic Ansible lab. Lab should consist of 1 Ansible 
controller and a minimum of 2 managed nodes. (examples include a Cisco virtual router, or
secondary Linux machines with ip routing enabled)

Configure an Ansible playbook that will configure the connected interface IP addresses
into a running state; configure a static route between the devices, and save the running
configuration to the startup config. 

Execute the playbook. 

Log into the remote devices and confirm the playbook performed the basic interface
configuration, built the static route, and saved the configuration.  
