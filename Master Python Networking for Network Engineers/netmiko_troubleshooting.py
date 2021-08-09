from netmiko import Netmiko 
import logging
import time

logging.basicConfig(filename="test.log", level=logging.DEBUG)
logger = logging.getLogger("netmiko")



from netmiko.ssh_dispatcher import ConnectHandler 

cisco_device = {
    "device_type": "cisco_ios",
    "host": "192.168.0.152",
    "username": "ansible",
    "password": "ansible",
    "port": 22,
    "verbose": True,
}

connection = ConnectHandler(**cisco_device)

# output = connection.send_command("show version")
# print(output)

connection.write_channel("show version\n")
time.sleep(2)
output = connection.read_channel()
print(output)

print("Closing Connection")
connection.disconnect()
