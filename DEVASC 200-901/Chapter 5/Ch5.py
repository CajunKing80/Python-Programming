# ===========================================================================================================================================================================================================================================
# ===========================================================================================================================================================================================================================================

# FILE INPUT & OUTPUT
# file:open() file:close()

# JSON

import json #import the standard library JSON
with open("Ch5.json") as data: #using the open() function, open the JSON file and map it to a Python object (data)
    json_data = data.read()

json_dict = json.loads(json_data) #converted the JSON file into a Python dict with the json_dict variable name
print (json_dict)
json_dict ["interface"]["description"] = "Backup Link" #with json_dict now Python, modifications to the file can be made in Python
print (json_dict)

with open("json_sample.json", "w") as fh:
    json.dump(json_dict, fh, indent = 4) #load the json file back to a file using the dump() function\

with open("json_sample.json") as data: #print the output converted back to JSON format
    json_data = data.read()
    print (json_data)

# XML

# import xmltodict

# with open("Ch5.xml") as data:
#     xml_example = data.read()

# xml_dict = xmltodict.parse(xml_example)

# print (xml_dict)

# YAML

# import yaml

# with open('Ch5.yaml') as data: 
#     yaml_sample = data.read()

# yaml_dict = yaml.load(yaml_sample, Loader=yaml.FullLoader)
# type (yaml_dict)
# print (yaml_dict)
# yaml_dict ["interface"]["name"] = "GigabitEthernet1"
# print (yaml.dump(yaml_dict, default_flow_style=False))
# with open("yaml_sample.yaml", "w") as data: 
#     data.write(yaml.dump(yaml_dict, default_flow_style=False))

# Error Handling

# x = 0
# while True: 

#     try:
#         filename = input('Which file would you like to open? ')
#         with open(filename, "r") as fh:
#             file_data = fh.read()
#     except FileNotFoundError:
#         print (f"Sorry, {filename} doesn't exist. Please try again.")
#     else: 
#         print (file_data)
#         x = 0
#         break
#     finally:
#         x += 1
#         if x == 3:
#             print ("Wrong filename 3 times. \nCheck name and rerun.")
#             break

# Test Driven Development

