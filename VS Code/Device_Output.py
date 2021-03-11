class DeviceOutput(Script):

    # Will change an entire tenant
    tenant_to_change = ObjectVar(
        model=Tenant,
        display_field='model'
    )

    class Meta:
        name = "Device Output"
        description = "Tesing script to change the device type on an existing device."
        commit_default = False

    def run(self, data, commit):
        
        #Output all devices in the KL# to the output tab of the script
        device_list = Device.objects.filter(tenant=data['tenant_to_change'])
        output = []
        for dev in device_list: 
            output.append(dev.name)
        return output