#! /usr/bin/env python
from dnacentersdk import api

DNAC = api.DNACenterAPI(username="devnetuser", 
            password="Cisco123!", 
            base_url="https://sandboxdnac.cisco.com")

DEVICES = DNAC.devices.get_device_list()

print ('{0:25s}{1:1}{2:5s}{3:1}{4:15s}'.format("Device Name", "|", "Device Type", "|", "Up Time"))

print ('-'*95)

for DEVICE in DEVICES.response: 
    print ('{0:25s}{1:1}{2:5s}{3:1}{4:15s}'.format(DEVICE.hostname, "|", DEVICE.type, "|", DEVICE.upTime))

print ('-'*95)

CLIENTS = DNAC.clients.get_overall_client_health(timestamp="timestamp")

print ('{0:25s}{1:1}{2:5s}{3:1}{4:15s}'.format("Client Category", "|", "Number of Clients", "|", "Client Score"))

print ('-'*95)

for CLIENT in CLIENTS.response: 
    for score in CLIENT.scoreDetail:
        print ('{0:25s}{1:1}{2:<45d}{3:1}{4:<15d}'.format(score.scoreCategory.value, "|", score.clientCount, "|", score.scoreValue))

print ('-'*95)