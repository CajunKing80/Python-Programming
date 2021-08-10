from netmiko import ConnectHandler
from netmiko import file_transfer

device = {
    "device_type": "cisco_ios",
    "host": "10.211.211.1",
    "username": "commadmin",
    "password": "password",
    "port": 22,
    "verbose": True
}

connection = ConnectHandler(**device)

transfer_output = file_transfer(
    connection,
    source_file="csr1000v-universalk9.17.03.03.SPA.bin",
    dest_file="csr1000v-universalk9.17.03.03.SPA.bin69",
    file_system="flash:",
    direction="put",
    overwrite_file=True,
    socket_timeout=30,
)

print(transfer_output)
connection.disconnect()
