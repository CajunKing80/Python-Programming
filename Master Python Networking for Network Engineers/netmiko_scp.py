from netmiko import ConnectHandler
from netmiko import file_transfer
import time
from tqdm import tqdm, trange


device = {
    "device_type": "cisco_ios",
    "host": "192.168.0.155",
    "username": "ansible",
    "password": "ansible",
    "port": 22,
    "verbose": True
}

connection = ConnectHandler(**device)

print("\nFile transfer in progress...\n")

start = time.time()

scp = file_transfer(
    connection,
    source_file="csr1000v-universalk9.17.03.03.SPA.bin",
    dest_file="csr1000v-universalk9.17.03.03.SPA.bin",
    file_system="flash:",
    direction="put",
    overwrite_file=True,
    socket_timeout=30,
)

for i in trange(517565655):
    time.sleep(5)

end = time.time()

print("Transfer Complete!!!\n")
print(f"Total transfer time: {end - start}\n")

connection.disconnect()
