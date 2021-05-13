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

print ()
print (net4.network_address)
print (net4.broadcast_address)
print (net4.netmask)
print (net4.num_addresses)
print (len(all_hosts))
print ()


# =================================================================================================
# MEDIUM ==========================================================================================
# =================================================================================================

# From the easy challenge, write a script to subnet your network
# Return whether your network is Public or Private

from ipaddress import ip_network, IPv4Network


net4 = IPv4Network('192.169.0.0/24')
print ()
print(list(net4.subnets(new_prefix=27)))
print ()

if net4.is_private == True:
    print(f'{net4} is a private network')
else: 
    print(f'{net4} is a public network')