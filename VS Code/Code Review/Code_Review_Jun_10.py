####################################################################################################
############################################### EASY ###############################################
####################################################################################################

# Using cURL or Postman or Python, retrieve the API authentication token from the Cisco DNA Center Always On Sandbox

import requests
from requests.auth import HTTPBasicAuth
# from dnac_config import DNAC, DNAC_PORT, DNAC_USER, DNAC_PASSWORD

def get_auth_token():
    
    url = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'       # Endpoint URL
    resp = requests.post(url, auth=HTTPBasicAuth(username='devnetuser', password='Cisco123!'))  # Make the POST Request
    token = resp.json()['Token']    # Retrieve the Token from the returned JSON
    print("Token Retrieved: {}".format(token))  # Print out the Token
    return token    # Create a return statement to send the token back for later use 

print(__name__)
if __name__ == "__main__":
    get_auth_token()