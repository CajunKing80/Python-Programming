############################################################################################################################################
################################################################### EASY ###################################################################
############################################################################################################################################

# Write a simple Python program to return the name variable within your main program. 

def get_name():
    print("The name of my current program is set to: {}" .format(__name__))

if __name__ == '__main__':
    get_name()

# print(f"\n{'='*100}  EASY  {'='*100}\n")
# print("The name of my current program is set to: {}" .format(__name__))
# print()
# print('='*208)

############################################################################################################################################
################################################################## MEDIUM ##################################################################
############################################################################################################################################

# Write a Python program to retrieve the API authentication token from the Cisco DNA Center Always On Sandbox
# Cisco DevNet Sandbox Topology: https://devnetsandbox.cisco.com/RM/Diagram/Index/c3c949dc-30af-498b-9d77-4f1c07d835f9?diagramType=Topology
# Cisco DevNet Sandbox for DNAC: https://sandboxdnac.cisco.com
# username: devnetuser
# password: Cisco123!
# Per the documentation, this token is required to set as the X-Auth-Token HTTP Header for all API calls into the DNA Center

import requests
from requests.auth import HTTPBasicAuth
import json

def get_auth_token():
    
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    resp = requests.post(url, auth=HTTPBasicAuth(username='devnetuser', password='Cisco123!'))
    token = resp.json()['Token']
    print(f"\n{'='*100} MEDIUM {'='*100}\n")
    print("DNAC Token: {}".format(token))
    print()
    print('='*209)
    print(resp)
    return token

if __name__ == "__main__":
    get_auth_token()

# {"Token":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MDJjMGUyODE0NzEwYTIyZDFmN2UxNzIiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjYwMmJlYmU1MTQ3MTBhMDBjOThmYTQwOSJdLCJ0ZW5hbnRJZCI6IjYwMmJlYmU1MTQ3MTBhMDBjOThmYTQwMiIsImV4cCI6MTYyMjg0MzU5MCwiaWF0IjoxNjIyODM5OTkwLCJqdGkiOiIyNDExZWFmYy01ODQ5LTQ5YWUtODIxYi05YzIyM2E4YWRjMDgiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.U6d33UroOiIRH4LQOBw7rYTitFvsx0TAvk0ubAnSWSsfjY9p7qDTqnKex5Wo_SjAym7-9_dqvucofWibA8qnJFxqHqGSU9SFOdcvBB-21uT5RKnfG9mQXEXeScHEfh13quEl6SjwhUFgiG9zG8HQokrwDcinom280Ty_2B1pxuVS6TGeBFptJ2qHCox-1nwJjIEqMKMmqPpmbkoYZIcFhYOxWm4s7O23p2qetLeMdrMguIk-xbtdz1O3dFMU4cP_MLcGffu0FSPKN35Xdt_lADAEhZym3fkpMeazfJBnPVzOHszoTVFNonl9Czpl_xX18CBD9GbhFatlLZCsqbht7w"}

############################################################################################################################################
################################################################### HARD ###################################################################
############################################################################################################################################

# Using the API token retrieved from the medium challenge, return teh list of network devices by name type and last update DTG

# import requests

# headers = {
#     'X-Auth-Token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MDJjMGUyODE0NzEwYTIyZDFmN2UxNzIiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjYwMmJlYmU1MTQ3MTBhMDBjOThmYTQwOSJdLCJ0ZW5hbnRJZCI6IjYwMmJlYmU1MTQ3MTBhMDBjOThmYTQwMiIsImV4cCI6MTYyMjg0MzU5MCwiaWF0IjoxNjIyODM5OTkwLCJqdGkiOiIyNDExZWFmYy01ODQ5LTQ5YWUtODIxYi05YzIyM2E4YWRjMDgiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.U6d33UroOiIRH4LQOBw7rYTitFvsx0TAvk0ubAnSWSsfjY9p7qDTqnKex5Wo_SjAym7-9_dqvucofWibA8qnJFxqHqGSU9SFOdcvBB-21uT5RKnfG9mQXEXeScHEfh13quEl6SjwhUFgiG9zG8HQokrwDcinom280Ty_2B1pxuVS6TGeBFptJ2qHCox-1nwJjIEqMKMmqPpmbkoYZIcFhYOxWm4s7O23p2qetLeMdrMguIk-xbtdz1O3dFMU4cP_MLcGffu0FSPKN35Xdt_lADAEhZym3fkpMeazfJBnPVzOHszoTVFNonl9Czpl_xX18CBD9GbhFatlLZCsqbht7w',
# }

# response = requests.get('https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device', headers=headers)

# from dnacentersdk import api

# DNAC = api.DNACenterAPI(username="devnetuser", 
#             password="Cisco123!", 
#             base_url="https://sandboxdnac.cisco.com")

# print(f"\n{'='*100}  HARD  {'='*100}\n")

# DEVICES = DNAC.devices.get_device_list()

# print('-'*95)
# print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format("Device Name", "|", "Device Type", "|", "Last Updated"))
# print('-'*95)

# for DEVICE in DEVICES.response: 
#     print ('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format(DEVICE.hostname, "|", DEVICE.type, "|", DEVICE.lastUpdated))

# print('-'*95)
# print()
# print('='*208)