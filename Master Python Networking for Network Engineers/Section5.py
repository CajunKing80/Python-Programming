######################################################
############ Lesson 55 Welcome to Paramiko############
######################################################

import paramiko 

ssh_client = paramiko.SSHClient()
print (type(ssh_client))

print ('Connecting to ')
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='10.1.1.10', port='22', )

# Video 55 Intro to Paramiko
# pip install paramiko

import paramiko