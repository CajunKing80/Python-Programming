    ###############################################################
    ###############     LEARNING TO USE STRINGS     ###############
    ###############################################################

hostname = 'Router_1'

print (hostname)

banner = "\n\n  WELCOME TO ROUTER_1  \n\n"
banner
print(banner)

final = 'The IP address os router1 is: '
ipaddr = '1.1.1.1'
type(final)
final + ipaddr
print (final + ipaddr)

dir()
dir(str)

# Upper and Lower
help(str.upper)
help(hostname.upper)
interface = 'Ethernet1/1'
interface.lower()
interface.upper()
intf_lower = interface.lower()
print(intf_lower)
print(interface)

# Starts and Ends With
ipaddr = '10.100.20.5'
ipaddr.startswith('10')
ipaddr.startswith('100')
ipaddr.endswith('5')
interface = 'Eth1/1'
interface.lower().startswith('et')

# Strip lstrip, rstrip
ipaddr = '     10.1.50.1     '
ipaddr.strip()

# Is Digit
ten = '10'
ten.isdigit()
bogus = '10a'
bogus.isdigit()

# Count
octet = '11110000'
octet.count('1')

# Format
# Ping 8.8.8.8 vrf management

ipaddr = '8.8.8.8'
vrf = 'management'
ping = 'ping ' + ipaddr + ' vrf ' + vrf 
ping = 'ping {} vrf {}'.format(ipaddr, vrf)

# Join & Split
# Join = Create a stringfrom a list
hostnames = ['r1', 'r2', 'r3', 'r4', 'r5']
commands = ['conf t', 'interface Ethernet1/1', 'shutdown']
'\n'.join(commands)
' ; '.join(commands)
''.join(commands)
# Split = Create a list from a string
commands = 'config t ; interface Ethernet1/1 ; shutdown'
cmds_list = commands.split(' ; ')

ipaddr = '10.1.20.30'
ipaddr.split('.')

    ###############################################################
    ###############     LEARNING TO USE INTEGERS    ###############
    ###############################################################

# ADDITION
cpu = 14.3
type (cpu)

5 + 3

a = 1
b = 2
c = a + b

counter = 1
counter = counter + 1
counter += 1

# SUBTRACTION

100 - 90

counter = 10
counter = counter - 1
counter -= 1

# MULTIPLICATION

100 * 50

print (2 * 50)

print ('*' * 50)
print ('=' * 50)

# DIVISION

100 / 50

12 / 10

12 % 10

    ###############################################################
    ###############     LEARNING TO USE BOOLEANS    ###############
    ###############################################################

exists = True
exists

True and True
True and False
False and False

value1 = True
value2 = False
value1 and value2
value1 or value2

value3 = True
value4 = True
value1 and value2 and value3 and value4
value1 and value3 and value4

not False
is_layer3 = True
is_layer3
not is_layer3

True == True
True != False
'network' == 'network'
'network' == 'no_network'

    ###############################################################
    #############     LEARNING TO USE PYTHON LISTS    #############
    ###############################################################

hostnames = ['R1', 'R2', 'R3', 'R4', 'R5']
commands = ['config t', 'interface Ethernet1/1', 'shutdown']
new_list = ['Router1', False, 5]
print (new_list)

interfaces = ['Eth1/1', 'Eth1/2', 'Eth1/3', 'Eth1/4']
print (interfaces[0])
print (interfaces[1])
print (interfaces[2])
print (interfaces[3])

len(interfaces)

interfaces[-1]

dir(interfaces)

# Append

vendors = []
vendors.append('Arista')
print(vendors)
vendors.append('Cisco')
print(vendors)

# Insert

commands = ['interface Eth1/1', 'IP Address 1.1.1.1/32']
commands.insert(0, 'conf t')
commands
commands.insert(2, 'no switchport')
commands

# Count

vendors = ['Cisco', 'Cisco', 'Juniper', 'Arista', 'Cisco', 'HP', 'Cumulus', 'Arista', 'Cisco']
vendors.count('Cisco')
vendors.count('Arista')

# Pop and Index

hostnames = ['R1', 'R2', 'R3', 'R4', 'R5']
hostnames.pop()
'R5'
print (hostnames)

hostnames.index('R2')
hostnames.pop(1) # Or hostnames.pop(hostnames.index('r2'))
print(hostnames)

# Sort

available_ips = ['10.1.1.1', '10.1.1.9', '10.1.1.8', '10.1.1.7', '10.1.1.4']
available_ips.sort()
print (available_ips)

device = ['Router', 'Juniper', '12.2']

    ###############################################################
    #########    LEARNING TO USE PYTHON DICTIONARIES   ############
    ###############################################################

device = {
    'Hostname': 'Router1', 
    'Vendor': 'Juniper', 
    'OS': '12.2'
    }
print (device)
print (device['Hostname'])
print (device['Vendor'])
print (device['OS'])

device = {}
device['Hostname'] = 'Router1'
device['Vendor'] = 'Juniper'
device['OS'] = '12.2'
print (device)

device = dict(Hostname = "Router1", Vendor = "Juniper", OS = "12.2")
print (device)

# Get

device.get('Hostname')
device.get('Vendor')
device.get('OS')
device.get('Model', False)
device.get('Model', 'DOES NOT EXIST')
device.get('Hostname', 'DOES NOT EXIST')

# Keys & Values

device.keys()
device.values()

# Pop

