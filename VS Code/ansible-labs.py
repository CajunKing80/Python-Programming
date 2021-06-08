##################################################################################################################################
##################################################################################################################################
##################################  SECTION 01 - Network Automation Fundamentals with Ansible  ###################################
##################################################################################################################################
##################################################################################################################################


    ####################################################################################################
    #######################  LAB 1 Deploying Basic Configurations with Ansible  ########################
    ####################################################################################################

ntc@ntc-training:ntc$ mkdir ansible
ntc@ntc-training:ntc$ 
ntc@ntc-training:ntc$ cd ansible
ntc@ntc-training:ansible$

ntc@ntc-training:ansible$ touch inventory
ntc@ntc-training:ansible$ 

# contents into inventory.txt
[iosxe]
csr1 ansible_network_os=ios
csr2 ansible_network_os=ios
csr3 ansible_network_os=ios

[vmx]
vmx1 ansible_network_os=junos
vmx2 ansible_network_os=junos
vmx3 ansible_network_os=junos

# contents into snmp-config-01.yml playbook
---

  - name: PLAY 1 - DEPLOYING SNMP CONFIGURATIONS ON IOS
    hosts: iosxe
    connection: network_cli
    gather_facts: no

    tasks:

      - name: TASK 1 in PLAY 1 - ENSURE SNMP COMMANDS EXIST ON IOS DEVICES
        ios_config:
          commands:
            - snmp-server community ntc-course RO
            - snmp-server location NYC_HQ
            - snmp-server contact JOHN_SMITH

# append contents into snmp-config-01.yml playbook
  - name: PLAY 2 - DEPLOYING SNMP CONFIGURATIONS ON JUNOS
    hosts: vmx
    connection: netconf
    gather_facts: no

    tasks:

      - name: TASK 1 in PLAY 2 - ENSURE SNMP COMMANDS EXIST ON JUNOS DEVICES
        junos_config:
          lines:
            - set snmp community public authorization read-only
            - set snmp location NYC_HQ
            - set snmp contact JOHN_SMITH

# contents into inventory file
[all:vars]
ansible_user=ntc
ansible_ssh_pass=ntc123

ntc@ntc-training:ansible$ ansible-playbook -i inventory snmp-config-01.yml
    
    ####################################################################################################
    ##############################  LAB 2 Deploying Configs From a File  ###############################
    ####################################################################################################

ntc@ntc-training:ansible$ mkdir configs
ntc@ntc-training:ansible$ cd configs
ntc@ntc-training:configs$

ntc@ntc-training:configs$ touch junos-snmp.cfg
ntc@ntc-training:configs$ touch ios-snmp.cfg
ntc@ntc-training:configs$

# ios-snmp.cfg
snmp-server community ntc-course RO
snmp-server location NYC_HQ        
snmp-server contact JOHN_SMITH     

# junos-snmp.cfg
set snmp location NYC_HQ
set snmp contact JOHN_SMITH
set snmp community public authorization read-only

ntc@ntc-training:ansible$ touch snmp-config-02.yml
ntc@ntc-training:ansible$


---

  - name: PLAY 1 - DEPLOYING SNMP CONFIGURATIONS ON IOS
    hosts: iosxe
    connection: network_cli
    gather_facts: no

    tasks:

      - name: TASK 1 in PLAY 1 - ENSURE SNMP COMMANDS EXIST ON IOS DEVICES
        ios_config:
          src: ./configs/ios-snmp.cfg

  - name: PLAY 2 - DEPLOYING SNMP CONFIGURATIONS ON JUNOS
    hosts: vmx
    connection: netconf
    gather_facts: no

    tasks:

      - name: TASK 1 in PLAY 2 - ENSURE SNMP COMMANDS EXIST ON JUNOS DEVICES
        junos_config:
          src: ./configs/junos-snmp.cfg
    
    ####################################################################################################
    ##########################  LAB 3 Deploying Configs Using a Multi-Vendor  ##########################
    ####################################################################################################

ntc@ntc-training:ansible$ touch snmp-config-03.yml
ntc@ntc-training:ansible$

# snmp-config-03.yml

---

    - name: PLAY 1 - DEPLOYING SNMP CONFIGURATIONS ON IOS 
      hosts: iosxe
      connection: network_cli
      gather_facts: no

      tasks:

        - name: TASK 1 in PLAY 1 - ENSURE SNMP COMMANDS EXIST ON IOS DEVICES
          cli_config:
            config: | 
               snmp-server community ntc-team RO
               snmp-server location FL_HQ        
               snmp-server contact JAMES_CHARLES

# Edit and add play

---

    - name: PLAY 1 - DEPLOYING SNMP CONFIGURATIONS ON IOS 
      hosts: iosxe
      connection: network_cli
      gather_facts: no

      tasks:

        - name: TASK 1 in PLAY 1 - ENSURE SNMP COMMANDS EXIST ON IOS DEVICES
          cli_config:
            config: | 
              snmp-server community ntc-team RO
              snmp-server location FL_HQ        
              snmp-server contact JAMES_CHARLES

    - name: PLAY 2 - DEPLOYING SNMP CONFIGURATIONS ON JUNOS 
      hosts: vmx
      connection: network_cli
      gather_facts: no
         
      tasks:
         
        - name: TASK 1 in PLAY 2 - ENSURE SNMP COMMANDS EXIST ON VMX DEVICES
          cli_config:
            config: |
               set snmp location FL_HQ
               set snmp contact JAMES_CHARLES
               set snmp community public authorization read-only

# Edit and add play

---

    - name: PLAY 1 - DEPLOYING SNMP CONFIGURATIONS ON IOS 
      hosts: iosxe
      connection: network_cli
      gather_facts: no

      tasks:

        - name: TASK 1 in PLAY 1 - ENSURE SNMP COMMANDS EXIST ON IOS DEVICES
          cli_config:
            config: | 
              snmp-server community ntc-team RO
              snmp-server location FL_HQ        
              snmp-server contact JAMES_CHARLES

    - name: PLAY 2 - DEPLOYING SNMP CONFIGURATIONS ON JUNOS 
      hosts: vmx
      connection: network_cli
      gather_facts: no
         
      tasks:
         
        - name: TASK 1 in PLAY 2 - ENSURE SNMP COMMANDS EXIST ON VMX DEVICES
          cli_config:
            config: |
               set snmp location FL_HQ
               set snmp contact JAMES_CHARLES
               set snmp community public authorization read-only
               
    - name: PLAY 3 - DEPLOYING SNMP CONFIGURATIONS ON IOS USING A VARIABLE
      hosts: iosxe
      connection: network_cli
      gather_facts: no
                
      vars:
        ios_commands: | 
             snmp-server community ntc-team RO
             snmp-server location FL_HQ        
             snmp-server contact JAMES_CHARLES

      tasks:
    
          - name: TASK 1 in PLAY 3 - ENSURE SNMP COMMANDS EXIST ON IOS DEVICES
            cli_config:
              config: "{{ ios_commands }}"
              
    - name: PLAY 4 - DEPLOYING SNMP CONFIGURATIONS ON JUNOS USING A VARIABLE
      hosts: vmx
      connection: network_cli
      gather_facts: no
                
      vars:
        junos_commands: |
             set snmp location FL_HQ
             set snmp contact JAMES_CHARLES
             set snmp community public authorization read-only
        
      tasks:
            
        - name: TASK 1 in PLAY 4 - ENSURE SNMP COMMANDS EXIST ON VMX DEVICES
          cli_config:
            config: "{{ junos_commands }}"

# Edit and add play

---

    - name: PLAY 1 - DEPLOYING SNMP CONFIGURATIONS ON IOS 
      hosts: iosxe
      connection: network_cli
      gather_facts: no

      tasks:

        - name: TASK 1 in PLAY 1 - ENSURE SNMP COMMANDS EXIST ON IOS DEVICES
          cli_config:
            config: | 
              snmp-server community ntc-team RO
              snmp-server location FL_HQ        
              snmp-server contact JAMES_CHARLES

    - name: PLAY 2 - DEPLOYING SNMP CONFIGURATIONS ON JUNOS 
      hosts: vmx
      connection: network_cli
      gather_facts: no
         
      tasks:
         
        - name: TASK 1 in PLAY 2 - ENSURE SNMP COMMANDS EXIST ON VMX DEVICES
          cli_config:
            config: |
               set snmp location FL_HQ
               set snmp contact JAMES_CHARLES
               set snmp community public authorization read-only
               
    - name: PLAY 3 - DEPLOYING SNMP CONFIGURATIONS ON IOS USING A VARIABLE
      hosts: iosxe
      connection: network_cli
      gather_facts: no
                
      vars:
        ios_commands: | 
             snmp-server community ntc-team RO
             snmp-server location FL_HQ        
             snmp-server contact JAMES_CHARLES

      tasks:
    
          - name: TASK 1 in PLAY 3 - ENSURE SNMP COMMANDS EXIST ON IOS DEVICES
            cli_config:
              config: "{{ ios_commands }}"

    - name: PLAY 4 - DEPLOYING SNMP CONFIGURATIONS ON JUNOS USING A VARIABLE
      hosts: vmx
      connection: network_cli
      gather_facts: no
                
      vars:
        junos_commands: |
             set snmp location FL_HQ
             set snmp contact JAMES_CHARLES
             set snmp community public authorization read-only
        
      tasks:
            
        - name: TASK 1 in PLAY 4 - ENSURE SNMP COMMANDS EXIST ON VMX DEVICES
          cli_config:
            config: "{{ junos_commands }}"
          

    - name: PLAY 5 - DEPLOYING SNMP CONFIGURATIONS ON IOS AND JUNOS
      hosts: iosxe,vmx
      connection: network_cli
      gather_facts: no
                
      vars:
        vendor_commands:
          ios: |
            snmp-server community ntc-team RO
            snmp-server location FL_HQ        
            snmp-server contact JAMES_CHARLES
          junos: |
             set snmp location FL_HQ
             set snmp contact JAMES_CHARLES
             set snmp community public authorization read-only

      tasks:
    
          - name: TASK 1 in PLAY 5 - ENSURE SNMP COMMANDS EXIST ON IOS AND VMX DEVICES
            cli_config:
              config: "{{ vendor_commands[ansible_network_os] }}"

    ####################################################################################################
    ##############################  LAB 4 Using Check Mode and Verbosity  ##############################
    ####################################################################################################

ntc@ntc-training:ansible$ cp snmp-config-01.yml snmp-config-04.yml
ntc@ntc-training:ansible$


      - name: TASK 1 in PLAY 1 - ENSURE SNMP COMMANDS EXIST ON IOS DEVICES
        ios_config:
          commands:
            - snmp-server community ntc-course RO
            - snmp-server community supersecret RW
            - snmp-server location NYC_HQ
            - snmp-server contact JOHN_SMITH
  
  
      - name: TASK 1 in PLAY 2 - ENSURE SNMP COMMANDS EXIST ON JUNOS DEVICES
        junos_config:
          lines:
            - set snmp community public authorization read-only
            - set snmp community supersecret authorization read-write
            - set snmp location NYC_HQ
            - set snmp contact JOHN_SMITH


ntc@ntc-training:ansible$ ansible-playbook -i inventory snmp-config-04.yml -v

- snmp-server location NYC_HQ_COLO

- set snmp location NYC_HQ_COLO



---

  - name: PLAY 1 - DEPLOYING SNMP CONFIGURATIONS ON IOS
    hosts: iosxe
    connection: network_cli
    gather_facts: no

    tasks:

      - name: TASK 1 in PLAY 1 - ENSURE SNMP COMMANDS EXIST ON IOS DEVICES
        ios_config:
          commands:
            - snmp-server community ntc-course RO
            - snmp-server community supersecret RW
            - snmp-server location NYC_HQ_COLO
            - snmp-server contact JOHN_SMITH
            
  - name: PLAY 2 - DEPLOYING SNMP CONFIGURATIONS ON JUNOS
    hosts: vmx
    connection: netconf
    gather_facts: no

    tasks:

      - name: TASK 1 in PLAY 2 - ENSURE SNMP COMMANDS EXIST ON JUNOS DEVICES
        junos_config:
          lines:
            - set snmp community public authorization read-only
            - set snmp community supersecret authorization read-write
            - set snmp location NYC_HQ_COLO
            - set snmp contact JOHN_SMITH      


ntc@ntc-training:ansible$ ansible-playbook -i inventory snmp-config-04.yml --check


ssh ntc@csr1


ntc@ntc-training:ansible$ ssh ntc@vmx1


ntc@ntc-training:ansible$ ansible-playbook -i inventory snmp-config-04.yml --check -v


ntc@ntc-training:ansible$ ansible-playbook -i inventory snmp-config-04.yml -v


ntc@ntc-training:ansible$ ansible-playbook -i inventory snmp-config-04.yml -v


    ####################################################################################################
    ##############################  LAB 5 Creating the Course Inventory  ###############################
    ####################################################################################################

[all:vars]
ansible_user=ntc
ansible_ssh_pass=ntc123

[iosxe:vars]
ansible_network_os=ios
ntc_api=ssh
ntc_vendor=cisco

[nxos:vars]
ansible_network_os=nxos
ntc_api=nxapi
ntc_vendor=cisco

[vmx:vars]
ansible_network_os=junos
ntc_api=netconf
ntc_vendor=juniper

[eos:vars]
ansible_network_os=eos
ntc_api=eapi
ntc_vendor=arista

[iosxe]
csr[1:3]

[nxos-spines]
nxos-spine[1:2]

[vmx]
vmx[1:3]

[eos-spines]
eos-spine[1:2]

[eos-leaves]
eos-leaf[1:2]

[eos:children]
eos-spines
eos-leaves

[nxos:children]
nxos-spines

[AMER:children]
iosxe

[EMEA:children]
vmx

    ####################################################################################################
    ##################################  LAB 6 Using the Debug Module  ##################################
    ####################################################################################################

