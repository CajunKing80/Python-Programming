import paramiko_ssh
import getpass

username = input('Username: ')
password = getpass.getpass()

ssh_client = paramiko_ssh.connect('192.160.0.133', 2299, username, password)
remote_connection = paramiko_ssh.get_shell(ssh_client)

new_user = input('Enter a new username: ')
command = 'sudo useradd -m -d /home/' + new_user + ' -s /bin/bash ' + new_user'
paramiko_ssh.send_command(remote_connection, command)
paramiko_ssh.send_command(remote_connection, password)
print ('A new user has been created')

answer = input ('Display the users? <y|n>')
if answer == 'y':
    users = paramiko_ssh.send_command(remote_connection, 'cat /etc/passwd')
    print (users.decode())
    
paramiko_ssh.close(ssh_client)