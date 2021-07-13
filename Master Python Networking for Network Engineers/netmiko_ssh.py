from netmiko import Netmiko 
import time 

# ssh_client = paramiko.SSHClient()
# ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def main():


    router1 = {
        'hostname': '192.168.0.152',
        'port': '22', 
        'username': 
        'ansible', 
        'password': 'ansible'
        }
    router2 = {
        'hostname': '192.168.0.155', 
        'port': '22', 
        'username': 'ansible', 
        'password': 'ansible'
        }
    router3 = {
        'hostname': '192.168.0.115', 
        'port': '22', 
        'username': 'ansible', 
        'password': 'ansible'
        }
    routers = [router1, router2, router3]

    platform_map = {"ios": "cisco_ios", "iosxe": "cisco_xe"}

    for router in routers: 
        platform = platform_map[routers["platform"]]
        conn = Netmiko(
            host = host["name"],
            username = "ansible", 
            password = 'ansible',
            device_type = platform,
        )
        print (f'Connected to {conn.find_prompt()} successfully')

        conn.disconnect()

if __name__ == '__main__':
    main()



        # ssh_client.connect(
        #     **router, 
        #     look_for_keys = False, 
        #     allow_agent = False
        #     )
        # cmd = ssh_client.invoke_shell()
    cmd.send('enable\n')
    cmd.send('conf t\n')
    cmd.send('router ospf 1\n')
    cmd.send('net 192.168.0.0 0.0.0.255 area 0\n')
    cmd.send('end\n')
    cmd.send('term len 0\n')
    cmd.send('sh ip protocols\n')
    cmd.send('sh ip route\n')
    cmd.send('sh ip os ne\n')
    time.sleep(2)

    output = cmd.recv(65535).decode('utf-8')
    print (output
    )

if ssh_client.get_transport().is_active() == True:
    print ("Closing Connection")
    ssh_client.close()
