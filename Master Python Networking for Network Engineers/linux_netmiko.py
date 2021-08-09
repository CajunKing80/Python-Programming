from netmiko import ConnectHandler

linux = {
    "device_type": "linux",
    "host": "192.168.0.134",
    "username": "ansible",
    "password": "ansible",
    "port": 22,
    "verbose": True,
}

connection = ConnectHandler(**linux)

connection.enable()
output = connection.send_command("uname -a")

print(output)
print("Closing Connection")

connection.disconnect()
