from napalm import get_network_driver
import json

driver = get_network_driver("ios")

optional_args = {"secret" : "cisco"} #cisco enable password
ios=driver(
"192.168.0.152",
"ansible",
"ansible", 
optional_args=optional_args
)

ios.open()
# Start Code Here

ios.load_merge_candidate("acl.txt")

diff = ios.compare_config()




# End Code Here
ios.close()