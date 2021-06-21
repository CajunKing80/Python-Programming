# =================================================================================================
# EASY ============================================================================================
# =================================================================================================

# Write a Python script that returns the name and IP address for your system. Also
# return the IP address from a URL of choice. 


import socket

system_name = socket.gethostname()
system_address = socket.gethostbyname(system_name)
ipaddr = socket.gethostbyname('w3schools.com')
print(f'System Name is {":" :^25} {system_name :<1}')
print(f'System IP Address is {":" :^13} {system_address :<1}')
print(f'IP Address of W3Schools is {":" :^} {ipaddr :<1}')