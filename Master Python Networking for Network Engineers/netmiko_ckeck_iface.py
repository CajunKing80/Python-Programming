
from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "192.168.0.22",
    "username": "ansible",
    "password": "ansible",
    "port": 22,
    "verbose": True,
}

connection = ConnectHandler(**device)
prompt = connection.find_prompt()

if ">" in prompt:
    connection.enable()

interface = input("Enter the interface tht you want to enable:")
output = connection.send_command("sh ip int " + interface)

if "Invalid input detected" in output:
    print ("Invalid Interface")
else:
    first_line = output.splitlines()[0]
    print (first_line)
    if not 'up' in first_line:
        print("The interface is down. Enabling the interface")
        commands = ["interface " + interface, "no shut", "exit"]
        output = connection.send_config_set(commands)
        print('#' * 40)
        print("The interface has been enabled")
    else:
        print("This interface is already enabled")

connection.disconnect()