class DevelopmentScript(Script):

    # Will change an entire tenant
    tenant_to_change = ObjectVar(
        model=Tenant,
        display_field='model'
    )

    # select target device
    target_device = ObjectVar(
        description = "Select the device that you want to change.",
        model=Device,
        display_field='name'
    )


    # Select new device role - this will map to the device type with a dictionary in this script
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

    ### switch type

    ### kg type

    class Meta:
        name = "Development Script"
        description = "Tesing script to change the device type on an existing device."
        commit_default = False

    def run(self, data, commit):
        
        # role / type / name mapping
        type_dict = {
            "MFS Lite" : ["mfs_router_lite", "L"],
            "MFS Medium" : ["mfs_router_med", "M"],
            "MFS Heavy" : ["mfs_router", "H"]
        }

        # fetches device object from netbox and assigns as "old_dev"
        old_dev = Device.objects.get(name=data['target_device'])

        new_device_type = type_dict[str(data['new_role'])][0]

        def main():
            update_device(old_dev)

        def new_router_type(role, item):
            type_dict = {
                "MFS Lite" : ["mfs_router_lite", "L"],
                "MFS Medium" : ["mfs_router_med", "M"],
                "MFS Heavy" : ["mfs_router", "H"]
            }
            return type_dict[role][item]

        def new_name(old_name):
            temp = old_name.split("-")
            temp[2] = new_router_type(str(data['new_role']), 1)
            return "-".join(temp)
        
        def update_device(old_dev):
            ''' Appliees selected changes to the old device '''
            old_dev.device_role= data['new_role']
            old_dev.device_type= DeviceType.objects.get(model=new_router_type(str(data['new_role']), 0))
            old_dev.name= f"{new_name(old_dev.name)}"
            old_dev.save()
            
        # get device interfaces
        # loop through interfaces and check if one of them has the 

            # my_ips = IPAddress.objects.prefetch_related().filter(tenant__name='KL001')
            

            # output = []
            # for ip in my_ips:
            #     if ip.assigned_object != None:
            #         if ip.assigned_object.device.name == current_device and ip.assigned_object.name == "Loopback0":
            #             output.append(ip.assigned_object.name)
            # return output


        main()


        template_interfaces = [i.name for i in InterfaceTemplate.objects.select_related().filter(device_type__model=new_device_type)]


        # builds a dictionary of interfaces based on the new device type
        virtual_interface_mapping = {}
        virtual_interface_prefixes = ["bdi", "bvi", "vla"]
        for interface in template_interfaces:
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
        old_dev_interfaces = Interface.objects.filter(device__name=old_dev.name)
        for item in old_dev_interfaces:
            if item.name[:3].lower() in virtual_interface_prefixes:
                if item.name[-1:] in virtual_interface_mapping.keys():
                    item.name = virtual_interface_mapping[item.name[-1:]]
                elif item.name[-2:] in virtual_interface_mapping.keys():
                    item.name = virtual_interface_mapping[item.name[-2:]]
                elif item.name[-3:] in virtual_interface_mapping.keys():
                    item.name = virtual_interface_mapping[item.name[-3:]]
            item.save()

        def cleanup_interfaces():
            for interface in Interface.objects.filter(device__name=old_dev):
                if interface.name not in template_interfaces:
                    interface.delete()
        
        def create_new_interfaces(interfaces):
            output = f"The following interfaces were created on {old_dev}:\n\n"
            
            for interface in interfaces:
                if interface.name not in [i.name for i in Interface.objects.filter(device__name=old_dev)]:
                    new_interface = Interface(
                        name = interface.name,
                        device = old_dev
                    )
                    new_interface.save()
                    output += f"Interface {interface.name}\n"
            
            if new_device_type == "mfs_router":
                new_ip = IPAddress(
                    address= "10.211.211.1/29",
                    tenant= Tenant.objects.get(name=data['tenant_to_change']),
                    assigned_object= Interface.objects.get(name='GigabitEthernet1',device__name=old_dev)
                )
                new_ip.save()

            # Add IP Address to BDI85 if none is assigned
            if "BDI85" in template_interfaces:
                kl_num = old_dev.tenant.name[2:5]
                new_ip = IPAddress(
                    address= f"10.100.98.{kl_num}/23",
                    description="MANET",
                    tenant= Tenant.objects.get(name=data['tenant_to_change']),
                    assigned_object= Interface.objects.get(name='BDI85',device__name=old_dev)
                )
                new_ip.save()

            # Add IP Address to VLAN85 if none is assigned
            if "VLAN85" in template_interfaces:
                kl_num = old_dev.tenant.name[2:5]
                new_ip = IPAddress(
                    address= f"10.100.98.{kl_num}/23",
                    tenant= Tenant.objects.get(name=data['tenant_to_change']),
                    assigned_object= Interface.objects.get(name='VLAN85',device__name=old_dev)
                )
                new_ip.save()
                


            return output

        cleanup_interfaces()
        
        # return create_new_interfaces(["test1", "test2", "test3"])
        return create_new_interfaces(InterfaceTemplate.objects.select_related().filter(device_type__model=new_device_type))
        my_test = InterfaceTemplate.objects.select_related().filter(device_type__model=new_device_type)
        my_test2 = ["FastEthernet0/0", "FastEthernet0/1"]
        # return my_test
        return create_new_interfaces(my_test)