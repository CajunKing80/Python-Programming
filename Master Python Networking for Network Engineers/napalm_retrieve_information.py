from napalm import get_network_driver
import json

driver = get_network_driver('ios')

optional_args = {'secret' : 'cisco'} #cisco enable password
ios = driver(
    '192.168.0.152', 
    'ansible', 'ansible', 
    optional_args=optional_args
    )

ios.open()
# start code here 

print(dir(ios))

output = ios.get_facts()
dump=json.dumps(
    output, 
    sort_keys=True,
    indent=4
)
print(dump)

output2 = ios.get_interfaces()
dump=json.dumps(
    output, 
    sort_keys=True,
    indent=4
)
print(dump)

output3 = ios.get_interfaces_counters()
dump=json.dumps(
    output, 
    sort_keys=True,
    indent=4
)
print(dump)

output4 = ios.get_interfaces_ip()
dump=json.dumps(
    output, 
    sort_keys=True,
    indent=4
)
print(dump)

output5 = ios.get_bgp_neighbors()
dump=json.dumps(
    output, 
    sort_keys=True,
    indent=4
)
print(dump)

output6 = ios.get_users()
dump=json.dumps(
    output, 
    sort_keys=True,
    indent=4
)
print(dump)

ios.get #hover over this method to see a list of available parameters VIDEO 111
# end code here
ios.close()