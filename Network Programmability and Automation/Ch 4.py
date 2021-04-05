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
