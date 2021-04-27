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

device.pop('Vendor')

# Update

oper = dict(CPU = '5%', Memory = '10%')
oper
device.update(oper)
device

# Items

for key, value in device.items():
    print (key + ':' + value)

    ###############################################################
    #########    LEARNING TO USE PYTHON SETS & TUPLES   ###########
    ###############################################################

# Sets

vendors = set(['Arista', 'Cisco', 'Arista', 'Cisco', 'Juniper', 'Cisco'])
vendors
len(vendors)

#  Tuples

description = tuple(['Router1', 'Portland'])
description
print(description[0])

# Adding Conditional Logic

hostname = 'NYC'
if hostname == 'NYC':
    print('The hostname is NYC')
    print(len(hostname))
    print('The End')

hostname = 'DEN_CO'
if hostname == 'NYC':
    print ('The hostname is NYC')
elif hostname == 'NJ':
    print ('the hostname is NJ')
else: 
    print ('UNKNOWN HOSTNAME')

# Containment

vendors = ['Arista', 'Juniper', 'Big Switch', 'Cisco']
'Arista' in vendors

if 'Arista' in vendors:
    print ('Arista is deployed')

version = 'CRS100V Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.3.1, RELEASE'
"16.3.1" in version 

if "16.3.1" in version: 
    print("Version is 16.3.1")

    ###############################################################
    #################    USING LOOPS IN PYTHON   ##################
    ###############################################################

counter = 1
while counter < 5:
    print (counter)
    counter += 1

vendors = ['Arista', 'Juniper', 'Big Switch', 'Cisco']
for vendor in vendors:
    print ('VENDOR: ' + vendor)

vendors = ['Arista', 'Juniper', 'Big Switch', 'Cisco', 'O\'Reilly']
vendors
approved_vendors = ['Arista', 'Juniper', 'Big Switch', 'Cisco']
for vendor in vendors: 
    if vendor not in approved_vendors:
        print ('NETWORK VENDOR NOT APPROVED: ' + vendor)

# ===============================================================================

COMMANDS = {
    'description': 'description {}', 
    'speed': 'speed {}', 
    'duplex': 'duplex {}',
}
print (COMMANDS)
CONFIG_PARAMS = {
    'description': 'auto description by Python', 
    'speed': '10000', 
    'duplex': 'auto',
}
print (CONFIG_PARAMS)

commands_list = []

for feature, value in CONFIG_PARAMS.items():
    command = COMMANDS.get(feature).format(value)
    commands_list.append(command)

commands_list.insert(0, 'interface Eth1/1')
print (commands_list)

# Enumerate

# vendors = ['Arista', 'Juniper', 'Big Switch', 'Cisco']
# for index, each in enumerate(vendors):
#     if each == 'Arista':
#         print('Arista index is at: ' + index)

    ###############################################################
    #################    USING PYTHON FUNCTIONS  ##################
    ###############################################################

def print_vendor(net_vendor):
    print (net_vendor)

vendors = ['Arista', 'Juniper', 'Big Switch', 'Cisco']
for vendor in vendors:
    print_vendor(vendor)

# def get_commands(vlan, name):
#     commands = []
#     commands.append('vlan ' + vlan)
#     commands.append('name ', + name)
#     return commands

# def push_commands(device, commands):
#     print('Connecting to device: ' + device)
#     for cmd in commands:
#         print ('Sending command: ' + cmd)

# devices = ['Sw1', 'Sw2', 'Sw3']
# vlans = [
#     {
#         'id': 10, 
#         'name': 'USERS'
#     },
#     {
#         'id': 20,
#         'name': 'VOICE'
#     },
#     {
#         'id': 30,
#         'name': 'WLAN'
#     }
# ]

# for vlan in vlans: 
#     id = vlan.get('id')
#     name = vlan.get('name')
#     print('\n')
#     print('CONFIGURING VLAN: ' + id)
#     commands = get_commands(id, name)
#     for device in devices:
#         push_commands(device, commands)
#         print('\n')

    ###############################################################
    ###################    WORKING WITH FILES   ###################
    ###############################################################

vlans_file = open('vlans.cfg', 'r')
vlans_file.read()
vlans_file.close()
vlans_file = open('vlans.cfg', 'r')
vlans_file.readlines()
vlans_file.close()

vlans_file = open('vlans.cfg', 'r')
vlans_text = vlans_file.read()
vlans_list = vlans_text.splitlines()
vlans_list

vlans_file = open('vlans.cfg', 'r')
vlans_text = vlans_file.read()
vlans = []
for item in vlans_list:
    if 'vlan' in item:
        temp = {}
        id = item.strip().strip('vlan').strip()
        temp['id'] = id
    elif 'name' in item: 
        name = item.strip().strip('name').strip()
        temp['name'] = name
        vlans.append(temp)

vlans
vlans_file.close()

add_vlan = {'id': '70', 'name': 'MISC'}
vlans.append(add_vlan)
add_vlan = {'id': '80', 'name': 'HQ'}
vlans.append(add_vlan)
vlans

write_file = open('vlans_new.cfg', 'w')
for vlan in vlans:
    id = vlan.get('id')
    name = vlan.get('name')
    write_file.write('vlan ' + id + '\n')
    write_file.write(' name' + name + '\n')

write_file.close()

with open ('vlans_new.cfg', 'w') as write_file:
    write_file.write('vlan 10\n')
    write_file.write(' name TEST_VLAN\n')

write_file.close()

    ###############################################################
    ################    CREATING PYTHON PROGRAMS   ################
    ###############################################################

import push # from python functions section above

dir (push)

device = 'Router1'
commands = ['interface Eth1/1', 'shutdown']

push.push_commands(device, commands)

from push import push_commands

device = 'Router1'
commands = ['interface Eth1/1', 'shutdown']

push_commands(device, commands)

from push import push_commands as pc 

device = 'Router1'
commands = ['interface Eth1/1', 'shutdown']

pc(device, commands)

    ###############################################################
    #########    Passing Arguments into Python Scripts   ##########
    ###############################################################

#!/usr/bin/env python

import sys

if __name__ == "__main__":
    print(sys.argv)

    ###############################################################
    ######## Learning Additional Tips & Tricks with Python ########
    ###############################################################

dir()
type()
help()
isinstance()

hostname = 'router1'
type(hostname)
dir(hostname)
help(hostname.upper)

hostname = ''
devices = []

if isinstance(devices, list):
    print('devices is a list')

if isinstance(hostname, str):
    print('hostname is a string')

if __name__ == "__main__":
    devices = ['r1', 'r2,', 'r3']

    hostname = 'router5'

devices = []
if not devices: 
    print('devices is empty')

hostname = 'something'
if hostname:
    print('hostname is not null')

hostname = 'r5'
interface = 'Eth1/1'
test = 'device %s has one interface: %s ' % (hostname, interface)
print(test)
