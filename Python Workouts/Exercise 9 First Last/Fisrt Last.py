
from ipaddress import IPv4Network, IPv4Address

def firstlast(subnet):

    subnet = IPv4Network()
    print(str(subnet.network_address))

firstlast('192.168.0.0/24')