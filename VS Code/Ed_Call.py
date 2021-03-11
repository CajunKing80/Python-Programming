#!/usr/bin/env python3



from extras.scripts import *

from dcim.choices import DeviceStatusChoices, SiteStatusChoices

from dcim.models import Device, DeviceType, DeviceRole, Platform, Rack, Site, InterfaceTemplate, Interface

from ipam.models import IPAddress

from tenancy.models import Tenant

import tenancy.models

import ipaddress

import json

from django.db import models



# Version 1.0

# Created: 1/11/2021

# Developer: John Fuller



class Tenant_Testing(Script):



    # Generates a list of KL#s so that the script will on change KL's

    all_KL = [i.name for i in Tenant.objects.filter(name__icontains= 'KL')]



    tenant_to_change = ObjectVar(

        model=Tenant,

        display_field='name',

        query_params={

            'name': all_KL

        }

    )



    new_role = ObjectVar(

        description = "Select the new role for the device selected.",

        model= DeviceRole,

        display_field='model',

        query_params={

            'name':[

                'MFS Lite',

                'MFS Medium',

                'MFS Heavy'

            ]

        }

    )



    crypto_device = ObjectVar(

        description = "Select the new role for the device selected.",

        model= DeviceType,

        display_field='model',

        query_params={

            'model':[

                'kg_250x',

                'kg_250xs',

            ] 

        }

    )



    switch_type = ObjectVar(

        description = "Select the type of switch:  mfs_switch = 14 port, mfs_switch_v2 = 26 port",

        model= DeviceType,

        display_field='model',

        query_params={

            'model':[

                'mfs_switch',

                'mfs_switch_v2',

            ] 

        }

    )



    class Meta:

        name = "Device Change Script"

        description = "Tesing script that will allow users to easily change a device's device type."

        commit_default = False



    def run(self, data, commit):

        

        # role / type / name mapping

        type_dict = {

            "MFS Lite" : ["mfs_router_lite", "L"],

            "MFS Medium" : ["mfs_router_med", "M"],

            "MFS Heavy" : ["mfs_router", "H"]

        }



        # Redefine input selections

        tenant = data['tenant_to_change']

        new_role = data['new_role']

        new_device_type = type_dict[str(new_role)][0]

        kg_type = data['crypto_device']

        switch_type = data['switch_type']



        # Get list of devices, routers, switches, and KGs in selected tenant

        # Only gets devices with a "B" in their names so it only processes Black devices

        tenant_devices = Device.objects.filter(tenant=tenant)

        tenant_routers = [i for i in tenant_devices if "router" in i.device_type.model and "B" in i.name]

        tenant_switches = [i for i in tenant_devices if "switch" in i.device_type.model and "B" in i.name]

        tenant_kgs = [i for i in tenant_devices if "kg" in i.device_type.model]



        

        def main():

            update_routers()

            update_switches()

            update_kgs()




        def new_name(old_name):

            ''' Returns new device name based on new device type '''

            temp = old_name.split("-")

            temp[2] = type_dict[str(new_role)][1]

            return "-".join(temp)




        def update_routers():

            ''' Appliees selected changes to the routers '''

            router_template_interfaces = [i for i in InterfaceTemplate.objects.filter(device_type__model=new_device_type)]

            router_template_interface_names = [i.name for i in router_template_interfaces]

            for router in tenant_routers:

                # update name

                router.name= f"{new_name(router.name)}"



                # update device role

                router.device_role= data['new_role']

                

                # update device type

                router.device_type= DeviceType.objects.get(model=new_device_type)

                

                # update interfaces

                interface_configuration(router, router_template_interface_names)

                cleanup_interfaces(router, router_template_interface_names)

                create_new_interfaces(router, router_template_interfaces)

                

                # commit changes

                router.save()



        def update_switches():

            ''' Appliees selected changes to the switches '''

            switch_template_interfaces = [i for i in InterfaceTemplate.objects.filter(device_type__model=switch_type)]

            switch_template_interface_names = [i.name for i in switch_template_interfaces]

            

            for switch in tenant_switches:

                # update name

                switch.name = f"{new_name(switch.name)}"



                # update device type

                switch.device_type = switch_type



                # update interfaces

                # interface_configuration(switch, switch_template_interface_names)

                # cleanup_interfaces(switch, switch_template_interface_names)

                # create_new_interfaces(switch, switch_template_interfaces)

            

                # commit changes

                switch.save()




        def update_kgs():

            ''' Applies selected changes to the KGs '''

            for kg in tenant_kgs:

                # update the device role

                kg.device_role = new_role

            

                # update the device type

                kg.device_type = kg_type



                # commit changes

                kg.save()




        def interface_configuration(_device, _template_interface_names):

            ''' Maps interfaces from old device type to interfaces of new device type '''

            # builds a dictionary of interfaces based on the new device type

            virtual_interface_mapping = {}

            virtual_interface_prefixes = ["bdi", "bvi", "vla"]

            for interface in _template_interface_names:

                if interface[:3].lower() in virtual_interface_prefixes:

                    if interface[-1:] == "1":

                        virtual_interface_mapping["1"] = interface

                    if interface[-2:] == "10":

                        virtual_interface_mapping["10"] = interface

                    if interface[-2:] == "20":

                        virtual_interface_mapping["20"] = interface

                    if interface[-2:] == "25":

                        virtual_interface_mapping["25"] = interface

                    if interface[-2:] == "35":

                        virtual_interface_mapping["35"] = interface

                    if interface[-2:] == "36":

                        virtual_interface_mapping["36"] = interface

                    if interface[-2:] == "60":

                        virtual_interface_mapping["60"] = interface

                    if interface[-2:] == "85":

                        virtual_interface_mapping["85"] = interface

                    if interface[-2:] == "90":

                        virtual_interface_mapping["90"] = interface

                    if interface[-3:] == "100":

                        virtual_interface_mapping["100"] = interface

                    if interface[-3:] == "200":

                        virtual_interface_mapping["200"] = interface

                    if interface[-3:] == "240":

                        virtual_interface_mapping["240"] = interface



            # progresses through interfaces in old device and looks up new name from interface mapping table

            _device_interfaces = Interface.objects.filter(device=_device)

            for item in _device_interfaces:

                if item.name[:3].lower() in virtual_interface_prefixes:

                    if item.name[-1:] in virtual_interface_mapping.keys():

                        item.name = virtual_interface_mapping[item.name[-1:]]

                    elif item.name[-2:] in virtual_interface_mapping.keys():

                        item.name = virtual_interface_mapping[item.name[-2:]]

                    elif item.name[-3:] in virtual_interface_mapping.keys():

                        item.name = virtual_interface_mapping[item.name[-3:]]

                item.save()




        def cleanup_interfaces(_device, _template_interface_names):

            ''' Deletes interfaces that are not in the new device type template '''

            for interface in Interface.objects.filter(device=_device):

                if interface.name not in _template_interface_names:

                    interface.delete()

        



        def create_new_interfaces(_device, _template_interface_objects):

            ''' Creates interfaces that are in the new device type interface template, but do not already exist '''

            for interface in _template_interface_objects:

                if interface.name not in [i.name for i in Interface.objects.filter(device=_device)]:

                    new_interface = Interface(

                        name = interface.name,

                        device = _device,

                        type = interface.type,

                        description = interface.description

                    )

                    new_interface.save()

            

            # Test for an IP assigned to the GigabitEthernet1 port

            is_10_assigned = [ i for i in IPAddress.objects.all() if i.assigned_object != None and i.assigned_object.device == _device and str(i.address) == "10.211.211.1/29"]

            if not is_10_assigned:



                # Add IP Address to the GigabitEthernet1 port

                if new_device_type == "mfs_router":

                    new_ip = IPAddress(

                        address= "10.211.211.1/29",

                        tenant= Tenant.objects.get(name=data['tenant_to_change']),

                        assigned_object= Interface.objects.get(name='GigabitEthernet1',device=_device)

                    )

                    new_ip.save()



            # Test for an IP assigned to the #85 interface of the device

            is_85_assigned = [i for i in IPAddress.objects.all() if i.assigned_object != None and i.assigned_object.device == _device and i.description == "MANET"]

            if not is_85_assigned:

            

                # Add IP Address to BDI85 if none is assigned

                if "BDI85" in _template_interfaces:

                    kl_num = _device.tenant.name[2:5]

                    new_ip = IPAddress(

                        address= f"10.100.98.{kl_num}/23",

                        description= "MANET",

                        assigned_object= Interface.objects.get(name='BDI85',device=_device)

                    )

                    new_ip.save()



                # Add IP Address to VLAN85 if none is assigned

                if "VLAN85" in _template_interfaces:

                    kl_num = _device.tenant.name[2:5]

                    new_ip = IPAddress(

                        address= f"10.100.98.{kl_num}/23",

                        description= "MANET",

                        assigned_object= Interface.objects.get(name='VLAN85',device=_device)

                    )

                    new_ip.save()




        main()