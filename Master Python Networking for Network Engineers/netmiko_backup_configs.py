from netmiko import ConnectHandler
import netmiko 
from datetime import datetime

with open('devices.txt') as f:
    devices = f.read().splitlines()

for ip in devices:

    cisco_device={
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'ansible',
        'password': 'ansible',
        'port': 22,
    }

    connection=ConnectHandler(**cisco_device)
    print ("\nEntering Enable Mode\n")
    connection.enable()


    output = connection.send_command('show run')


    prompt = connection.find_prompt()
    hostname = prompt[0:-1]

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    filename = f'{hostname}-{year}-{month}-{day}_backup.txt'
    # print (prompt)
    # print(hostname)
    # print (filename)

    with open (filename, 'w') as backup:
        backup.write(output)
        print ('#' * 37)
        print (f"Backup of {hostname} completed successfully")
        print ('#' * 37)



    print ("\nClosing Connection\n")
    connection.disconnect()