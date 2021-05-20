from ansible.module_utils.basic import AnsibleModule

if __name__ == '__main__':
    main()

def main():
    data = {
        "host" : {
            "default" : "localhost", 
            "type" : "str"
        },
        "username" : {
            "default" : "username", 
            "type" : "str"
        },
        "password" : {
            "default" : "password", 
            "type" : "str"
        },
        "url" : {
            "default" : "localhost", 
            "type" : "str"
        }
    }

    module = AnsibleModule(argument_spec = data)

host = module.params.get('host')
username = module.params.get('username')
password = module.params.get('password')
url = 'http://' + host + '/authentication'
module.params.update({"url": url})

module.exit_json(changed=True, meta=module.params)















# import requests
# import pygeoip
# from geolite2 import geolite2
# import socket
# import argparse
# import json

# parser = argparse.ArgumentParser(description='Get IP Geolocation Info')
# parser.add_argument('--hostname', action="store", dest="hostname", required=True)

# given_args= parser.parse_args()
# hostname = given_args.hostname
# ip_address = socket.gethostbyname(hostname)

# print ("IP Address: {0}".format(ip_address))

# reader = geolite2.reader()
# response = reader.get(ip_address)
# print (json.dumps(response,indent=4))
# print (json.dumps(response['continent']['names']['en'],indent=4))
# print (json.dumps(response['country']['names']['en'],indent=4))
# print (json.dumps(response['location']['latitude'],indent=4))
# print (json.dumps(response['location']['longitude'],indent=4))
# print (json.dumps(response['location']['time_zone'],indent=4))

# ipaddr = requests.get('https://api.ipify.org').text
# gip = pygeoip.GeoIP(geolite2)
# res = gip.record_by_addr(ipaddr)

# print (res)

# class IPtoGeo(object):
#     def __init__(self,ip_address):
#         self.ip_address = ip_address
#         self.country = ''
#         self.state = ''
#         self.city = ''
#         self.latitude = ''
#         self.longitude = ''
#         # self._get_location()

# def _get_location(self):
#     json_request = requests.get('https://hackertarget.com/geoip-ip-location-lookup/' % self.ip_address).json()
#     if 'country_name' in json_request:
#         self.country = json_request['country_name']
#     if 'country_code' in json_request:
#         self.country_code = json_request['country_code']
#     if 'city' in json_request:
#         self.city = json_request['city']
#     if 'latitude' in json_request:
#         self.latitude = json_request['latitude']
#     if 'longitude' in json_request:
#         self.longitude = json_request['longitude']

# if __name__ == '__main__':
#     geolocation = IPtoGeo('65.191.205.187')
#     print (geolocation .__dict__)