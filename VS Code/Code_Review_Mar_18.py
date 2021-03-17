# =================================================================================================
# EASY ============================================================================================
# =================================================================================================


# def pling_plang():

#     '''Pling Plang is a function used to return the output  of intergers divisible by 3, 5, and 7'''

#     for i in range(1,101):
#         if i % 3 == 0:
#             print("Pling")
#         elif i % 5 == 0:
#             print("Plang")
#         elif i % 7 == 0:
#             print("Plong")
#         else:
#             print(i)

# pling_plang()



# =================================================================================================
# MEDIUM ==========================================================================================
# =================================================================================================


# # Create the function
# def pling_plang():

    # Define the variable "my_dictionary" as a dictionary with empty lists as placeholders for the values. 
#     my_dictionary = {
#         "Pling": [],
#         "Plang": [],
#         "Plong": [],
#         "No_match": []
#     }

#     # Logic to determine "divisible by". If true, append (i) to the corresponding key in my_dictionary.
#     for i in range(1,101):
#         if i % 3 == 0:
#             my_dictionary["Pling"].append(i)
#         elif i % 5 == 0:
#             my_dictionary["Plang"].append(i)
#         elif i % 7 == 0:
#             my_dictionary["Plong"].append(i)
#         else:
#             my_dictionary["No_match"].append(i)

#     for key in my_dictionary:
#         print()
#         print(key, ":", my_dictionary[key])

# pling_plang()


# =================================================================================================
# HARD ============================================================================================
# =================================================================================================


import requests
import json
import ipaddress 


# Fetch data from URL and define global variables 
url = 'https://raw.githubusercontent.com/JohnFu11er/Code_Challenge_Data/main/network_addresses.json' 
response = requests.request('GET',url,)
ip_data = response.json()


# Function to return if a key exists in a dictionary
def key_exists(obj_dict,key):
    if (key in obj_dict):
        return True
    else:
        return False

# Function to parse data from the GET call into a dictionary object
def parse_data(obj_dict):
    
    # Define the IP dictionary to be used for formatting the parsed data
    ip_dict = {}

    # For loop to iterate through the entire IP list
    for ip in obj_dict: 
        # Define the variable to be used to "split" the IP addresses after the 2nd octet. 
        ip_split = ip.split(".")

        # Define a new variable to return the first two octets into a formatted string
        ip_header = (f'{ip_split[0]}.{ip_split[1]}.0.0')

        if(key_exists(ip_dict,ip_header)):
            ip_dict[ip_header].append(ip)
        else: 
            ip_dict[ip_header] = [ip]
    return ip_dict

# Function to sort IP addresses
def sort_data(ip_dict):
    for x in ip_dict:
        items = sorted(ip_dict[x], key = ipaddress.IPv4Address)
        ip_dict[x].clear()
        ip_dict[x] = items

if(key_exists(ip_data,'network_addresses')):
    #Pass in the dictionary to our parse function.
    results = parse_data(ip_data['network_addresses']) 
    sort_data(results)
    print('===================================')
    print(f'======= Total IP Subnets: {len(results)} =======')
    print('===================================')
    print('=== Total Addresses Per Subnet: ===')
    for ip in results.keys():
        print(f'{ip:15} {":" :^7} {len(results[ip]) :>11}')
    print('===================================')

with open ('Code_Review_Mar_18.json', 'w') as json_data:
    json.dump(results, json_data, indent = 4)