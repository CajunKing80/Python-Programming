from netmiko import ConnectHandler
from netmiko import file_transfer

device = {
    "device_type": "cisco_ios",
    "host": "192.168.0.152",
    "username": "ansible",
    "password": "ansible",
    "port": 22,
    "verbose": True
}

connection = ConnectHandler(**device)

transfer_output = file_transfer(
    connection,
    source_file="csr1000v-universalk9.17.03.03.SPA.bin",
    dest_file="csr1000v-universalk9.17.03.03.SPA.bin",
    file_system="flash:",
    direction="put",
    overwrite_file=True
)

print(transfer_output)
connection.disconnect()