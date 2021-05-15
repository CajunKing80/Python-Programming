import ipaddress

def firstlast(subnet):

    subnet = ipaddress.ip_network(subnet)
    network = str(subnet.network_address) + '\n' + str(subnet.broadcast_address)
    print ()
    print(network)
    print()
 
firstlast('192.168.0.0/24')