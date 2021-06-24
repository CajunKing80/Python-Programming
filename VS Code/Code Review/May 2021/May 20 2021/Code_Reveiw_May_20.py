# =================================================================================================
# EASY ============================================================================================
# =================================================================================================

# From a list of IP addresses, return the first index and the last index in the list
# ipaddress module
# netmask, network, and broadcast IP'a are anobject of the IP address module
# hosts method of the subnetB object

import ipaddress

net4 = ipaddress.ip_network ('172.16.0.0/16')
all_hosts = list(net4.hosts())

print("********** EASY **********")
print (net4.network_address)
print (net4.broadcast_address)
print (net4.netmask)
print (net4.num_addresses)
print (len(all_hosts))
print("********** EASY **********")


def firstlast(subnet):

    subnet = ipaddress.ip_network(subnet)
    network = str(subnet.network_address) + '\n' + str(subnet.broadcast_address)
    print ()
    print (network)
    print ()
 
firstlast('192.168.0.0/24')


# =================================================================================================
# MEDIUM ==========================================================================================
# =================================================================================================

# From the easy challenge, write a script to subnet your network
# Return whether your network is Public or Private

from ipaddress import IPv4Network

print("********** MEDIUM **********")
network = IPv4Network('192.168.0.0/24')
for net in network.subnets(new_prefix=28):
    print(net)

if network.is_private == True:
    print(f'{network} is a Private Network')
else: 
    print(f'{network} is a Public Network')
print("********** MEDIUM **********")