    
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

    