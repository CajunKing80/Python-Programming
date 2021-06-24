############################################################################################################################################
################################################################### EASY ###################################################################
############################################################################################################################################


def get_name():
    print(f"\n{'='*100}  EASY  {'='*100}\n")
    print("The name of my current program is set to: {}" .format(__name__))
    print()
    print('='*208)

if __name__ == '__main__':
    get_name()


############################################################################################################################################
################################################################## MEDIUM ##################################################################
############################################################################################################################################


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


############################################################################################################################################
################################################################### HARD ###################################################################
############################################################################################################################################


import requests
from dnacentersdk import api

headers = {
    'X-Auth-Token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MDJjMGUyODE0NzEwYTIyZDFmN2UxNzIiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjYwMmJlYmU1MTQ3MTBhMDBjOThmYTQwOSJdLCJ0ZW5hbnRJZCI6IjYwMmJlYmU1MTQ3MTBhMDBjOThmYTQwMiIsImV4cCI6MTYyNDQ5NDEyNCwiaWF0IjoxNjI0NDkwNTI0LCJqdGkiOiI1ZDBlMmQ1Mi02NmRlLTRmZTUtODJlMi02ZmE5YzBkOGVhNDQiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.AHtTpUJ7IIeX-_4131QTm9xBf3kYlNsNHlaIxhVZrFtETieWE4IStqNLulNiRCSkQrkn0nqp7h1SGvWzxLQTUZyNCLfM0ssqMyWbJyW-MnYdVh-rgcuefOp3OoOuBAwua5KwodduTLLsD1uqej41kcbkRqgeljmYfbPUShiYPa39qPB2BtUtpNG8QiWtewqx9Ncj2lbqhhGudeb93F8HlMTYQn3wJ6DCx85SzVTG0mZRfQzPomJKv6ViWPeBrzH8W6YLDArgH81mog60q_bxclgL0-EJx-j00a7ohPXA479dPvmIk0BDr6qjxJaQMTHUBgLFWq_650G209IFAAsACA',
}

response = requests.get('https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device', headers=headers)


DNAC = api.DNACenterAPI(username="devnetuser", 
            password="Cisco123!", 
            base_url="https://sandboxdnac.cisco.com")

print(f"\n{'='*100}  HARD  {'='*100}\n")

DEVICES = DNAC.devices.get_device_list()

print('-'*95)
print('{0:25s}{1:1}{2:50s}{3:1}{4:15s}'.format("Device Name", "|", "Device Type", "|", "Last Updated"))
print('-'*95)

for DEVICE in DEVICES.response: 
    # print ('{0:25s}{1:1}{2:50s}{3:1}{4:15s}'.format(DEVICE.hostname, "|", DEVICE.type, "|", DEVICE.lastUpdated))
    print (DEVICE.hostname)
    print (DEVICE.type)
    print (DEVICE.lastUpdated)

print('-'*95)
print()
print('='*208)