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

# print(dir(ios))
output = ios.get_arp_table()
for item in output: 
    print(item)

dump = json.dumps(
    output,
    sort_keys=True,
    indent=4
    )
print(dump)

with open('arp.txt', 'w') as f: 
    f.write(dump)


# end code here
ios.close()