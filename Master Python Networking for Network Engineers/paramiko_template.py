import paramiko
import time 

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

if ssh_client.get_transport().is_active() == True:
    print ("Closing Connection")
    ssh_client.close()
