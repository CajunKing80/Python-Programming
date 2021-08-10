# from netmiko import Netmiko
from netmiko import ConnectHandler
# connection = Netmiko(host='192.168.0.22', port='22', username='ansible', password='ansible', device_type='cisco_xe')

cisco_device={
    'device_type': 'cisco_ios',
    'host': '192.168.0.22',
    'username': 'ansible',
    'password': 'ansible',
    'port': 22,
}

connection=ConnectHandler(**cisco_device)
# Find the prompt to determine priviledged or unprivileged mode
prompt=connection.find_prompt()
print(prompt)

#Connect directly into enable mode
if '>' in prompt:
    connection.enable()

output = connection.send_command('show run')
print(output)

# Confirm if the prompt is currently in global configuration mode
print (connection.check_config_mode())

if not connection.check_config_mode():
    connection.config_mode()

print (connection.check_config_mode())

print("Closing Connection")
connection.disconnect()