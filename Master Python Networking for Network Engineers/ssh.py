import paramiko
import time 

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

router1 = {'hostname': '192.168.0.21', 'port': '22', 'username': 'ansible', 'password': 'ansible'}
router2 = {'hostname': '192.168.0.24', 'port': '22', 'username': 'ansible', 'password': 'ansible'}
router3 = {'hostname': '192.168.0.22', 'port': '22', 'username': 'ansible', 'password': 'ansible'}
routers = [router1, router2, router3]

for router in routers: 
    print (f'Connecting to {router["hostname"]}')
    ssh_client.connect(
        **router, 
        look_for_keys = False, 
        allow_agent = False
        )
    shell = ssh_client.invoke_shell()

    shell.send('enable\n')
    shell.send('conf t\n')
    shell.send('router ospf 1\n')
    shell.send('net 192.168.0.0 0.0.0.255 area 0\n')
    shell.send('end\n')
    shell.send('term len 0\n')
    shell.send('sh ip protocols\n')
    time.sleep(2)

    output = shell.recv(65535).decode('utf-8')
    print (output
    )

if ssh_client.get_transport().is_active() == True:
    print ("Closing Connection")
    ssh_client.close()




# router = {
#     'hostname': '192.168.0.152',
#     'port': '22', 
#     'username': 'ansible', 
#     'password': 'ansible'
# }
# print (f'Connecting to {router["hostname"]}')
# ssh_client.connect(**router, look_for_keys = False, allow_agent = False)
# shell = ssh_client.invoke_shell()
# shell.send('terminal length 0\n')
# shell.send('show version\n')
# time.sleep(2)
# output =shell.recv(10000)
# print (type(output))

# ssh_client.connect(
#     hostname = "192.168.0.134",
#     port = "22",
#     username = "ansible",
#     password = "ansible",
#     look_for_keys = False,
#     allow_agent = False
#     )