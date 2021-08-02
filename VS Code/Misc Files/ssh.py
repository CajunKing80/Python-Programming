import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router = {
    'hostname': '192.168.0.21',
    'port': '22', 
    'username': 'ansible', 
    'password': 'ansible'
}

print (f'Connecting to {router["hostname"]}')

# ** will unpack the dictionary for the variable router, and kwargs added to the connect method
ssh_client.connect(**router, look_for_keys = False, allow_agent = False)

shell = ssh_client.invoke_shell()
shell.send('term len 0\n')
shell.send('show version\n')
time.sleep(1)

output = shell.recv(10000)
print(type(output))
output = output.decode('utf-8')
print (output)



if ssh_client.get_transport().is_active() == True:
    print (f'Closing Connection to {router["hostname"]}')
    ssh_client.close()



# print(type(ssh_client))
# ssh_client.connect(
#     hostname = "192.168.0.21",
#     port = "22",
#     username = "ansible",
#     password = "ansible",
#     look_for_keys = False,
#     allow_agent = False
#     )
# print (ssh_client.get_transport().is_active())
