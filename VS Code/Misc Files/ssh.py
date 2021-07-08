import paramiko

ssh_client = paramiko.SSHClient()
print(type(ssh_client))

print ("Connecting to 192.168.0.23")
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(
    hostname = "192.168.0.23",
    port = "22",
    username = "ansible",
    password = "ansible",
    look_for_keys = False,
    allow_agent = False
    )


print (ssh_client.get_transport().is_active())

print ("Closing Connection")
ssh_client.close()