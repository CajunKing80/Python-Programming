import json 

with open("2nd_devices.json", mode="rt") as _file:

    data = _file.read()

formatted_data = json.loads(data)

interface_status = {}

for device in formatted_data:
    device_interfaces = device['interfaces']
    interface_status[device["name"]]=[]
    for interface in device_interfaces: 
        if interface['is_active'] == True:
            interface_status[device["name"]].append(interface['name'])
print(interface_status)