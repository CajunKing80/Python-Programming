
############################################################################################################################################
################################################################### EASY ###################################################################
############################################################################################################################################


import requests
from requests.auth import HTTPBasicAuth
from dnacentersdk import api


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


def get_auth_token():
    
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    resp = requests.post(url, auth=HTTPBasicAuth(username='devnetuser', password='Cisco123!'))
    token = resp.json()['Token']
    print(f"\n{'='*100} MEDIUM {'='*100}\n")
    print("DNAC Token: {}".format(token))
    print()
    print('='*209)
    return token

if __name__ == "__main__":
    get_auth_token()


############################################################################################################################################
################################################################### HARD ###################################################################
############################################################################################################################################



def get_network_devices():

    headers = {
        'X-Auth-Token': '{get_auth_token}'
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

if __name__ == '__main__':
    get_network_devices()