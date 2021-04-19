#############################################################
##### Application Policy Infrastructure Controller APIC #####
#############################################################

#! /usr/bin/env python

import sys
import acitoolkit.acitoolkit as aci

APIC_URL = 'https://sandboxapicdc.cisco.com'
USERNAME = 'admin'
PASSWORD = 'ciscopsdt'

# Login to APIC

SESSION = aci.Session(APIC_URL, USERNAME, PASSWORD)
RESP = SESSION.login()
if not RESP.ok:
    print('Could Not Login to APIC')
    sys.exit()

ENDPOINTS = aci.Endpoint.get(SESSION)
print('{0:19s}{1:14s}{2:10s}{3:8s}{4:17s}{5:10s}'.format(
    "MAC ADDRESS", 
    "IP ADDRESS", 
    "ENDCAP", 
    "TENANT", 
    "APP PROFILE", 
    "EPG"))
print('-' * 80)

for EP in ENDPOINTS:
    epg = EP.get_parent()
    app_profile = epg.get_parent()
    tenant = app_profile.get_parent()
    print('{0:19s}{1:14s}{2:10s}{3:8s}{4:17s}{5:10s}'.format(
        EP.mac,
        EP.ip, 
        EP.encap, 
        tenant.name, 
        app_profile.name, 
        epg.name))

#############################################################
####### Cisco Unified Computing System (UCS) Manager ########
#############################################################

