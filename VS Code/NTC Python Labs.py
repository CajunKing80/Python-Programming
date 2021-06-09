    
    ####################################################################################################
    ###################################  LAB 4 Working With Integers  ##################################
    ####################################################################################################
     
>>>
>>> vlan_id = 10
>>> 

    >>> type(vlan_id)
<class 'int'>
>>> 

>>> dir(vlan_id)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__',
'__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__',
'__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__',
'__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__',
'__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__',
'__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__',
'__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__',
'__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__',
'__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__',
'__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>>

>>> vid = "100"
>>> 

>>> print(vlan_id)
10
>>> 
>>> print(vid)
100
>>>

>>> vlan_id
10
>>> 
>>> vid
'100'
>>> 

>>> ipaddr = "10.2.9.1"
>>> 
>>> mask = 24
>>> 

>>> ipaddr + "/" + mask

>>> ipaddr + "/" + str(mask)
'10.2.9.1/24'
>>> 

>>> type(vlan_id)
<class 'int'>
>>> 
>>> vlan_id_string = str(vlan_id)
>>> 
>>> type(vlan_id_string)
<type 'str'>
>>> 

    ####################################################################################################
    ####################################  LAB 5 Working With Lists  ####################################
    ####################################################################################################

>>> mac_list = ['00.00.00.00.11.11', '00.00.00.00.22.22',
'33.00.00.00.33.33', '44:00:00:00:44:44']

>>> print(mac_list)
['00.00.00.00.11.11', '00.00.00.00.22.22', '33.00.00.00.33.33', '44:00:00:00:44:44']
>>>

>>> mac_list[3] = mac_list[3].replace(':', '.')

>>> print(mac_list)
['00.00.00.00.11.11', '00.00.00.00.22.22', '33.00.00.00.33.33', '44.00.00.00.44.44']
>>>

>>> mac_list.pop()
'44.00.00.00.44.44'
>>>
>>> mac_list
['00.00.00.00.11.11', '00.00.00.00.22.22', '33.00.00.00.33.33']
>>>

>>> mac_list.pop(1)
'00.00.00.00.22.22'
>>> 
>>> mac_list
['00.00.00.00.11.11', '33.00.00.00.33.33']
>>> 

>>> mac_list.insert(1, '00.00.00.00.22.22')
>>> 
>>> mac_list
['00.00.00.00.11.11', '00.00.00.00.22.22', '33.00.00.00.33.33']
>>>

>>> mac_list.insert(2, '22.22.00.00.00.22')
>>>
>>> mac_list
['00.00.00.00.11.11', '00.00.00.00.22.22', '22.22.00.00.00.22', '33.00.00.00.33.33']

>>> mac_list.append('55.55.55.55.55.55')
>>>
>>> mac_list.append('66.66.66.66.66.66')
>>>
>>> print(mac_list)
['00.00.00.00.11.11', '00.00.00.00.22.22', '22.22.00.00.00.22', '33.00.00.00.33.33', '55.55.55.55.55.55', '66.66.66.66.66.66']
>>>

>>> commands = ['interface Eth1/1', 'description configured by Python', 'shutdown']
>>> 

>>> cmd_string = ' ; '.join(commands)
>>> 

>>> print(cmd_string)
interface Eth1/1 ; description configured by Python ; shutdown
>>>

>>> cmd_string_n = '\n'.join(commands)
>>> 

>>> print(cmd_string_n)
interface Eth1/1
description configured by Python
shutdown
>>>

>>> cmd_string_n = '\n '.join(commands)
>>> 
>>> print(cmd_string_n)                
interface Eth1/1
 description configured by Python
 shutdown
>>> 

>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__',
'__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__',
'__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index',
'insert', 'pop', 'remove', 'reverse', 'sort']
>>>

>>> n7k_linecards = ['N7K-SUP1', 'N7K-M132XP-12', 'N7K-M148GS-11', 'N7K-M148GT-11', 'N7K-F132XP-15', 'N7K-SUP1', 'N7K-M132XP-12', 'N7K-M132XP-12', 'N7K-M148GT-11','N7K-M148GT-11']
>>> 

>>> n7k_linecards.count("N7K-SUP2")
0
>>> 
>>> n7k_linecards.count("N7K-SUP1")
2
>>> 
>>> n7k_linecards.count("N7K-M132XP-12")
3
>>>

>>> vendors = ["cisco", "cisco", "juniper", "cisco", "arista", "juniper"]
>>> 
>>> vendors.count('cisco')
3
>>> 

>>> vendors.sort()
>>> 
>>> vendors
['arista', 'cisco', 'cisco', 'cisco', 'juniper', 'juniper']
>>> 

>>> vendors.sort(reverse=True)
>>> 
>>> vendors
['juniper', 'juniper', 'cisco', 'cisco', 'cisco', 'arista']
>>> 
    
    ####################################################################################################
    ###################################  LAB 6 Working With Booleans  ##################################
    ####################################################################################################

>>> is_layer3 = True
>>>

>>> type(is_layer3)
<class 'bool'>
>>>

>>> needs_bgp = False
>>>
>>> print(needs_bgp)
False
>>>

>>> hostname = 'nxos-spine1'
>>> vendor = 'cisco'
>>> interfaces = ['Ethernet2/1', 'Ethernet2/2', 'Ethernet2/3']
>>>

>>> hostname == 'nxos-spine2'
False
>>>
>>> vendor == 'cisco'
True
>>>

>>> len(interfaces) > 3
False
>>>
>>> len(interfaces) != 3
False

>>> hostname != 'nxos-spine2'
True
>>>

>>> 'Ethernet2/4' in interfaces
False
>>>

>>> "Eth" in "Ethernet2/4"
True
>>>

>>> "eth" in "Ethernet2/4"
False
>>>

>>> "eth" in "Ethernet2/4".lower()
True
>>>

>>> 'Ethernet2/2' in interfaces and vendor == 'cisco'
True
>>>

>>> True and True and True and False
False
>>>
>>> True and True and True
True
>>>

>>> hostname == "nxos-spine2" or hostname == "nxos-spine10"
False
>>>

>>> vendor == "cisco" or hostname == "nxos-spine10"
True
>>>

>>> hostname = "r1"
>>>

>>> bool(hostname)
True
>>>

>>> vendor = ""
>>>

>>> bool(vendor)
False
>>>

>>> vendors = ['cisco']
>>>
>>> bool(vendors)
True
>>>

>>> vendors = []
>>>
>>> bool(vendors)
False
>>>
    
    ####################################################################################################
    #################################  LAB 7 Working With Dictionaries  ################################
    ####################################################################################################

>>> facts = {}
>>> 

>>> type(facts)
<class 'dict'>

>>> facts['vendor'] = 'cisco'
>>> 

>>> print(facts)
{'vendor': 'cisco'}
>>> 

>>> len(facts)
1
>>> 

>>> facts['os'] = 'nxos'
>>> facts['version'] = '7.1'
>>> facts['platform'] = 'nexus'
>>> 
>>> print(facts)
{'os': 'nxos', 'version': '7.1', 'vendor': 'cisco', 'platform': 'nexus'}
>>> 

>>> facts['version'] = "7.3"
>>> 
>>> facts
{'os': 'nxos', 'version': '7.3', 'vendor': 'cisco', 'platform': 'nexus'}
>>> 

>>> facts_2 = {'os': 'ios', 'version': '16.6', 'vendor': 'cisco', 'platform': 'catalyst'}
>>> 

>>>
>>> facts_3 = dict(hostname='APAC1', vendor='arista', location='Sydney', model='7050')
>>> facts_3
{'model': '7050', 'hostname': 'APAC1', 'vendor': 'arista', 'location': 'Sydney'}

>>> facts_4 = dict()
>>> 

>>> dir(facts)
['clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues',
'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys',
'viewvalues']
>>> # shorterned for brevity

>>> print(facts.keys())
['os', 'version', 'vendor', 'platform']
>>> 

>>> print(facts.values())
['nxos', '7.3', 'cisco', 'nexus']
>>>  

>>> print(facts_2.keys())
['vendor', 'version', 'os', 'platform']
>>> 
>>> print(facts_2.values())
['cisco', '16.6', 'ios', 'catalyst']
>>> 

>>> facts_3['hostname']
'APAC1'
>>>

>>> print(facts['os'])
nxos
>>> 

>>> print(facts['os_version'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'os_version'
>>> 

>>> facts.get('os_version')
>>> 

>>> facts.get('os_version', 'ERROR')
'ERROR'
>>>

>>> os_ver = facts.get('os_version')
>>>
>>> print(os_ver)
None
>>>

>>> facts_3
{'model': '7050', 'hostname': 'APAC1', 'vendor': 'arista', 'location': 'Sydney'}
>>> 

>>> facts_3.pop('hostname')
'APAC1'
>>>

>>> facts_3['hostname'] = 'nycr01'
>>> 
>>> facts_3
{'model': '7050', 'hostname': 'nycr01', 'vendor': 'arista', 'location': 'Sydney'}
>>> 

>>> static_facts = {'customer': 'acme', 'device_type': 'switch'}
>>> 

>>> facts.update(static_facts)
>>> 
>>> facts_2.update(static_facts)
>>> 
>>> facts_3.update(static_facts)
>>> 

>>> facts
{'customer': 'acme', 'platform': 'nexus', 'version': '7.3', 'vendor': 'cisco', 'device_type': 'switch', 'os': 'nxos'}
>>> 
>>> facts_2
{'customer': 'acme', 'platform': 'catalyst', 'version': '16.6', 'vendor': 'cisco', 'device_type': 'switch', 'os': 'ios'}
>>> 
>>> facts_3
{'customer': 'acme', 'vendor': 'arista', 'location': 'Sydney', 'device_type': 'switch', 'model': '7050', 'hostname': 'nycr01'}
>>> 
    
    ####################################################################################################
    ####################################  LAB 8 Using Python Modules  ##################################
    ####################################################################################################

>>> facts = {'platform': 'nexus', 'version': '7.3', 'vendor': 'cisco', 'device_type': 'switch', 'os': 'nxos'}
>>>

>>> print(facts)
{'platform': 'nexus', 'version': '7.3', 'vendor': 'cisco', 'device_type': 'switch', 'os': 'nxos'}
>>>
>>> import json
>>>

>>> print(json.dumps(facts, indent=4))
{
    "platform": "nexus",
    "version": "7.3",
    "vendor": "cisco",
    "device_type": "switch",
    "os": "nxos"
}
>>>

>>> print(json.dumps(facts, indent=10))
{
          "platform": "nexus",
          "version": "7.3",
          "vendor": "cisco",
          "device_type": "switch",
          "os": "nxos"
}
>>>
>>> print(json.dumps(facts, indent=20))
{
                    "platform": "nexus",
                    "version": "7.3",
                    "vendor": "cisco",
                    "device_type": "switch",
                    "os": "nxos"
}
>>>

>>> import time
>>>

>>> time.sleep(5)
>>>

>>> local_time = time.asctime()
>>>
>>> print(local_time)
Sat January 27 19:21:47 2018
>>>

>>> import os
>>>

>>> os.getcwd()
'/home/ntc'

>>> os.chdir('/home/ntc/files')
>>>
>>> os.getcwd()
'/home/ntc/files'
>>>

>>> os.getenv('HOME')
'/home/ntc'
>>>

>>> os.listdir('/home/ntc')
# output omitted
>>>

>>> os.system('date')    
Sat Feb 17 19:37:18 UTC 2018
0
>>>

>>> os.system('ifconfig')
# output omitted
>>>
    
    ####################################################################################################
    ##################################  LAB 9 Exploring Nested Objects  ################################
    ####################################################################################################

facts_list = [{'customer': 'acme', 'vendor': 'arista', 'hostname': 'APAC1', 'location': 'Sydney', 'device_type': 'switch', 'model': '7050', 'os': 'eos'}, {'customer': 'acme', 'vendor': 'juniper', 'hostname': 'EMEA1', 'location': 'London', 'device_type': 'switch', 'model': 'mx', 'os': 'junos'}, {'customer': 'acme', 'vendor': 'cisco', 'hostname': 'nycr01', 'location': 'new_york', 'device_type': 'switch', 'model': 'catalyst', 'os': 'ios'}]

>>> import json
>>>
>>> print(json.dumps(facts_list, indent=4))
[
    {
        "customer": "acme",
        "vendor": "arista",
        "hostname": "APAC1",
        "location": "Sydney",
        "device_type": "switch",
        "model": "7050",
        "os": "eos"
    },
    {
        "customer": "acme",
        "vendor": "juniper",
        "hostname": "EMEA1",
        "location": "London",
        "device_type": "switch",
        "model": "mx",
        "os": "junos"
    },
    {
        "customer": "acme",
        "vendor": "cisco",
        "hostname": "nycr01",
        "location": "new_york",
        "device_type": "switch",
        "model": "catalyst",
        "os": "ios"
    }
]
>>>

>>> type(facts_list)
<class 'list'>
>>>

>>> len(facts_list)
3
>>>

>>> type(facts_list[0])
<class 'dict'>
>>>

>>> first = facts_list[0]
>>>
>>> type(first)
<class 'dict'>
>>>

>>> print(facts_list[0])
{'customer': 'acme', 'vendor': 'arista', 'hostname': 'APAC1', 'location': 'Sydney', 'device_type': 'switch', 'model': '7050', 'os': 'eos'}
>>>

>>> print(facts_list[0]['location'])
Sydney
>>>

>>> neighbor1 = {'neighbor_interface': 'Eth1/2', 'local_interface': 'Eth1/1', 'neighbor': 'R1'}
>>>
>>> neighbor2 = {'neighbor_interface': 'Eth1/4', 'local_interface': 'Eth1/2', 'neighbor': 'R2'}
>>>

>>> neighbors = [neighbor1, neighbor2]
>>>

>>> print(neighbors)
[{'neighbor_interface': 'Eth1/2', 'local_interface': 'Eth1/1', 'neighbor': 'R1'}, {'neighbor_interface': 'Eth1/4', 'local_interface': 'Eth1/2', 'neighbor': 'R2'}]
>>>

>>> print(json.dumps(neighbors, indent=4))
[
    {
        "neighbor_interface": "Eth1/2",
        "local_interface": "Eth1/1",
        "neighbor": "R1"
    },
    {
        "neighbor_interface": "Eth1/4",
        "local_interface": "Eth1/2",
        "neighbor": "R2"
    }
]
>>>

>>> facts_list[0]['neighbors'] = neighbors
>>>

>>> print(json.dumps(facts_list, indent=4))
[
    {
        "customer": "acme",
        "neighbors": [
            {
                "neighbor_interface": "Eth1/2",
                "local_interface": "Eth1/1",
                "neighbor": "R1"
            },
            {
                "neighbor_interface": "Eth1/4",
                "local_interface": "Eth1/2",
                "neighbor": "R2"
            }
        ],
        "vendor": "arista",
        "hostname": "APAC1",
        "location": "Sydney",
        "device_type": "switch",
        "model": "7050",
        "os": "eos"
    },
    {
        "customer": "acme",
        "vendor": "juniper",
        "hostname": "EMEA1",
        "location": "London",
        "device_type": "switch",
        "model": "mx",
        "os": "junos"
    },
    {
        "customer": "acme",
        "vendor": "cisco",
        "hostname": "nycr01",
        "location": "new_york",
        "device_type": "switch",
        "model": "catalyst",
        "os": "ios"
    }
]
>>>

>>> print(facts_list[0]['neighbors'][1]['neighbor'])
R2
>>>

ntc@ntc-training:ntc$ python
Python 3.6.8 (default, Jun 11 2019, 01:16:11) 
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import json
>>>

>>> content = {'output': {'ansible_facts': {'fan_info': [{'status': 'Ok', 'model': None, 'hw_ver': '0.0', 'name': 'ChassisFan1'}, {'status': 'None', 'model': None, 'hw_ver': '0.0', 'name': 'ChassisFan2'}, {'status': 'Ok', 'model': '--', 'hw_ver': '--', 'name': 'Fan_in_PS1'}, {'status': 'Failure', 'model': '--', 'hw_ver': '--', 'name': 'Fan_in_PS2'}], 'ansible_net_model': 'NX-OSv Chassis', 'ansible_net_interfaces': {'Ethernet2/13': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/12': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/11': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/10': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/15': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/14': {'macaddress': '2cc2.604f.feb2', 'state': 'down', 'mode': 'routed', 'duplex': 'auto', 'speed': 'auto-speed', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}, 'Ethernet2/1': {'macaddress': '2cc2.604f.feb2', 'state': 'up', 'mode': 'routed', 'duplex': 'full', 'speed': '1000 Mb/s', 'type': 'Ethernet', 'bandwidth': 1000000, 'mtu': '1500'}}, 'ansible_net_all_ipv4_addresses': ['10.0.0.71'], 'ansible_net_hostname': 'nxos-spine1', 'hostname': 'nxos-spine1', 'ansible_net_serialnum': 'TM6017D760B', 'interfaces_list': ['mgmt0', 'Ethernet2/1', 'Ethernet2/2', 'Ethernet2/3', 'Ethernet2/4', 'Ethernet2/5', 'Ethernet2/6', 'Ethernet2/7', 'Ethernet2/8', 'Ethernet2/9', 'Ethernet2/10', 'Ethernet2/11', 'Ethernet2/12', 'Ethernet2/13', 'Ethernet2/14', 'Ethernet2/15'], 'ansible_net_gather_subset': ['hardware', 'default', 'interfaces', 'legacy'], 'power_supply_info': [{'status': 'Ok', 'model': 'DS-CAC-845W', 'number': 1}, {'status': 'Absent', 'model': '------------', 'number': 2}], 'platform': 'NX-OSv Chassis', 'ansible_net_version': '7.3(1)D1(1) [build 7.3(1)D1(0.10)]', 'module': [{'status': 'active *', 'model': 'N7K-SUP1', 'type': 'NX-OSv Supervisor Module', 'ports': 0}, {'status': 'ok', 'model': 'N7K-F248XP-25', 'type': 'NX-OSv Ethernet Module', 'ports': 48}, {'status': 'ok', 'model': 'N7K-F248XP-25', 'type': 'NX-OSv Ethernet Module', 'ports': 48}, {'status': 'ok', 'model': 'N7K-F248XP-25', 'type': 'NX-OSv Ethernet Module', 'ports': 48}], 'ansible_net_all_ipv6_addresses': [], 'ansible_net_memtotal_mb': 3908, 'ansible_net_filesystems': ['bootflash:'], 'ansible_net_image': 'bootflash:///titanium-d1.7.3.1.D1.0.10.bin', 'os': '7.3(1)D1(1) [build 7.3(1)D1(0.10)]', 'vlan_list': [1]}}}
>>>

>>> print(json.dumps(content, indent=4))
{
    "output": {
        "ansible_facts": {
            "fan_info": [
                {
                    "status": "Ok",
                    "model": null,
                    "hw_ver": "0.0",
                    "name": "ChassisFan1"
                },
                {
                    "status": "None",
                    "model": null,
                    "hw_ver": "0.0",
                    "name": "ChassisFan2"
                },
                {
                    "status": "Ok",
                    "model": "--",
                    "hw_ver": "--",
                    "name": "Fan_in_PS1"
                },
                {
                    "status": "Failure",
                    "model": "--",
                    "hw_ver": "--",
                    "name": "Fan_in_PS2"
                }
            ],
            "hostname": "nxos-spine1",
            "ansible_net_serialnum": "TM6017D760B",
            "platform": "NX-OSv Chassis",
            "ansible_net_all_ipv4_addresses": [
                "10.0.0.71"
            ],
            "ansible_net_model": "NX-OSv Chassis",
            "ansible_net_hostname": "nxos-spine1",
            "interfaces_list": [
                "mgmt0",
                "Ethernet2/1",
                "Ethernet2/2",
                "Ethernet2/3",
                "Ethernet2/4",
                "Ethernet2/5",
                "Ethernet2/6",
                "Ethernet2/7",
                "Ethernet2/8",
                "Ethernet2/9",
                "Ethernet2/10",
                "Ethernet2/11",
                "Ethernet2/12",
                "Ethernet2/13",
                "Ethernet2/14",
                "Ethernet2/15"
            ],
            "ansible_net_gather_subset": [
                "hardware",
                "default",
                "interfaces",
                "legacy"
            ],
            "power_supply_info": [
                {
                    "status": "Ok",
                    "model": "DS-CAC-845W",
                    "number": 1
                },
                {
                    "status": "Absent",
                    "model": "------------",
                    "number": 2
                }
            ],
            "ansible_net_interfaces": {
                "Ethernet2/13": {
                    "macaddress": "2cc2.604f.feb2",
                    "state": "down",
                    "mode": "routed",
                    "duplex": "auto",
                    "type": "Ethernet",
                    "speed": "auto-speed",
                    "bandwidth": 1000000,
                    "mtu": "1500"
                },
                "Ethernet2/12": {
                    "macaddress": "2cc2.604f.feb2",
                    "state": "down",
                    "mode": "routed",
                    "duplex": "auto",
                    "type": "Ethernet",
                    "speed": "auto-speed",
                    "bandwidth": 1000000,
                    "mtu": "1500"
                },
                "Ethernet2/11": {
                    "macaddress": "2cc2.604f.feb2",
                    "state": "down",
                    "mode": "routed",
                    "duplex": "auto",
                    "type": "Ethernet",
                    "speed": "auto-speed",
                    "bandwidth": 1000000,
                    "mtu": "1500"
                },
                "Ethernet2/10": {
                    "macaddress": "2cc2.604f.feb2",
                    "state": "down",
                    "mode": "routed",
                    "duplex": "auto",
                    "type": "Ethernet",
                    "speed": "auto-speed",
                    "bandwidth": 1000000,
                    "mtu": "1500"
                },
                "Ethernet2/15": {
                    "macaddress": "2cc2.604f.feb2",
                    "state": "down",
                    "mode": "routed",
                    "duplex": "auto",
                    "type": "Ethernet",
                    "speed": "auto-speed",
                    "bandwidth": 1000000,
                    "mtu": "1500"
                },
                "Ethernet2/14": {
                    "macaddress": "2cc2.604f.feb2",
                    "state": "down",
                    "mode": "routed",
                    "duplex": "auto",
                    "type": "Ethernet",
                    "speed": "auto-speed",
                    "bandwidth": 1000000,
                    "mtu": "1500"
                },
                "Ethernet2/1": {
                    "macaddress": "2cc2.604f.feb2",
                    "state": "up",
                    "mode": "routed",
                    "duplex": "full",
                    "type": "Ethernet",
                    "speed": "1000 Mb/s",
                    "bandwidth": 1000000,
                    "mtu": "1500"
                }
            },
            "ansible_net_version": "7.3(1)D1(1) [build 7.3(1)D1(0.10)]",
            "module": [
                {
                    "status": "active *",
                    "model": "N7K-SUP1",
                    "type": "NX-OSv Supervisor Module",
                    "ports": 0
                },
                {
                    "status": "ok",
                    "model": "N7K-F248XP-25",
                    "type": "NX-OSv Ethernet Module",
                    "ports": 48
                },
                {
                    "status": "ok",
                    "model": "N7K-F248XP-25",
                    "type": "NX-OSv Ethernet Module",
                    "ports": 48
                },
                {
                    "status": "ok",
                    "model": "N7K-F248XP-25",
                    "type": "NX-OSv Ethernet Module",
                    "ports": 48
                }
            ],
            "ansible_net_all_ipv6_addresses": [],
            "ansible_net_memtotal_mb": 3908,
            "ansible_net_filesystems": [
                "bootflash:"
            ],
            "ansible_net_image": "bootflash:///titanium-d1.7.3.1.D1.0.10.bin",
            "os": "7.3(1)D1(1) [build 7.3(1)D1(0.10)]",
            "vlan_list": [
                1
            ]
        }
    }
}
>>>

>>> len(content)
1
>>>

>>> len(content)
1
>>>

>>> print(content.keys())
dict_keys(['output'])
>>>

>>> output = content['output']
>>>

>>> type(output)
<class 'dict'>
>>>

>>> print(output.keys())
dict_keys(['ansible_facts'])
>>>

>>> print(json.dumps(output, indent=4))
{
    "ansible_facts": {
        "fan_info": [
            {
                "status": "Ok",
                "model": null,
                "hw_ver": "0.0",
                "name": "ChassisFan1"
            },
            {
                "status": "None",
                "model": null,
                "hw_ver": "0.0",
                "name": "ChassisFan2"
            },
            {
                "status": "Ok",
                "model": "--",
                "hw_ver": "--",
                "name": "Fan_in_PS1"
            },
            {
                "status": "Failure",
                "model": "--",
                "hw_ver": "--",
                "name": "Fan_in_PS2"
            }
        ],
        "hostname": "nxos-spine1",
        "ansible_net_serialnum": "TM6017D760B",
        "platform": "NX-OSv Chassis",
        "ansible_net_all_ipv4_addresses": [
            "10.0.0.71"
        ],
        "ansible_net_model": "NX-OSv Chassis",
        "ansible_net_hostname": "nxos-spine1",
        "interfaces_list": [
            "mgmt0",
            "Ethernet2/1",
            "Ethernet2/2",
            "Ethernet2/3",
            "Ethernet2/4",
            "Ethernet2/5",
            "Ethernet2/6",
            "Ethernet2/7",
            "Ethernet2/8",
            "Ethernet2/9",
            "Ethernet2/10",
            "Ethernet2/11",
            "Ethernet2/12",
            "Ethernet2/13",
            "Ethernet2/14",
            "Ethernet2/15"
        ],
        "ansible_net_gather_subset": [
            "hardware",
            "default",
            "interfaces",
            "legacy"
        ],
        "power_supply_info": [
            {
                "status": "Ok",
                "model": "DS-CAC-845W",
                "number": 1
            },
            {
                "status": "Absent",
                "model": "------------",
                "number": 2
            }
        ],
        "ansible_net_interfaces": {
            "Ethernet2/13": {
                "macaddress": "2cc2.604f.feb2",
                "duplex": "auto",
                "type": "Ethernet",
                "state": "down",
                "mtu": "1500",
                "bandwidth": 1000000,
                "mode": "routed",
                "speed": "auto-speed"
            },
            "Ethernet2/12": {
                "macaddress": "2cc2.604f.feb2",
                "duplex": "auto",
                "type": "Ethernet",
                "state": "down",
                "mtu": "1500",
                "bandwidth": 1000000,
                "mode": "routed",
                "speed": "auto-speed"
            },
            "Ethernet2/11": {
                "macaddress": "2cc2.604f.feb2",
                "duplex": "auto",
                "type": "Ethernet",
                "state": "down",
                "mtu": "1500",
                "bandwidth": 1000000,
                "mode": "routed",
                "speed": "auto-speed"
            },
            "Ethernet2/10": {
                "macaddress": "2cc2.604f.feb2",
                "duplex": "auto",
                "type": "Ethernet",
                "state": "down",
                "mtu": "1500",
                "bandwidth": 1000000,
                "mode": "routed",
                "speed": "auto-speed"
            },
            "Ethernet2/15": {
                "macaddress": "2cc2.604f.feb2",
                "duplex": "auto",
                "type": "Ethernet",
                "state": "down",
                "mtu": "1500",
                "bandwidth": 1000000,
                "mode": "routed",
                "speed": "auto-speed"
            },
            "Ethernet2/14": {
                "macaddress": "2cc2.604f.feb2",
                "duplex": "auto",
                "type": "Ethernet",
                "state": "down",
                "mtu": "1500",
                "bandwidth": 1000000,
                "mode": "routed",
                "speed": "auto-speed"
            },
            "Ethernet2/1": {
                "macaddress": "2cc2.604f.feb2",
                "duplex": "full",
                "type": "Ethernet",
                "state": "up",
                "mtu": "1500",
                "bandwidth": 1000000,
                "mode": "routed",
                "speed": "1000 Mb/s"
            }
        },
        "ansible_net_version": "7.3(1)D1(1) [build 7.3(1)D1(0.10)]",
        "module": [
            {
                "status": "active *",
                "model": "N7K-SUP1",
                "type": "NX-OSv Supervisor Module",
                "ports": 0
            },
            {
                "status": "ok",
                "model": "N7K-F248XP-25",
                "type": "NX-OSv Ethernet Module",
                "ports": 48
            },
            {
                "status": "ok",
                "model": "N7K-F248XP-25",
                "type": "NX-OSv Ethernet Module",
                "ports": 48
            },
            {
                "status": "ok",
                "model": "N7K-F248XP-25",
                "type": "NX-OSv Ethernet Module",
                "ports": 48
            }
        ],
        "ansible_net_all_ipv6_addresses": [],
        "ansible_net_memtotal_mb": 3908,
        "ansible_net_filesystems": [
            "bootflash:"
        ],
        "ansible_net_image": "bootflash:///titanium-d1.7.3.1.D1.0.10.bin",
        "os": "7.3(1)D1(1) [build 7.3(1)D1(0.10)]",
        "vlan_list": [
            1
        ]
    }
}

>>> print(json.dumps(output['ansible_facts']['fan_info'], indent=4))
[
    {
        "status": "Ok",
        "model": null,
        "hw_ver": "0.0",
        "name": "ChassisFan1"
    },
    {
        "status": "None",
        "model": null,
        "hw_ver": "0.0",
        "name": "ChassisFan2"
    },
    {
        "status": "Ok",
        "model": "--",
        "hw_ver": "--",
        "name": "Fan_in_PS1"
    },
    {
        "status": "Failure",
        "model": "--",
        "hw_ver": "--",
        "name": "Fan_in_PS2"
    }
]

>>> print(type(output['ansible_facts']['fan_info']))
<class 'list'>
>>>

>>> print(json.dumps(output['ansible_facts']['fan_info'][1], indent=4))
{
    "status": "None",
    "model": null,
    "hw_ver": "0.0",
    "name": "ChassisFan2"
}
>>>

>>> fan_name = output['ansible_facts']['fan_info'][1]['name']
>>>
>>> print(fan_name)
ChassisFan2
>>>

>>> interfaces = output['ansible_facts']['ansible_net_interfaces']
>>> print(interfaces.keys())
# output omitted

>>> mac = output['ansible_facts']['ansible_net_interfaces']['Ethernet2/11']['macaddress']
>>> print(mac)
2cc2.604f.feb2
>>>

vlans = {
    "output": {
        "proposed": {
            "name": "NTC"
        },
        "existing_vlans_list": [
            "1"
        ],
        "end_state_vlans_list": [
            "1",
            "100"
        ],
        "existing": {},
        "updates": [
            "vlan 100",
            "name NTC",
            "exit"
        ],
        "end_state": {
            "vlan_state": "active",
            "mapped_vni": "",
            "admin_state": "up",
            "name": "NTC",
            "vlan_id": "100"
        },
        "proposed_vlans_list": [
            "100"
        ]
    }
}

>>> existing_vlans = vlans['output']['existing_vlans_list']
>>> proposed_vlans = vlans['output']['proposed_vlans_list']
>>>

>>> end_state_vlans = existing_vlans + proposed_vlans
>>>
>>> print(end_state_vlans)
['1', '100']
>>>


>>> print(vlans['output']['updates'][2])
exit
>>>


>>> print(vlans['output']['updates'][-1])
exit
>>>
    
    ####################################################################################################
    ###################################  LAB 10 Basic File OPerations  #################################
    ####################################################################################################

ntc@ntc-training:ntc$ cd files
ntc@ntc-training:files$ 

ntc@ntc-training:files$ cat vlan_ids.conf
vlan 1
vlan 2
vlan 10
vlan 20
vlan 50

ntc@ntc-training:files$ python
Python 3.6.8 (default, Jun 11 2019, 01:16:11) 
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> vlan_file = open('vlan_ids.conf', 'r')
>>>

type(vlan_file)
<class '_io.TextIOWrapper'>

>>> dir(vlan_file)
['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__',
 '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__',
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer',
 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines',
 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines']
>>>

>>> data = vlan_file.read()
>>>

>>> print(data)
vlan 1
vlan 2
vlan 10
vlan 20
vlan 50
>>>

>>> vlan_file.close()
>>>

>>> out_file = open('interface.cfg', 'w')
>>>

>>> out_file.write("interface Eth1\n")
15
>>> out_file.write(" speed 100\n")
11
>>> out_file.write(" duplex full\n")
13

>>> out_file.close()
>>>

ntc@ntc-training:ntc$ cd files
ntc@ntc-training:files$ cat interface.cfg
interface Eth1
 speed 100
 duplex full

>>> with open("interfaces_2.cfg", "w") as out_file:
...     out_file.write("interface Eth2\n")
...     out_file.write(" speed 10\n")   
...     out_file.write(" duplex half\n")
... 
15
10
13

>>> with open("vlan_ids.conf", "r") as vlan_file:
...     data = vlan_file.read()
...
>>> print(data)
vlan 1
vlan 2
vlan 10
vlan 20
vlan 50
>>>
    
    ####################################################################################################
    ###################################  LAB 11 Writing Python Scripts  ################################
    ####################################################################################################

ntc@ntc-training:ntc$ mkdir scripts
ntc@ntc-training:ntc$ 

ntc@ntc-training:ntc$ cd scripts
ntc@ntc-training:scripts$

ntc@ntc-training:scripts$ touch networkauto.py
ntc@ntc-training:scripts$

#! /usr/bin/env python

print('Hello Network Automation!')

ntc@ntc-training:scripts$ python networkauto.py
Hello Network Automation!

#! /usr/bin/env python

import json 

facts1 = {'vendor': 'cisco', 'os': 'nxos', 'ipaddr': '10.1.1.1'}
facts2 = {'vendor': 'cisco', 'os': 'ios', 'ipaddr': '10.2.1.1'}
facts3 = {'vendor': 'arista', 'os': 'eos', 'ipaddr': '10.1.1.2'}

devices = [facts1, facts2, facts3]

print(json.dumps(devices, indent=4))


ntc@ntc-training:scripts$ python print_facts.py
[
    {
        "vendor": "cisco",
        "os": "nxos",
        "ipaddr": "10.1.1.1"
    },
    {
        "vendor": "cisco",
        "os": "ios",
        "ipaddr": "10.2.1.1"
    },
    {
        "vendor": "arista",
        "os": "eos",
        "ipaddr": "10.1.1.2"
    }
]
    
    ####################################################################################################
    ################################  LAB 12 Getting Started with Netmiko  #############################
    ####################################################################################################

oot@ntc-training:~$ ping csr1 -c 3
PING csr1 (172.21.0.6) 56(84) bytes of data.
64 bytes from csr1.ntc-training (172.21.0.6): icmp_seq=1 ttl=64 time=0.053 ms
64 bytes from csr1.ntc-training (172.21.0.6): icmp_seq=2 ttl=64 time=0.059 ms
64 bytes from csr1.ntc-training (172.21.0.6): icmp_seq=3 ttl=64 time=0.073 ms

ntc@ntc-training:ntc$ cd files
ntc@ntc-training:files$

>>> from netmiko import ConnectHandler
>>>
>>> platform = 'cisco_ios'
>>> host = 'csr1'
>>> username = 'ntc'
>>> password = 'ntc123'
>>>
>>> device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
>>>
>>>

>>> dir(device)
['__class__', '__delattr__', '__dict__', '__doc__', '__enter__', '__exit__',
'__format__', '__getattribute__', '__hash__', '__init__', '__module__',
__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_autodetect_fs',
'_build_ssh_client', '_connect_params_dict', '_lock_netmiko_session',
'_modify_connection_params', '_read_channel', '_read_channel_expect',
'_read_channel_timing', '_sanitize_output', '_session_locker',
'_test_channel_read', '_timeout_exceeded', '_unlock_netmiko_session',
'_use_ssh_config', '_write_channel', 'allow_agent', 'alt_host_keys',
'alt_key_file', 'ansi_escape_codes', 'base_prompt', 'check_config_mode',
'check_enable_mode', 'cleanup', 'clear_buffer', 'commit', 'config_mode',
'device_type', 'disable_paging', 'disconnect', 'enable', 'establish_connection'
, 'exit_config_mode', 'exit_enable_mode', 'find_prompt', 'global_delay_factor',
 'host', 'is_alive', 'keepalive', 'key_file', 'key_policy', 'normalize_cmd',
 'normalize_linefeeds', 'password', 'port', 'protocol', 'read_channel', '
'read_until_pattern', 'read_until_prompt', 'read_until_prompt_or_pattern',
 'remote_conn', 'remote_conn_pre', 'secret', 'select_delay_factor',
 'send_command', 'send_command_expect', 'send_command_timing',
 'send_config_from_file', 'send_config_set', 'session_preparation',
 'session_timeout', 'set_base_prompt', 'set_terminal_width',
 'special_login_handler', 'ssh_config_file', 'strip_ansi_escape_codes',
 'strip_backspaces', 'strip_command', 'strip_prompt', 'system_host_keys',
 'telnet_login', 'timeout', 'use_keys', 'username', 'verbose', 'write_channel']
>>>

>>> device.is_alive()
True
>>>

>>> help(device.is_alive)
Help on method is_alive in module netmiko.base_connection:

is_alive(self) method of netmiko.cisco.cisco_ios.CiscoIosBase instance
    Returns a boolean flag with the state of the connection.
(END)

>>> output = device.send_command('show version')
>>>
>>> print(output)
Cisco IOS XE Software, Version 16.06.02
Cisco IOS Software [Everest], Virtual XE Software (X86_64_LINUX_IOSD-UNIVERSALK9-M), Version 16.6.2, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2017 by Cisco Systems, Inc.
Compiled Wed 01-Nov-17 07:24 by mcpre


Cisco IOS-XE software, Copyright (c) 2005-2017 by cisco Systems, Inc.
All rights reserved.  Certain components of Cisco IOS-XE software are
licensed under the GNU General Public License ("GPL") Version 2.0.  The
software code licensed under GPL Version 2.0 is free software that comes
with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
GPL code under the terms of GPL Version 2.0.  For more details, see the
documentation or "License Notice" file accompanying the IOS-XE software,
or the applicable URL provided on the flyer accompanying the IOS-XE
software.


ROM: IOS-XE ROMMON

csr1 uptime is 27 minutes
Uptime for this control processor is 32 minutes
System returned to ROM by reload
System image file is "bootflash:packages.conf"
Last reload reason: reload



This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

License Level: ax
License Type: Default. No valid license found.
Next reload license Level: ax

cisco CSR1000V (VXE) processor (revision VXE) with 2190795K/3075K bytes of memory.
Processor board ID 9KIBQAQ3OPE
4 Gigabit Ethernet interfaces
32768K bytes of non-volatile configuration memory.
3984708K bytes of physical memory.
7774207K bytes of virtual hard disk at bootflash:.
0K bytes of WebUI ODM Files at webui:.

Configuration register is 0x2102

>>>

>>> output = device.send_command('show version | include register')
>>>
>>> print(output)
Configuration register is 0x2102
>>>

>>> '0x2102' in output
True
>>>

>>> '0x2142' not in output
True
>>>

>>> output = device.send_command('wr mem')
>>>
>>> print(output)
Building configuration...
[OK]
>>>

>>> output = device.send_command('ping 10.0.0.15')
>>>
>>> print(output)
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 10.0.0.15, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
>>>

>>> print(output)
config term
Enter configuration commands, one per line.  End with CNTL/Z.
csr1(config)#interface Loopback100
csr1(config-if)#ip address 10.200.1.20 255.255.255.0
csr1(config-if)#end
csr1#
>>>

>>> help(device.send_config_set)

Help on method send_config_set in module netmiko.base_connection:

send_config_set(self, config_commands=None, exit_config_mode=True, **kwargs) method of netmiko.cisco.cisco_nxos_ssh.CiscoNxosSSH instance
    Send group of configuration commands down the SSH channel.

    config_commands is an iterable containing all of the configuration commands.
    The commands will be executed one after the other.

    Automatically exits/enters configuration mode.

    **kwargs will allow passing of all the arguments to send_command
    strip_prompt and strip_command will be set to False if not explicitly set in
    the method call.
(END)

>>> snmp_commands = ['snmp-server community ntclab RO', 'snmp-server community ntcrw RW']
>>>
>>> response = device.send_config_set(snmp_commands)
>>>
>>> verify = device.send_command('show run | inc snmp-server community')
>>>
>>> print(verify)
snmp-server community ntclab RO
snmp-server community ntcrw RW
>>>

>>> import os
>>>
>>> os.system('ls /home/ntc/files/config.txt')
/home/ntc/files/config.txt
0

>>> os.system('cat /home/ntc/files/config.txt')
!
snmp-server community supersecret RW
snmp-server community notprivate RO
!
interface Loopback101
 ip address 10.9.88.1 255.255.255.0
!
0

>>> print(output)
config term
Enter configuration commands, one per line.  End with CNTL/Z.
csr1(config)#!
csr1(config)#snmp-server community supersecret RW
csr1(config)#snmp-server community notprivate RO
csr1(config)#!
csr1(config)#interface Loopback101
csr1(config-if)# ip address 10.9.88.1 255.255.255.0
csr1(config-if)#!
csr1(config-if)#end
csr1#
>>>

>>> device.config_mode()
u'config term\nEnter configuration commands, one per line.  End with CNTL/Z.\ncsr1(config)#'
>>>

>>> data = device.config_mode()
>>> data = device.send_command_timing('interface Gigabit3')
>>>

>>> print(device.find_prompt())
csr1(config-if)#
>>>

>>> device.exit_config_mode()
u'end\ncsr1#'
>>>

>>> device.disconnect()
>>>

>>> device.is_alive()
False
>>>

>>> device.establish_connection()
u''
>>>

>>> device.disconnect()
>>>
    
    ####################################################################################################
    #########################################  LAB 13 Challenge  #######################################
    ####################################################################################################

#! /usr/bin/env python

from netmiko import ConnectHandler

print("Connecting to device | CSR1")

csr1 = ConnectHandler(host='csr1', username='ntc', password='ntc123', device_type='cisco_ios')

print("Saving configuration | CSR1")

csr1.send_command("wr mem")

print("Backing up configuration | CSR1")

csr1.send_command("term len 0")
csr1_config = csr1.send_command("show run")

print("Writing config to file | CSR1\n")

with open("/home/ntc/scripts/configs/csr1.cfg", "w") as config_file:
    config_file.write(csr1_config)

print("Connecting to device | CSR2")

csr2 = ConnectHandler(host='csr2', username='ntc', password='ntc123', device_type='cisco_ios')

print("Saving configuration | CSR2")

csr2.send_command("wr mem")

print("Backing up configuration | CSR2")

csr2.send_command("term len 0")
csr2_config = csr1.send_command("show run")

print("Writing config to file | CSR2\n")

with open("/home/ntc/scripts/configs/csr2.cfg", "w") as config_file:
    config_file.write(csr2_config)
    
    ####################################################################################################
    ########################################  LAB 14 Conditionals  #####################################
    ####################################################################################################

nxos-spine10

>>> hostname != 'nxos-spine2'
True
>>>

>>> "eth" in "Ethernet2/4"
False
>>>

>>> hostname == "nxos-spine2" or hostname == "nxos-spine10"
True
>>>

>>> vendor = ""
>>>

>>> bool(vendor)
False
>>>

>>> vendors = ['cisco']
>>>
>>> bool(vendors)
True
>>>

>>> hostname = "nxos-spine1"
>>>
>>> if hostname == "nxos-spine1":
...     print("The hostname is correct.")
...
The hostname is correct.
>>>

>>> platforms = ['nexus', 'catalyst', 'asa', 'csr', 'aci']
>>>
>>> if 'catalyst' in platforms:
...     print("Catalyst has been found in the network.")
...
Catalyst has been found in the network.
>>>

>>> supported_platforms = ['nexus', 'catalyst']
>>>
>>> for platform in platforms:
...     if platform in supported_platforms:
...         print("Platform {}  -- SUPPORTED".format(platform))
...
...
Platform nexus  -- SUPPORTED
Platform catalyst  -- SUPPORTED
>>>

>>> supported_platforms = ['nexus', 'catalyst']
>>>
>>> for platform in platforms:
...     if platform in supported_platforms:
...         print("Platform {}  -- SUPPORTED".format(platform))
...
...
Platform nexus  -- SUPPORTED
Platform catalyst  -- SUPPORTED
>>>

>>> for platform in platforms:
...     if platform in supported_platforms:
...         print("Platform {}  -- SUPPORTED".format(platform))
...     else:
...         print("Platform {}  -- NOT SUPPORTED".format(platform))
...
Platform nexus  -- SUPPORTED
Platform catalyst  -- SUPPORTED
Platform asa  -- NOT SUPPORTED
Platform csr  -- NOT SUPPORTED
Platform aci  -- NOT SUPPORTED
>>>

>>> vlans = [{'name': 'web', 'id': 10}, {'name': 'app', 'id': 20}, {'name': 'db', 'id': 30}]
>>>

>>> for item in vlans:
...     if item['id'] == 20:
...         print("VLAN NAME: {}".format(item['name']))
...
VLAN NAME: app
>>>

>>> for item in vlans:
...   vlan_id = item['id']
...   name = item['name']
...   print("vlan {}".format(vlan_id))
...   print(" name {}".format(name))
...
vlan 10
 name web
vlan 20
 name app
vlan 30
 name db
>>>

>>> vlans[1].pop('name')
'app'
>>>

>>> for item in vlans:
...   vlan_id = item['id']
...   name = item.get('name')
...   print("vlan {}".format(vlan_id))
...   if name:
...     print(" name {}".format(name))
...
vlan 10
 name web
vlan 20
vlan 30
 name db
>>>

>>> devices = [{'platform': 'nexus', 'hostname': 'nycr01'}, {'platform': 'catalyst', 'hostname': 'nycsw02'}, {'platform': 'mx', 'hostname': 'nycr03'}, {'platform': 'srx', 'hostname': 'nycfw01'}, {'platform': 'asa', 'hostname': 'nycfw02'}]
>>> print(devices)
[{'platform': 'nexus', 'hostname': 'nycr01'}, {'platform': 'catalyst', 'hostname': 'nycsw02'}, {'platform': 'mx', 'hostname': 'nycr03'}, {'platform': 'srx', 'hostname': 'nycfw01'}, {'platform': 'asa', 'hostname': 'nycfw02'}]
>>>

>>> for item in devices:
...     platform = item.get('platform')
...     if platform == "nexus":
...         print("Vendor is Cisco")
...     elif platform == "catalyst":
...         print("Vendor is Cisco")
...     elif platform == "aci":
...         print("Vendor is Cisco")
...     elif platform == "srx" or platform == "mx":
...         print("Vendor is Juniper")
...     else:
...         print("Unknown Vendor")
...
Vendor is Cisco
Vendor is Cisco
Vendor is Juniper
Vendor is Juniper
Unknown Vendor
>>>

>>> cisco_platforms = ['catalyst', 'nexus', 'aci']
>>> juniper_platforms = ['mx', 'srx']
>>>
>>> for item in devices:
...     platform = item.get('platform')
...     if platform in cisco_platforms:
...         print("Vendor is Cisco")
...     elif platform in juniper_platforms:
...         print("Vendor is Juniper")
...     else:
...         print("Unknown Vendor")
...
Vendor is Cisco
Vendor is Cisco
Vendor is Juniper
Vendor is Juniper
Unknown Vendor
>>>
    
    ####################################################################################################
    ############################################  LAB 15 Loops  ########################################
    ####################################################################################################

>>> commands = ['interface Eth2/1', 'description Configured by Python', 'speed 100', 'duplex full']
>>>

>>> for command in commands:
...      print(command)
...
interface Eth2/1
description Configured by Python
speed 100
duplex full
>>>

>>> for item in commands:
...     print(item)
...
interface Eth2/1
description Configured by Python
speed 100
duplex full
>>>

Connecting to device | csr1

>>> routers = ['csr1', 'csr2', 'csr3']
>>>
>>> for router in routers:
...     print("Connecting to device | {}".format(router))
...
Connecting to device | csr1
Connecting to device | csr2
Connecting to device | csr3
>>>

>>> interface = {}
>>> interface['duplex'] = 'full'
>>> interface['speed'] = '100'
>>> interface['description'] = 'Configured by Python'
>>>
>>> print(interface)
{'duplex': 'full', 'speed': '100', 'description': 'Configured by Python'}
>>>

>>> for key in interface.keys():
...      print(key)
...
duplex
speed
description
>>>

>>> for value in interface.values():
...     print(value)
...
full
100
Configured by Python
>>>


>>> for key, value in interface.items():
...     print(key, '--->', value)
...
duplex ---> full
speed ---> 100
description ---> Configured by Python
>>>

>>> for feature, configured_value in interface.items():
...     print(feature, '--->', configured_value)
...
duplex ---> full
speed ---> 100
description ---> Configured by Python
>>>

>>> vlan10 = {'name': 'web', 'id': '10'}
>>> vlan20 = {'name': 'app', 'id': '20'}
>>> vlan30 = {'name': 'db', 'id': '30'}


>>> vlans = [vlan10, vlan20, vlan30]
>>>

>>> print(vlans)
[{'name': 'web', 'id': '10'}, {'name': 'app', 'id': '20'}, {'name': 'db', 'id': '30'}]
>>>

>>> import json
>>>
>>> print(json.dumps(vlans, indent=4))
[
    {
        "name": "web",
        "id": "10"
    },
    {
        "name": "app",
        "id": "20"
    },
    {
        "name": "db",
        "id": "30"
    }
]
>>>

>>> for vlan in vlans:
...     print(vlan)
...
{'name': 'web', 'id': '10'}
{'name': 'app', 'id': '20'}
{'name': 'db', 'id': '30'}
>>>

>>> for vlan in vlans:
...     print(vlan)
...     print(type(vlan))
...
{'name': 'web', 'id': '10'}
<class 'dict'>
{'name': 'app', 'id': '20'}
<class 'dict'>
{'name': 'db', 'id': '30'}
<class 'dict'>
>>>

vlan 10
 name web
vlan 20
 name app
vlan 30
 name db

>>> for vlan in vlans:
...     print("vlan {}".format(vlan['id']))
...     print(" name {}".format(vlan['name']))
...
vlan 10
 name web
vlan 20
 name app
vlan 30
 name db
>>>
    
    ####################################################################################################
    ##############################  LAB 16 Re-factoring Code Using Loops  ##############################
    ####################################################################################################

#! /usr/bin/env python

from netmiko import ConnectHandler

print("Connecting to device | CSR1")

csr1 = ConnectHandler(host='csr1', username='ntc', password='ntc123', device_type='cisco_ios')

print("Saving configuration | CSR1")

csr1.send_command("wr mem")

print("Backing up configuration | CSR1")

csr1.send_command("term len 0")
csr1_config = csr1.send_command("show run")

print("Writing config to file | CSR1\n")

with open("/home/ntc/scripts/configs/csr1.cfg", "w") as config_file:
    config_file.write(csr1_config)

print("Connecting to device | CSR2")

csr2 = ConnectHandler(host='csr2', username='ntc', password='ntc123', device_type='cisco_ios')

print("Saving configuration | CSR2")

csr2.send_command("wr mem")

print("Backing up configuration | CSR2")

csr2.send_command("term len 0")
csr2_config = csr1.send_command("show run")

print("Writing config to file | CSR2\n")

with open("/home/ntc/scripts/configs/csr2.cfg", "w") as config_file:
    config_file.write(csr2_config)

#! /usr/bin/env python

from netmiko import ConnectHandler

devices = ['csr1']

#! /usr/bin/env python

from netmiko import ConnectHandler

devices = ['csr1']

for device in devices:
    print("Connecting to device | {}".format(device))
    csr1 = ConnectHandler(host=device, username='ntc', password='ntc123', device_type='cisco_ios')
    print("Saving configuration | {}".format(device))
    csr1.send_command("wr mem")
    print("Backing up configuration | {}".format(device))
    csr1.send_command("term len 0")
    csr1_config = csr1.send_command("show run")
    print("Writing config to file | {}\n".format(device))
    with open("/home/ntc/files/scripts/configs/{}.cfg".format(device), "w") as config_file:
        config_file.write(csr1_config)
    print("Connecting to device | CSR2")
    csr2 = ConnectHandler(host='csr2', username='ntc', password='ntc123', device_type='cisco_ios')
    print("Saving configuration | CSR2")
    csr2.send_command("wr mem")
    print("Backing up configuration | CSR2")
    csr2.send_command("term len 0")
    csr2_config = csr1.send_command("show run")
    print("Writing config to file | CSR2\n")
    with open("/home/ntc/files/scripts/configs/csr2.cfg", "w") as config_file:
        config_file.write(csr2_config)


ntc@ntc-training:scripts$ python backupv2.py
Connecting to device | csr1
Saving configuration | csr1
Backing up configuration | csr1
Writing config to file | csr1

Connecting to device | CSR2
Saving configuration | CSR2
Backing up configuration | CSR2
Writing config to file | CSR2

#! /usr/bin/env python

from netmiko import ConnectHandler

devices = ['csr1', 'csr2']

for device in devices:
    print("Connecting to device | {}".format(device))
    csr1 = ConnectHandler(host=device, username='ntc', password='ntc123', device_type='cisco_ios')
    print("Saving configuration | {}".format(device))
    csr1.send_command("wr mem")
    print("Backing up configuration | {}".format(device))
    csr1.send_command("term len 0")
    csr1_config = csr1.send_command("show run")
    print("Writing config to file | {}\n".format(device))
    with open("/home/ntc/files/scripts/configs/{}.cfg".format(device), "w") as config_file:
        config_file.write(csr1_config)

#! /usr/bin/env python

from netmiko import ConnectHandler

devices = ['csr1', 'csr2']

for device in devices:
    print("Connecting to device | {}".format(device))
    net_device = ConnectHandler(host=device, username='ntc', password='ntc123', device_type='cisco_ios')
    print("Saving configuration | {}".format(device))
    net_device.send_command("wr mem")
    print("Backing up configuration | {}".format(device))
    net_device.send_command("term len 0")
    config = net_device.send_command("show run")
    print("Writing config to file | {}\n".format(device))
    with open("/home/ntc/files/scripts/configs/{}.cfg".format(device), "w") as config_file:
        config_file.write(config)

#! /usr/bin/env python

from netmiko import ConnectHandler

devices = ['csr1', 'csr2']

for device in devices:
    print("Connecting to device | {}".format(device))
    net_device = ConnectHandler(host=device, username='ntc', password='ntc123', device_type='cisco_ios')
    print("Saving configuration | {}".format(device))
    net_device.send_command("wr mem")
    print("Backing up configuration | {}".format(device))
    net_device.send_command("term len 0")
    config = net_device.send_command("show run")
    print("Writing config to file | {}\n".format(device))
    with open("/home/ntc/files/scripts/configs/{}.cfg".format(device), "w") as config_file:
        config_file.write(config)

devices = ['csr1', 'csr2' ,'csr3']

#! /usr/bin/env python

from netmiko import ConnectHandler

devices = ['csr1', 'csr2', 'csr3']

for device in devices:
    print("Connecting to device | {}".format(device))
    net_device = ConnectHandler(host=device, username='ntc', password='ntc123', device_type='cisco_ios')
    print("Saving configuration | {}".format(device))
    net_device.send_command("wr mem")
    print("Backing up configuration | {}".format(device))
    net_device.send_command("term len 0")
    config = net_device.send_command("show run")
    print("Writing config to file | {}\n".format(device))
    with open("/home/ntc/files/scripts/configs/{}.cfg".format(device), "w") as config_file:
        config_file.write(config)
    net_device.disconnect()
    
    ####################################################################################################
    ##################################  LAB 17 Using Python Functions  #################################
    ####################################################################################################

#! /usr/bin/env python

def get_vlans():
    return [1, 5, 10, 20]

vlans = get_vlans()

print(vlans)

ntc@ntc-training:scripts$ python functions.py
[1, 5, 10, 20]
ntc@ntc-training:scripts$

#! /usr/bin/env python

def get_vlans():
    return [1, 5, 10, 20]

vlans = get_vlans()

print(vlans)

def vlan_exists(vlan_id):
    return vlan_id in [1, 5, 10, 20]

print(vlan_exists(10))
print(vlan_exists(12))

def vlan_exists(vlan_id):
    vlans = [1, 5, 10, 20]
    is_vlan_valid = vlan_id in vlans
    return is_vlan_valid

def ez_cisco(hostname, username, password, show_command):
    print(hostname)
    print(username)
    print(password)
    print(show_command)

ez_cisco('csr1', 'ntc', 'ntc123', 'show version')


#! /usr/bin/env python

def get_vlans():
    return [1, 5, 10, 20]

vlans = get_vlans()

print(vlans)

def vlan_exists(vlan_id):
    return vlan_id in [1, 5, 10, 20]

print(vlan_exists(10))
print(vlan_exists(12))

def ez_cisco(hostname, username, password, show_command):
    print(hostname)
    print(username)
    print(password)
    print(show_command)

ez_cisco('csr1', 'ntc', 'ntc123', 'show version')

ntc@ntc-training:scripts$ python functions.py
[1, 5, 10, 20]
True
False
csr1
ntc
ntc123
show version
ntc@ntc-training:scripts$

#! /usr/bin/env python

def ez_cisco(hostname, username, password, show_command):
    print(hostname)
    print(username)
    print(password)
    print(show_command)

ez_cisco('csr1', 'ntc', 'ntc123', 'show version')

#! /usr/bin/env python

from netmiko import ConnectHandler

def ez_cisco(hostname, username, password, show_command):
    platform = "cisco_ios"
    device = ConnectHandler(ip=hostname, username=username, password=password, device_type=platform)

    output = device.send_command(show_command)
    device.disconnect()

    return output

response = ez_cisco('csr1', 'ntc', 'ntc123', 'show version')

print(response)

#! /usr/bin/env python

from netmiko import ConnectHandler

def ez_cisco(hostname, show_command, username='ntc', password='ntc123'):
    platform = "cisco_ios"
    device = ConnectHandler(ip=hostname, username=username, password=password, device_type=platform)

    output = device.send_command(show_command)
    device.disconnect()

    return output

response = ez_cisco('csr1', 'show version')

print(response)

response = ez_cisco('csr1', 'show version')
print(response)

response = ez_cisco('csr2', 'show ip int brief')
print(response)

response = ez_cisco('csr3', 'show run | inc snmp')
print(response)

#! /usr/bin/env python

from netmiko import ConnectHandler

def ez_cisco(hostname, show_command, username='ntc', password='ntc123'):
    platform = "cisco_ios"
    device = ConnectHandler(ip=hostname, username=username, password=password, device_type=platform)

    output = device.send_command(show_command)
    return output

response = ez_cisco('csr1', 'show version')
print(response)

response = ez_cisco('csr2', 'show ip int brief')
print(response)

response = ez_cisco('csr3', 'show run | inc snmp')
print(response)
    
    ####################################################################################################
    ############################  LAB 18 Re-factoring Code with Functions  #############################
    ####################################################################################################

#! /usr/bin/env python

from netmiko import ConnectHandler

devices = ['csr1', 'csr2', 'csr3']

for device in devices:
    print("Connecting to device | {}".format(device))

    net_device = ConnectHandler(host=device, username='ntc', password='ntc123', device_type='cisco_ios')

    print("Saving configuration | {}".format(device))

    net_device.send_command("wr mem")

    print("Backing up configuration | {}".format(device))

    net_device.send_command("term len 0")
    config = net_device.send_command("show run")

    print("Writing config to file | {}\n".format(device))

    with open("/home/ntc/scripts/configs/{}.cfg".format(device), "w") as config_file:
        config_file.write(config)

    net_device.disconnect()

#! /usr/bin/env python

from netmiko import ConnectHandler

def main():
    devices = ['csr1', 'csr2', 'csr3']

    for device in devices:
        print("Connecting to device | {}".format(device))

        net_device = ConnectHandler(host=device, username='ntc', password='ntc123', device_type='cisco_ios')

        print("Saving configuration | {}".format(device))

        net_device.send_command("wr mem")

        print("Backing up configuration | {}".format(device))

        net_device.send_command("term len 0")
        config = net_device.send_command("show run")

        print("Writing config to file | {}\n".format(device))

        with open("/home/ntc/scripts/configs/{}.cfg".format(device), "w") as config_file:
            config_file.write(config)

        net_device.disconnect()

main()

def connect_to_device(hostname):
    print("Connecting to device | {}".format(hostname))
    device = ConnectHandler(host=hostname, username='ntc', password='ntc123', device_type='cisco_ios')

    return device

#! /usr/bin/env python

from netmiko import ConnectHandler

def connect_to_device(hostname):
    print("Connecting to device | {}".format(hostname))
    net_d = ConnectHandler(host=hostname, username='ntc', password='ntc123', device_type='cisco_ios')

    return net_d

def main():
    devices = ['csr1', 'csr2', 'csr3']

    for device in devices:

        net_device = connect_to_device(device)

        print("Saving configuration | {}".format(device))
        net_device.send_command("wr mem")

        print("Backing up configuration | {}".format(device))

        net_device.send_command("term len 0")
        config = net_device.send_command("show run")

        print("Writing config to file | {}\n".format(device))

        with open("/home/ntc/scripts/configs/{}.cfg".format(device), "w") as config_file:
            config_file.write(config)

        net_device.disconnect()

main()

#! /usr/bin/env python

from netmiko import ConnectHandler

def connect_to_device(hostname):
    print("Connecting to device | {}".format(hostname))
    net_d = ConnectHandler(host=hostname, username='ntc', password='ntc123', device_type='cisco_ios')

    return net_d

def save_config(device, hostname):
    print("Saving configuration | {}".format(hostname))
    device.send_command("wr mem")

def backup_config(device, hostname):
    pass

def write_to_file():
    pass

def main():
    devices = ['csr1', 'csr2', 'csr3']

    for device in devices:
        net_device = connect_to_device(device)

        save_config(net_device, device)

        print("Backing up configuration | {}".format(device))
        net_device.send_command("term len 0")
        config = net_device.send_command("show run")

        print("Writing config to file | {}\n".format(device))
        with open("/home/ntc/scripts/configs/{}.cfg".format(device), "w") as config_file:
            config_file.write(config)

        net_device.disconnect()

main()

def backup_config(device, hostname):
    print("Backing up configuration | {}".format(hostname))
    device.send_command("term len 0")
    config = device.send_command("show run")

    return config

def main():
    devices = ['csr1', 'csr2', 'csr3']

    for device in devices:
        net_device = connect_to_device(device)
        save_config(net_device, device)

        config = backup_config(net_device, device)

        print("Writing config to file | {}\n".format(device))
        with open("/home/ntc/scripts/configs/{}.cfg".format(device), "w") as config_file:
            config_file.write(config)

        net_device.disconnect()

def write_to_file(hostname, show_run):
    print("Writing config to file | {}\n".format(hostname))
    with open("/home/ntc/scripts/configs/{}.cfg".format(hostname), "w") as config_file:
        config_file.write(show_run)

#! /usr/bin/env python

from netmiko import ConnectHandler

def connect_to_device(hostname):
    print("Connecting to device | {}".format(hostname))
    net_d = ConnectHandler(host=hostname, username='ntc', password='ntc123', device_type='cisco_ios')

    return net_d

def save_config(device, hostname):
    print("Saving configuration | {}".format(hostname))
    device.send_command("wr mem")

def backup_config(device, hostname):
    print("Backing up configuration | {}".format(hostname))
    device.send_command("term len 0")
    config = device.send_command("show run")

    return config

def write_to_file(hostname, show_run):
    print("Writing config to file | {}\n".format(hostname))
    with open("/home/ntc/scripts/configs/{}.cfg".format(hostname), "w") as config_file:
        config_file.write(show_run)

def main():
    devices = ['csr1', 'csr2', 'csr3']

    for device in devices:
        net_device = connect_to_device(device)

        save_config(net_device, device)

        config = backup_config(net_device, device)

        write_to_file(device, config)

        net_device.disconnect()

main()
    
    ####################################################################################################
    ##################################  LAB 19 Passing in User Input  ##################################
    ####################################################################################################

snmp-server community networktocode RO
snmp-server community public RO
snmp-server community ntcrw RW
snmp-server community supersecret RW
snmp-server location new_york
snmp-server contact jane_smith


from netmiko import ConnectHandler


def connect_to_device(hostname, username, password, device_type):
    message = "Connecting to device"
    print_logger(message, hostname)
    net_d = ConnectHandler(host=hostname, username=username, password=password, device_type=device_type)

    return net_d

def deploy_commands(device, hostname, config_file):
    print("Sending commands from file | {}".format(hostname))
    device.send_config_from_file(config_file)

def print_logger(message, hostname):
    print("{} | {}".format(message, hostname))

def main(device, username, password, device_type):
    config_file = './configs/snmp.cfg'

    net_device = connect_to_device(device, username, password, device_type)

    deploy_commands(net_device, device, config_file)

    print_logger("Disconnecting from device", device)
    net_device.disconnect()

if __name__ == "__main__":
    device = 'csr1'
    username = 'ntc'
    password = 'ntc123'
    device_type = 'cisco_ios'

    main(device, username, password, device_type)

if __name__ == "__main__":
    device = input("Please enter the hostname or IP: ")
    username = input("Please enter the username: ")
    password = input("Please enter the password: ")
    device_type = input("Please enter the device type: ")

    main(device, username, password, device_type)


from getpass import getpass


password = getpass("Please enter the password: ")


import argparse


    device = input("Please enter the hostname or IP: ")
    username = input("Please enter the username: ")
    password = getpass("Please enter the password: ")
    device_type = input("Please enter the device type: ")


    parser = argparse.ArgumentParser(description='Collect device and data'
                                     ' file information to configure a device')
    parser.add_argument('-i', '--ip',
                        help='Enter the IP address or hostname of the device',
                        required=True)
    parser.add_argument('-d', '--device_type', help='Enter the device type',
                        required=True)
    parser.add_argument('-u', '--username', help='Enter the username',
                        required=True)
    parser.add_argument('-p', '--password', help='Enter the password',
                        required=True)

    # parse all args and render
    args = parser.parse_args()

    device = args.ip
    username = args.username
    password = args.password
    device_type = args.device_type


ntc@ntc-training:scripts$ python user-flags.py
usage: flags_user_input.py [-h]  -i IP -d DEVICE_TYPE -u
                             USERNAME -p PASSWORD
flags_user_input.py: error: argument -i/--ip is required


ntc@ntc-training:scripts$ python user-flags.py --help
usage: flags_user_input.py [-h] -i IP -d DEVICE_TYPE -u
                             USERNAME -p PASSWORD
Collect device and data file information to configure a device

optional arguments:
  -h, --help            show this help message and exit
  -i IP, --ip IP        Enter the IP address or hostname of the device
  -d DEVICE_TYPE, --device_type DEVICE_TYPE
                        Enter the device type
  -u USERNAME, --username USERNAME
                        Enter the username
  -p PASSWORD, --password PASSWORD
                        Enter the password



ntc@ntc-training:scripts$ python user-flags.py -i csr1 -d cisco_ios -u ntc -p ntc123
# output omitted


print(sys.argv)



#! /usr/bin/env python

import sys

if __name__ == "__main__":

    print('HERE ARE MY ARGUMENTS: ')
    print(sys.argv)



ntc@ntc-training:scripts$ python basic_args.py
HERE ARE MY ARGUMENTS:
['basic_args.py']


ntc@ntc-training:scripts$ python basic_args.py cisco arista juniper


if __name__ == "__main__":

    print('HERE ARE MY ARGUMENTS: ')

    args = sys.argv

    print(args[1])


ntc@ntc-training:scripts$ python basic_args.py cisco arista juniper


>>> args = ['basic_args.py', 'cisco', 'arista', 'juniper']
>>>
>>> args[1:]
['cisco', 'arista', 'juniper']
>>>
>>>
>>> limited = args[1:]
>>>
>>> if limited:
...   'args were passed in'
...
'args were passed in'
>>>
>>>
>>> args = ['basic_args.py']
>>>
>>> limited = args[1:]
>>>
>>> if limited:
...   'args were passed in'
...
>>>