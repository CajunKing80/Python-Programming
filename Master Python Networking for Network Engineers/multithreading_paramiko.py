import paramiko_ssh
import threading 


def backup(router):

    client = paramiko_ssh.connect(**router)
    shell - paramiko_ssh.get_shell(client)

    paramiko_ssh.send_command(shell, 'terminal length 0')
    paramiko_ssh.send_command(shell, 'enable')
    paramiko_ssh.send_command(shell, 'cisco')
    paramiko_ssh.send_command(shell, 'show run')

    output = paramiko_ssh.show(shell)

    output_list = output.splitlines()
    output_list = output_list[11:-1]

    output = '\n'.join(output_list)

    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second

    filename - f'{router["server_ip"]}_{year}-{month}-{day}-{hour}:{minute}:{second}.txt'
    with open (filename, 'w') as f:
        f.write(output)

    paramiko_ssh.close(client)

# Define each router variable as a dictionary
router1 = {'server_ip': '10.1.1.10', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco'}
router2 = {'server_ip': '10.1.1.20', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco'}
router3 = {'server_ip': '10.1.1.30', 'server_port': '22', 'user': 'u1', 'passwd': 'cisco'}

# Define the list of routers
routers = [router1, router2, router3]

# Define list to store the threads
threads = list()

for router in routers:
    thread = threading.Thread(target=backup, args = (router,))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
