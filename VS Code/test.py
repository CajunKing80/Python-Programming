# import requests
# from pprint import PrettyPrinter


# pp = PrettyPrinter()
# ip_dictionary = {
#     "Class_A" : [],
#     "Class_B" : [],
#     "Class_C" : []
# }

# # Fetch data from URL:
# url = 'https://raw.githubusercontent.com/JohnFu11er/Code_Challenge_Data/main/network_addresses.json' 

# response = requests.request('GET',url,)
# pp.pprint(response.json())


import requests

# simple function to see if a key exists in a dictionary.
def keyExists(dicObj,key):
    if (key in dicObj):
        return True
    else:
        return False

#Function to parse the data into dictionary object.
def parseData(dicObj):
    #a dictionary object to hold our parsed data.
    netDic = {}
    for ip in dicObj:
        ipSplit = ip.split('.') #Split the IP Address based off the '.' as a delimiter.
       
        ipHeader = f'{ipSplit[0]}.{ipSplit[1]}' #reconstruct the first two octets into a formatted string.
        if(keyExists(netDic,ipHeader)): #if the header exists then append the ip address to that list.
            netDic[ipHeader].append(ip)
        else: #Otherwise we create a new key in the dictionary and add a list to it with this IP.
            netDic[ipHeader] = [ip]
    return netDic


#------------------------------------------------------------------------------------------------------------
#MAIN ENTRY POINT
#------------------------------------------------------------------------------------------------------------

#The URL we will be hitting for the data.
url = 'https://raw.githubusercontent.com/JohnFu11er/Code_Challenge_Data/main/network_addresses.json'

#create request.
req = requests.get(url)

#If the request was successful we can attempt to parse.
#Must look for status code 200 as some endpoints will return a JSON result as error info,
if (req.status_code == 200):
    try:
        ipData = req.json()
        #Check to see if the data is valid by checking to see if the network_addresses key exists in the dictionary.
        if(keyExists(ipData,'network_addresses')):
            #Pass in the dictionary to our parse function.
            results = parseData(ipData['network_addresses']) 
            print(f'Total IP Blocks: {len(results)}')
            print('Total IP addresses in each block:')
            for ip in results.keys():
                print(f'{ip} - {len(results[ip])}')

    except ValueError: # The json function of the request object throws a value error if it cannot parse.
        print('An error occured parsing the JSON:')
else:
    print(f'Error attempting to get data. Error Code {req.status_code}')