from napalm import get_network_driver
import json

driver = get_network_driver('ios')
optional_args = {'secret': 'cisco'} #cisco enable password
ios = driver(
    '192.168.0.152', 
    'ansible', 'ansible', 
    optional_args=optional_args
    )
ios.open()
# start code here 


output=ios.ping(
    destination='192.168.0.155',
    count=4,
    source='1.1.1.1'
    )
ping=json.dumps(
    output, 
    sort_keys=True,
    indent=4
)
print(ping)



# end code here
ios.close()