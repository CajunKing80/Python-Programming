from netmiko import ConnectHandler
from netmiko import file_transfer
import time

start = time.time()

device = {
    "device_type": "cisco_ios",
    "host": "192.168.0.155",
    "username": "ansible",
    "password": "ansible",
    "port": 22,
    "verbose": True
}

connection = ConnectHandler(**device)

print("File transfer in progress...")


transfer_output = file_transfer(
    connection,
    source_file="csr1000v-universalk9.17.03.03.SPA.bin",
    dest_file="csr1000v-universalk9.17.03.03.SPA.bin",
    file_system="flash:",
    direction="put",
    overwrite_file=True,
    socket_timeout=30,
)
while file_transfer == True: 
    print ("!")
    time.sleep(5)

end = time.time()

print("Transfer Complete!!!")
print(f"Total transfer time: {end - start}")

connection.disconnect()
