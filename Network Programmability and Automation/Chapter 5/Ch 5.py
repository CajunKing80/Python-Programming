##############################################
#######  Data Formats and Data Models  #######
##############################################

import yaml

with open ('example.yml') as f: 
    result = yaml.load(f)
    print (result)
    type (result)
    print ()    