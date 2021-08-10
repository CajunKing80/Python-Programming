from netmiko import ConnectHandler

cisco_device={
    'device_type': 'cisco_ios',
    'host': '192.168.0.22',
    'username': 'ansible',
    'password': 'ansible',
    'port': 22,
}

connection=ConnectHandler(**cisco_device)
prompt=connection.find_prompt()

if '>' in prompt:
    connection.enable()

if not connection.check_config_mode():
    connection.config_mode()

connection.send_command('interface GigabitEthernet1')
connection.send_command('ip add 192.168.0.22 255.255.255.0')
connection.send_command('shut')
connection.send_command('no shut')
connection.send_command('end')
connection.send_command('wr')

output = connection.send_command('show ip int br')
print (output)

print("Closing Connection")
connection.disconnect()