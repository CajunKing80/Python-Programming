import paramiko
import time 

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router = {
    'hostname': '192.168.0.152',
    'port': '22', 
    'username': 'ansible', 
    'password': 'ansible'
}
print (f'Connecting to {router["hostname"]}')
ssh_client.connect(**router, look_for_keys = False, allow_agent = False)
shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show version\n')
time.sleep(2)
output =shell.recv(10000)
print (type(output))

# ssh_client.connect(
#     hostname = "192.168.0.134",
#     port = "22",
#     username = "ansible",
#     password = "ansible",
#     look_for_keys = False,
#     allow_agent = False
#     )


if ssh_client.get_transport().is_active() == True:
    print ("Closing Connection")
    ssh_client.close()
