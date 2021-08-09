from netmiko import ConnectHandler
from datetime import datetime
import time 
import threading

start = time.time()

def backup(device):
    connection = ConnectHandler(**device)
    print (f"Connecting To Router {ip}")
    connection.enable()

    output = connection.send_command('show run')
    prompt = connection.find_prompt()
    hostname = prompt [0:-1]

    now = datetime.now()
    year = now.year
    month = now.month 
    day = now.day

    filename = f'{hostname}_{year}--{month}--{day}_backup.txt'
    with open (filename, 'w') as backup:
        backup.write(output)
        print (f"Backup of {hostname} successful")

    print (f"Closing connection to {hostname}")
    connection.disconnect()

with open ('devices.txt') as f:
    devices = f.read().splitlines()

threads = list()
for ip in devices: 

    device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'username': 'ansible', 
        'password': 'ansible', 
        'port': 22,
        'verbose': True
    }

    th = threading.Thread(target=backup, args=(device,))
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

end = time.time()
print (f"Total execution time: {end - start}")