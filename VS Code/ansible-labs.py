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

ntc@ntc-training:~$ cd ansible/
ntc@ntc-training:ansible$

ntc@ntc-training:ansible$ touch debug.yml
ntc@ntc-training:ansible$


---

  - name: USING THE DEBUG MODULE
    hosts: iosxe
    connection: local
    gather_facts: no


    tasks:
      - name: DEBUG AND PRINT TO TERMINAL
        debug: 
          var: ntc_vendor

ntc@ntc-training:ansible$ ansible-playbook -i inventory debug.yml

    hosts: all

ntc@ntc-training:ansible$ ansible-playbook -i inventory debug.yml

[all:vars]
ansible_user=ntc
ansible_ssh_pass=ntc123
ntc_device_type=unknown


---

  - name: USING THE DEBUG MODULE
    hosts: all
    connection: local
    gather_facts: no


    tasks:
      - name: DEBUG AND PRINT TO TERMINAL
        debug:
          var: ntc_vendor

      - name: DEBUG AND PRINT DEVICE TYPE TO TERMINAL
        debug:
          var: ntc_device_type

ntc@ntc-training:ansible$ ansible-playbook -i inventory debug.yml

[iosxe:vars]
ansible_network_os=ios
ntc_api=ssh
ntc_vendor=cisco
ntc_device_type=csr1000v

[nxos:vars]
ansible_network_os=nxos
ntc_api=nxapi
ntc_vendor=cisco
ntc_device_type=n9kv

ntc@ntc-training:ansible$ ansible-playbook -i inventory debug.yml


[iosxe]
csr1    ntc_device_type=csr1000v-ng
csr2
csr3

[nxos-spines]
nxos-spine1  ntc_device_type=n9k
nxos-spine2

ntc@ntc-training:ansible$ ansible-playbook -i inventory debug.yml

---

  - name: USING THE DEBUG MODULE
    hosts: all
    connection: local
    gather_facts: no


    tasks:
      - name: DEBUG AND PRINT TO TERMINAL
        debug: 
          var: ntc_vendor

      - name: DEBUG AND PRINT DEVICE TYPE TO TERMINAL
        debug:
          var: ntc_device_type

      - name: DEBUG AND PRINT THE OS
        debug: 
          msg: "The OS for {{ inventory_hostname }} is {{ ansible_network_os }}."

ntc@ntc-training:ansible$ ansible-playbook -i inventory debug.yml

[iosxe]
csr1    ntc_device_type=csr1000v-ng
csr2    ansible_host=10.1.1.1
csr3


      - name: DEBUG AND PRINT INVENTORY_HOSTNAME VS ANSIBLE_HOST
        debug: 
           msg: "Devices defined in inventory_hostname: {{ inventory_hostname }} and ansible_host: {{ ansible_host }}"


ntc@ntc-training:ansible$ ansible-playbook -i inventory debug.yml

# Remove ansible_host=10.1.1.1 from the inventory or it will cause problems in later labs.

      - name: DEBUG AND PRINT LIST OF PLAY_HOSTS
        debug: 
          var: play_hosts

ntc@ntc-training:ansible$ ansible-playbook -i inventory debug.yml

      - name: DEBUG AND PRINT GROUP_NAMES
        debug: 
          var: group_names

ntc@ntc-training:ansible$ ansible-playbook -i inventory debug.yml


---

  - name: USING THE DEBUG MODULE
    hosts: csr1
    connection: local
    gather_facts: no


      - name: DEBUG AND PRINT GROUPS
        debug: 
          var: groups


ntc@ntc-training:ansible$ ansible-playbook -i inventory debug.yml


      - name: DEBUG AND PRINT ANSIBLE_VERSION
        debug: 
           msg: "Ansible Version: '{{ ansible_version }}'"

ntc@ntc-training:ansible$ ansible-playbook -i inventory debug.yml

    ####################################################################################################
    ###############################  LAB 7 Prompting the User for Input  ###############################
    ####################################################################################################

ntc@ntc-training:ansible$ touch user_input.yml
ntc@ntc-training:ansible$


---
- name: COLLECT USERNAME AND PASSWORD
  hosts: csr1
  connection: local
  gather_facts: no



---
- name: COLLECT USERNAME AND PASSWORD
  hosts: csr1
  connection: local
  gather_facts: no

  vars_prompt:
    - name: un
      prompt: "Please enter the username"
      private: no

    - name: pwd
      prompt: "Please enter the password"
      private: no

  tasks:

    - name: DISPLAY THE USERNAME AND PASSWORD
      debug:
        msg: "The Username is {{ un }} and password is {{ pwd }}"


ntc@ntc-training:ansible$ ansible-playbook -i inventory user_input.yml


---
- name: COLLECT USERNAME AND PASSWORD
  hosts: csr1
  connection: local
  gather_facts: no

  vars_prompt:
    - name: un
      prompt: "Please enter the username"
      private: no

    - name: pwd
      prompt: "Please enter the password"
      private: yes

  tasks:

    - name: DISPLAY THE USERNAME AND PASSWORD
      debug:
        msg: "The Username is {{ un }} and password is {{ pwd }}"


ntc@ntc-training:ansible$ ansible-playbook -i inventory user_input.yml


---
- name: COLLECT USERNAME AND PASSWORD
  hosts: csr1
  connection: local
  gather_facts: no

  vars_prompt:
    - name: un
      prompt: "Please enter the username"
      private: no
      default: ntc

    - name: pwd
      prompt: "Please enter the password"

  tasks:

    - name: DISPLAY THE USERNAME AND PASSWORD
      debug:
        msg: "The Username is {{ un }} and password is {{ pwd }}"


ntc@ntc-training:ansible$ ansible-playbook -i inventory user_input.yml

    ####################################################################################################
    #######################  LAB 8 Auto-Create Directories Using the File Module  ######################
    ####################################################################################################


ntc@ntc-training:ansible$ ansible-doc file

ntc@ntc-training:ansible$ touch auto-create.yml
ntc@ntc-training:ansible$


---

  - name: Auto Generate Files and Directories
    hosts: all
    connection: local
    gather_facts: no



---

  - name: Auto Generate Files and Directories
    hosts: all
    connection: local
    gather_facts: no

    tasks:

      - name: CREATE DIRECTORIES BASED ON OS
        file:
          path: ./tmp/{{ ansible_network_os }}/
          state: directory
          
          
          
ntc@ntc-training:ansible$ tree


---

  - name: Auto Generate Files and Directories
    hosts: all
    connection: local
    gather_facts: no

    tasks:

      - name: CREATE DIRECTORIES BASED ON OS
        file:
          path: ./tmp/{{ ansible_network_os }}/
          state: directory

      - name: CREATE SNMP.CONF FILE
        file:
          path: ./tmp/{{ ansible_network_os }}/{{ inventory_hostname }}-snmp.conf
          state: touch 
            

ntc@ntc-training:ansible$ ansible-playbook -i inventory auto-create.yml

ntc@ntc-training:ansible$ tree


---

  - name: Auto Generate Files and Directories
    hosts: all
    connection: local
    gather_facts: no

    tasks:

      - name: DELETE DIRECTORIES PREVIOUSLY CREATED BASED ON OS
        file:
          path: ./tmp
          state: absent
            

ntc@ntc-training:ansible$ ansible-playbook -i inventory auto-create.yml

ntc@ntc-training:ansible$ tree

    ####################################################################################################
    ##########################  LAB 9 Getting Started with the Command Module  #########################
    ####################################################################################################


---

  - name: BACKUP SHOW VERSION FOR IOS
    hosts: csr1
    connection: network_cli
    gather_facts: no

    tasks:



---

  - name: BACKUP SHOW VERSION FOR IOS
    hosts: csr1
    connection: network_cli
    gather_facts: no

    tasks:
      - name: GET SHOW COMMANDS
        ios_command:
          commands: show version


ntc@ntc-training:ansible$ ansible-playbook -i inventory core-command.yml 

ntc@ntc-training:ansible$ ansible-playbook -i inventory core-command.yml -v

      - name: GET SHOW COMMANDS
        ios_command:
          commands: show version
        register: config_data

      - name: VIEW DATA STORED IN CONFIG_DATA
        debug:
          var: config_data


ntc@ntc-training:ansible$ ansible-playbook -i inventory core-command.yml

      - name: GENERATE DIRECTORIES
        file:
          path: ./command-outputs/{{ ansible_network_os }}
          state: directory


      - name: SAVE SH VERSION TO FILE
        copy :
          content: "{{ config_data['stdout'][0] }}"
          dest: ./command-outputs/{{ ansible_network_os }}/show_version.txt


ntc@ntc-training:ansible$ ansible-playbook -i inventory core-command.yml

      - name: SAVE SH VERSION TO FILE
        copy :
          content: "{{ config_data['stdout'][0] }}"
          dest: ./command-outputs/{{ ansible_network_os }}/{{ inventory_hostname}}-show_version.txt



---

  - name: BACKUP SHOW VERSION ON IOS
    hosts: iosxe
    connection: network_cli
    gather_facts: no

    tasks:
      - name: GET SHOW COMMANDS
        ios_command:
          commands: show version
        register: config_data

      - name: VIEW DATA STORED IN CONFIG_DATA
        debug:
          var: config_data

      - name: GENERATE DIRECTORIES
        file:
          path: ./command-outputs/{{ ansible_network_os }}/
          state: directory

      - name: SAVE SH VERSION TO FILE
        copy :
          content: "{{ config_data['stdout'][0] }}"
          dest: ./command-outputs/{{ ansible_network_os }}/{{ inventory_hostname}}-show_version.txt

    ####################################################################################################
    ##############################  LAB 10 Continuous Compliance with IOS  #############################
    ####################################################################################################      


---

  - name: IOS COMPLIANCE
    hosts: iosxe
    connection: network_cli
    gather_facts: no


    tasks:

      - name: IOS show version
        ios_command:
          commands:
            - show version
        register: output

      - name: CHECK OS AND CONFIG REGISTER
        assert:
          that:
           - "'17.01.01' in output['stdout'][0]"
           - "'0x2102' in output['stdout'][0]"

ntc@ntc-training:ansible$ ansible-playbook -i inventory compliance.yml   


---

  - name: IOS COMPLIANCE
    hosts: iosxe
    connection: network_cli
    gather_facts: no


    tasks:

      - name: IOS show version
        ios_command:
          commands:
            - show version
        register: output

      - name: CHECK OS AND CONFIG REGISTER
        assert:
          that:
           - "'17.01.01' in output['stdout'][0]"
           - "'0x2102' in output['stdout'][0]"
           
           
  
  - name: JUNOS COMPLIANCE
    hosts: vmx
    connection: netconf
    gather_facts: no
    tags: vmx


    tasks:

      - name: JUNOS show version
        junos_command:
          commands:
            - show system storage
          display: json
        register: output

      - name: VIEW JSON DATA
        debug:
          var: output

ntc@ntc-training:ansible$ ansible-playbook -i inventory compliance.yml   


      - name: CREATE NEW VARIABLES
        set_fact:
          percent: "{{ output['stdout'][0]['system-storage-information'][0]['filesystem'][0]['used-percent'][0]['data'] }}"
          filesystem: "{{ output['stdout'][0]['system-storage-information'][0]['filesystem'][0]['filesystem-name'][0]['data'] }}"
          blocks: "{{ output['stdout'][0]['system-storage-information'][0]['filesystem'][0]['available-blocks'][0]['data'] }}"
          storage: "{{ output['stdout'][0]['system-storage-information'][0]['filesystem'][0]['available-blocks'][0]['attributes']['junos:format'] }}"

      - name: VIEW DATA STORED IN NEW VARIABLES
        debug:
          msg: "Percent: {{ percent }}%,  filesystem: {{ filesystem }}, Blocks: {{ blocks }}, Storage: {{ storage }}"


ntc@ntc-training:ansible$ ansible-playbook -i inventory compliance.yml   


      - name: CHECK STORAGE FILESYSTEM PERCENT
        assert:
          that:
            - "percent | int  <= 50"
          fail_msg: "Warning!! filesystem {{ filesystem }} is at {{ percent }}%"
          success_msg: "Current filesystem  {{ filesystem }} is at {{ percent }}%"
        
      - name: CHECK STORAGE FILESYSTEM AVAILABILITY
        assert:
          that:
            - "blocks | int >= 4194304"
          fail_msg: "Warning!! filesystem {{ filesystem }} is at {{ storage }}"
          success_msg: "Current filesystem  {{ filesystem }} is at {{ storage }}"


ntc@ntc-training:ansible$ ansible-playbook -i inventory compliance.yml 


      - name: CREATE NEW VARIABLES
        set_fact:
          #percent: "{{ output['stdout'][0]['system-storage-information'][0]['filesystem'][0]['used-percent'][0]['data'] }}"
          percent: "60"
          filesystem: "{{ output['stdout'][0]['system-storage-information'][0]['filesystem'][0]['filesystem-name'][0]['data'] }}"
          blocks: "{{ output['stdout'][0]['system-storage-information'][0]['filesystem'][0]['available-blocks'][0]['data'] }}"
          storage: "{{ output['stdout'][0]['system-storage-information'][0]['filesystem'][0]['available-blocks'][0]['attributes']['junos:format'] }}"

ntc@ntc-training:ansible$ ansible-playbook -i inventory compliance.yml 


      - name: CHECK STORAGE FILESYSTEM PERCENT
        assert:
          that:
           - "percent | int  <= 50"
          fail_msg: "Warning!! filesystem {{ filesystem }} is at {{ percent }}%"
          success_msg: "Current filesystem  {{ filesystem }} is at {{ percent }}%"
        ignore_errors: true
        

      - name: CHECK STORAGE FILESYSTEM AVAILABILITY
        assert:
          that:
           - "blocks | int >= 4194304"
          fail_msg: "Warning!! filesystem {{ filesystem }} is at {{ storage }}"
          success_msg: "Current filesystem  {{ filesystem }} is at {{ storage }}"
        ignore_errors: true


ntc@ntc-training:ansible$ ansible-playbook -i inventory compliance.yml  


---

  - name: IOS COMPLIANCE
    hosts: iosxe
    connection: network_cli
    gather_facts: no
    tags: ios


    tasks:

      - name: IOS show version
        ios_command:
          commands:
            - show version
        register: output

      - name: CHECK OS AND CONFIG REGISTER
        assert:
          that:
           - "'17.01.01' in output['stdout'][0]"
           - "'0x2102' in output['stdout'][0]"


  - name: JUNOS COMPLIANCE
    hosts: vmx
    connection: netconf
    gather_facts: no
    tags: vmx


    tasks:

      - name: JUNOS show version
        junos_command:
          commands:
            - show system storage
          display: json
        register: output


      - name: VIEW JSON DATA
        debug:
          var: output

      - name: CREATE NEW VARIABLES
        set_fact:
           #percent: "{{ output['stdout'][0]['system-storage-information'][0]['filesystem'][0]['used-percent'][0]['data'] }}"
           percent: "60"
           filesystem: "{{ output['stdout'][0]['system-storage-information'][0]['filesystem'][0]['filesystem-name'][0]['data'] }}"
           blocks: "{{ output['stdout'][0]['system-storage-information'][0]['filesystem'][0]['available-blocks'][0]['data'] }}"
           storage: "{{ output['stdout'][0]['system-storage-information'][0]['filesystem'][0]['available-blocks'][0]['attributes']['junos:format'] }}"


      - name: VIEW DATA STORED IN NEW VARIABLES
        debug:
          msg: "Percent: {{ percent }}%,  filesystem: {{ filesystem }}, Blocks: {{ blocks }}, Storage: {{ storage }}"


      - name: CHECK STORAGE FILESYSTEM PERCENT
        assert:
          that:
           - "percent | int  <= 50"
          fail_msg: "Warning!! filesystem {{ filesystem }} is at {{ percent }}%"
          success_msg: "Current filesystem  {{ filesystem }} is at {{ percent }}%"
        ignore_errors: true
        

      - name: CHECK STORAGE FILESYSTEM AVAILABILITY
        assert:
          that:
           - "blocks | int >= 4194304"
          fail_msg: "Warning!! filesystem {{ filesystem }} is at {{ storage }}"
          success_msg: "Current filesystem  {{ filesystem }} is at {{ storage }}"
        ignore_errors: true



##################################################################################################################################
##################################################################################################################################
##################################  SECTION 02 - Configuration Templating with Jinja2 and YAML  ##################################
##################################################################################################################################
##################################################################################################################################


    ####################################################################################################
    ##########################  LAB 11 Getting Started with Jinja2 Templates  ##########################
    ####################################################################################################

# ./ansible/templates/ios-snmp.j2
# ./ansible/templates/junos-snmp.j2
# ./ansible/group_vars/AMER.yml
# ./ansible/group_vars/EMEA.yml

ntc@ntc-training:ansible$ touch deploy-snmp.yml
ntc@ntc-training:ansible$

---

- name: GENERATE SNMP CONFIGS USING JINJA2 - AMERICAS
  hosts: AMER
  connection: local
  gather_facts: no

  vars:
    snmp_ro: ntc_course

  tasks:

    - name: VIEW SNMP_RO VARIABLE
      debug: 
        var: snmp_ro


ntc@ntc-training:ansible$ ansible-playbook -i inventory deploy-snmp.yml


---

- name: GENERATE SNMP CONFIGS USING JINJA2 - AMERICAS
  hosts: AMER
  connection: local
  gather_facts: no

  vars:
    snmp_ro: ntc_course

  tasks:
  
    - name: VIEW SNMP_RO VARIABLE
      debug: 
        var: snmp_ro
        
    - name: GENERATE IOS SNMP CONFIGURATIONS
      template:
        src: ios-snmp.j2
        dest: "./configs/{{ inventory_hostname }}-snmp.cfg"


ntc@ntc-training:ansible$
ntc@ntc-training:ansible$ mkdir templates
ntc@ntc-training:ansible$ cd templates
ntc@ntc-training:templates$

ntc@ntc-training:templates$ touch ios-snmp.j2
ntc@ntc-training:templates$

snmp-server community {{ snmp_ro }}  RO

ntc@ntc-training:ansible$ ansible-playbook -i inventory deploy-snmp.yml

ntc@ntc-training:ansible$ cd configs
ntc@ntc-training:configs$ cat csr1-snmp.cfg

snmp-server community ntc_course  RO

ntc@ntc-training:ansible$ mkdir group_vars
ntc@ntc-training:ansible$ cd group_vars
ntc@ntc-training:group_vars$ touch AMER.yml
ntc@ntc-training:group_vars$ touch EMEA.yml
ntc@ntc-training:group_vars$

# AMER.yml
snmp_ro: ntc_course
snmp_rw: ntc_private
snmp_location: NYC
snmp_contact: netops_team

# EMEA.yml
snmp_ro: ntc_course
snmp_rw: ntc_private
snmp_location: MILAN
snmp_contact: netops_team

# Update ios-snmp.j2
snmp-server community {{ snmp_ro }}  RO
snmp-server community {{ snmp_rw }}  RW
snmp-server contact {{ snmp_contact }}  
snmp-server location {{ snmp_location }}

# Update junos-snmp.j2
set snmp community {{ snmp_ro }} authorization read-only
set snmp community {{ snmp_rw }} authorization read-write
set snmp location {{ snmp_location }}
set snmp contact {{ snmp_contact }}


---

- name: GENERATE SNMP CONFIGS USING JINJA2 - AMERICAS
  hosts: AMER
  connection: local
  gather_facts: no

  tasks:
 
    - name: VIEW SNMP_RO VARIABLE
      debug: 
         var: snmp_ro
        
    - name: VIEW SNMP_LOCATION VARIABLE
      debug: 
         var: snmp_location
        
        
    - name: GENERATE IOS SNMP CONFIGURATIONS
      template:
         src: ios-snmp.j2
         dest: "./configs/{{ inventory_hostname }}-snmp.cfg"


# Update play for EMEA

---

- name: GENERATE SNMP CONFIGS USING JINJA2 - AMERICAS
  hosts: AMER
  connection: local
  gather_facts: no

  tasks:
 
    - name: VIEW SNMP_RO VARIABLE
      debug: 
         var: snmp_ro
        
    - name: VIEW SNMP_LOCATION VARIABLE
      debug: 
         var: snmp_location
        
        
    - name: GENERATE IOS SNMP CONFIGURATIONS
      template:
         src: ios-snmp.j2
         dest: "./configs/{{ inventory_hostname }}-snmp.cfg"

- name: GENERATE SNMP CONFIGS USING JINJA2 - EMEA
  hosts: EMEA
  connection: local
  gather_facts: no

  tasks:
    
    - name: VIEW SNMP_RO VARIABLE
      debug: 
        var: snmp_ro
        
    - name: VIEW SNMP_LOCATION VARIABLE
      debug: 
        var: snmp_location
    
    - name: GENERATE JUNOS SNMP CONFIGURATIONS
      template:
        src: junos-snmp.j2
        dest: "./configs/{{ inventory_hostname }}-snmp.cfg"

ntc@ntc-training:ansible$ ansible-playbook -i inventory deploy-snmp.yml

ntc@ntc-training:ansible$ ls configs/
# output omitted

    ####################################################################################################
    ##########################  LAB 12 Expanding the Use of Jinja2 Templates  ##########################
    ####################################################################################################

# AMER.yml
snmp_config:
  ro:
    - public
    - ntc-course
  rw:
    - private
    - ntc-private
  contact: netops_team
  location: NYC

# EMEA.yml
snmp_config:
  ro:
    - public
    - ntc-course
  rw:
    - private
    - ntc-private
  contact: netops_team
  location: MILAN

# ios-snmpv2.j2
{% for ro_comm in snmp_config.ro %}
snmp-server community {{ ro_comm }} RO
{% endfor %}
{% for rw_comm in snmp_config.rw %}
snmp-server community {{ rw_comm }} RW
{% endfor %}
snmp-server location {{ snmp_config.location }}
snmp-server contact {{ snmp_config.contact }}

# junos-snmpv2.j2
{% for ro_comm in snmp_config.ro %}
set snmp community {{ ro_comm }} authorization read-only
{% endfor %}
{% for rw_comm in snmp_config.rw %}
set snmp community {{ rw_comm }} authorization read-write
{% endfor %}
set snmp location {{ snmp_config.location }}
set snmp contact {{ snmp_config.contact }}


---

- name: GENERATE SNMP CONFIGS USING JINJA2 - AMERICAS
  hosts: AMER
  connection: local
  gather_facts: no

  tasks:
 
    - name: GENERATE IOS SNMP CONFIGURATIONS
      template:
         src: ios-snmpv2.j2
         dest: "./configs/{{ inventory_hostname }}-snmp.cfg"

- name: GENERATE SNMP CONFIGS USING JINJA2 - EMEA
  hosts: EMEA
  connection: local
  gather_facts: no

  tasks:
    
    - name: GENERATE JUNOS SNMP CONFIGURATIONS
      template:
        src: junos-snmpv2.j2
        dest: "./configs/{{ inventory_hostname }}-snmp.cfg"


# Update playbook src

---

- name: GENERATE SNMP CONFIGS USING JINJA2 - AMERICAS
  hosts: AMER
  connection: local
  gather_facts: no

  tasks:
 
    - name: GENERATE IOS SNMP CONFIGURATIONS
      template:
         src: ios-snmpv2.j2
         dest: "./configs/{{ inventory_hostname }}-snmp.cfg"

- name: GENERATE SNMP CONFIGS USING JINJA2 - EMEA
  hosts: EMEA
  connection: local
  gather_facts: no

  tasks:
    
    - name: GENERATE JUNOS SNMP CONFIGURATIONS
      template:
        src: junos-snmpv2.j2
        dest: "./configs/{{ inventory_hostname }}-snmp.cfg"


ntc@ntc-training:ansible$ ansible-playbook -i inventory deploy-snmp.yml

# Create host_cars and csr3.yml inside this directory
snmp_config:
  ro:
    - ntc-public
  rw:
    - private
    - ntc-private
  contact: netdevops_tiger_team
  location: NYC

ntc@ntc-training:ansible$ ansible-playbook -i inventory deploy-snmp.yml

    - name: DEBUG AND PRINT SNMP VARIABLES
      debug:
        var: snmp_config

---

- name: GENERATE SNMP CONFIGS USING JINJA2
  hosts: AMER, EMEA
  connection: local
  gather_facts: no

  tasks:
 
    - name: GENERATE SNMP CONFIGURATIONS
      template:
         src: "{{ ansible_network_os }}-snmpv2.j2"
         dest: "./configs/{{ inventory_hostname }}-snmp.cfg"

##################################################################################################################################
##################################################################################################################################
#################################  SECTION 03 - Diving Deeper Into Core Command & Config Modules  ################################
##################################################################################################################################
##################################################################################################################################


    ####################################################################################################
    #####################  LAB 13 Validating Reachability with the Command Module  #####################
    ####################################################################################################

---

  - name: TEST REACHABILITY - SOLUTION 1
    hosts: iosxe
    connection: network_cli
    gather_facts: no

    vars:
      target_ips:
        - "10.0.0.15"
        - "10.0.0.2"
        - "198.6.1.4"

    tasks:

      - name: ENSURE DIRECTORY FOR EACH DEVICE EXISTS
        file:
          path: ./ping-responses/
          state: directory

      - name: SEND PING COMMANDS TO DEVICES
        ios_command:
          commands: "ping {{ item }} repeat 2"
        register: ping_responses
        loop: "{{ target_ips }}"

      - name: VERIFY REGISTERED VARIABLE
        debug:
          var: ping_responses

      - name: TEST LOOPING OVER REGISTERED VARIABLE
        debug:
          var: "{{ item }}"
        loop: "{{ ping_responses.results }}"

      - name: SAVE OUTPUTS TO INDIVIDUAL FILES
        template:
          src: basic-copy-single.j2
          dest: ./ping-responses/ping_responses_from_{{ inventory_hostname }}.txt


    ####################################################################################################
    ###########################  LAB 14 Performing a Conditional Traceroute  ###########################
    ####################################################################################################

    ---

  - name: PING TEST AND TRACEROUTE
    hosts: csr1
    connection: network_cli
    gather_facts: no

    vars:
      dest: "10.0.0.15"

    tasks:

    - name: ISSUE PING
      ios_command:
        commands: "ping {{ dest }} repeat 2"
      register: output

    - name: PARSE PING RESPONSE TO OBTAIN % OF SUCCESS
      set_fact:
        ping_pct: "{{ output.stdout.0 | regex_search('Success rate is (\\d+)\\s+percent') | regex_search('(\\d+)') }}"

    - debug:
        var: ping_pct

    - name: ALTERNATE OPTION FOR PARSING WITH REGEX
      set_fact:
        ping_data2: "{{ output.stdout.0 | regex_findall('Success rate is (\\d+)\\s+percent') | first }}"

    - name: ISSUE TRACEROUTE
      ios_command:
        commands: "traceroute {{ dest }} timeout 1 ttl 1 5"
      register: traceroute
      when: ping_pct|int < 81

    - name: DEBUG TRACEROUTE
      debug:
        var: traceroute  


    ####################################################################################################
    ###############################  LAB 15 Exploring the Config Module  ###############################
    ####################################################################################################

# config-interfaces.yml
---

  - name: CONFIGURING INTERFACES
    hosts: iosxe
    connection: network_cli
    gather_facts: no

    tasks:
    
       - name: BACKUP CONFIG
         ios_config:
           backup: True

       - name: CONFIGURING LOOPBACK
         ios_config:
           parents:
             - interface Loopback200
           commands:
             - ip address 10.200.100.{{ inventory_hostname[-1] }} 255.255.255.255

# aaa.yml

---

  - name: CONFIGURING AAA SERVER GROUPS
    hosts: csr1
    connection: network_cli
    gather_facts: no

    tasks:
      - name: DEPLOYING AAA GROUP AND IPS 1
        ios_config:
          parents:
            - aaa group server tacacs+ TESTING
          commands:
            - server 1.2.3.4
            - server 2.1.3.4
            - server 3.2.1.4
        tags: starting_config

ntc@ntc-training:ansible$ ansible-playbook -i inventory aaa.yml --tags=starting_config -v


---

  - name: CONFIGURING AAA SERVER GROUPS
    hosts: csr1
    connection: network_cli
    gather_facts: no

    tasks:
      - name: DEPLOYING AAA GROUP AND IPS 1
        ios_config:
          parents:
            - aaa group server tacacs+ TESTING
          commands:
            - server 1.2.3.4
            - server 2.1.3.4
            - server 3.2.1.4
        tags: starting_config

      - name: DEPLOYING AAA GROUP AND IPS 2
        ios_config:
          parents:
            - aaa group server tacacs+ TESTING
          commands:
            - server 4.3.2.1
            - server 1.2.3.4
            - server 2.1.3.4
            - server 3.2.1.4
        tags: append_server

ntc@ntc-training:ansible$ ansible-playbook -i inventory aaa.yml --tags=append_server -v


---

  - name: CONFIGURING AAA SERVER GROUPS
    hosts: csr1
    connection: network_cli
    gather_facts: no

    tasks:
      - name: DEPLOYING AAA GROUP AND IPS
        ios_config:
          parents:
            - aaa group server tacacs+ TESTING
          commands:
            - server 1.2.3.4
            - server 2.1.3.4
            - server 3.2.1.4
        tags: starting_config

      - name: DEPLOYING AAA GROUP AND IPS
        ios_config:
          parents:
            - aaa group server tacacs+ TESTING
          commands:
            - server 4.3.2.1
            - server 1.2.3.4
            - server 2.1.3.4
            - server 3.2.1.4
        tags: append_server

      - name: DEPLOYING AAA GROUP AND IPS
        ios_config:
          before: no aaa group server tacacs+ TESTING
          parents:
            - aaa group server tacacs+ TESTING
          commands:
            - server 4.1.1.1
            - server 1.2.3.4
            - server 2.1.3.4
            - server 3.2.1.5
          match: exact
        tags: replace_on_change

ntc@ntc-training:ansible$ ansible-playbook -i inventory aaa.yml --tags=replace_on_change -v


---

  - name: USING DIFF AGAINST WITH CONFIG
    hosts: csr1
    connection: network_cli
    gather_facts: no

    tasks:

      - name: ENSURE THAT LOOPBACK222 IS CONFIGURED
        ios_config:
          parents:
            - interface Loopback222
          commands:
            - ip address 10.224.222.222 255.255.255.255
          diff_against: running
        tags: diff_me

ntc@ntc-training:ansible$ ansible-playbook -i inventory verify-config.yml --tags=diff_me --diff

  - name: USING DIFF AGAINST WITH CONFIG
    hosts: csr1
    connection: network_cli
    gather_facts: no

    tasks:

      - name: ENSURE THAT LOOPBACK222 IS CONFIGURED
        ios_config:
          parents:
            - interface Loopback222
          commands:
            - ip address 10.224.222.222 255.255.255.255
          diff_against: running
        tags: diff_me

      - name: CREATE BACKUP FILE VARIABLE
        set_fact:
          backup_file: "{{ lookup('fileglob', 'backup/{{ inventory_hostname }}_config.*') }}"
        tags: verify_config

      - name: VERIFY GOLDEN CONFIGURATION
        ios_config:
          diff_against: intended
          intended_config: "{{ lookup('file', '{{ backup_file }}') }}"
        tags: verify_config

ntc@ntc-training:ansible$ ansible-playbook -i inventory verify-config.yml --tags=verify_config --diff


    ####################################################################################################
    #########################  LAB 16 Making RESTful API Calls with Ansible  ###########################
    ####################################################################################################

Lab 16 - Making REST API Calls from Ansible
This lab shows how you can make HTTP-based API calls from Ansible. We'll look at making API calls to IOS-XE and NX-OS based systems using RESTCONF and NX-API, respectively, on those systems.

Task 1 - Using the IOS-XE API
This task will query Cisco IOS-XE routers for their GigE1 IP using the RESTCONF API available in 16.6 and later.

Step 1
SSH into csr2 and apply the following changes:

!
interface GigabitEthernet2
 ip address 10.1.13.1 255.255.255.0
!
Step 2
Create a playbook called rest-apis.yml and insert the following into it:

---

  - name: PLAY 1 - ISSUE API CALL TO CSR
    hosts: csr2
    connection: local
    gather_facts: no
    tags: ios

    tasks:

      - name: GET INTERFACE IP ADDRESS
        uri:
          url: https://{{ inventory_hostname }}/restconf/data/Cisco-IOS-XE-native:native/interface=GigabitEthernet/2/ip/address
          method: GET
          user: "{{ ansible_user }}"
          password: "{{ ansible_ssh_pass }}"
          return_content: yes
          validate_certs: no
          headers:
            Content-Type: application/yang-data+json
            Accept: application/yang-data+json
        register: response

      - debug:
          var: response
Step 3
Save and execute the playbook.

Do you see the API response?

Step 4
You should see there is a content key inside response that contains the actual response we need. Let's print just the content data now.

Add a new debug statement to the playbook:

---

  - name: PLAY 1 - ISSUE API CALL TO CSR
    hosts: csr2
    connection: local
    gather_facts: no
    tags: ios

    tasks:

      - name: GET INTERFACE IP ADDRESS
        uri:
          url: https://{{ inventory_hostname }}/restconf/data/Cisco-IOS-XE-native:native/interface=GigabitEthernet/2/ip/address
          method: GET
          user: "{{ ansible_user }}"
          password: "{{ ansible_ssh_pass }}"
          return_content: yes
          validate_certs: no
          headers:
            Content-Type: application/yang-data+json
            Accept: application/yang-data+json
        register: response

      - debug:
          var: response

      - debug:
          var: response['content']
Step 5
Execute the playbook.

You should see this response for the new task.

ok: [csr2] => {
    "response['content']": {
        "Cisco-IOS-XE-native:address": {
            "primary": {
                "address": "10.1.13.1",
                "mask": "255.255.255.0"
            }
        }
    }
}
Step 6
Try parsing the object to debug Primary IP address.

      - debug:
          var: response['content']['Cisco-IOS-XE-native:address']['primary']['address']
Does it work?

You should see this response:

TASK [debug] *******************************************************************
ok: [csr2] => {
    "response['content']['Cisco-IOS-XE-native:address']['primary']['address']": "VARIABLE IS NOT DEFINED!"
}
This is not working because remember HTTP API responses come back as a JSON string.

We need to convert it to be a dictionary.

Step 7
Remove the debug task you just added.

Step 8
Add the following tasks to convert the JSON string to a dictionary and then debug the IP address:

Note: take note of the from_json Jinja2 filter. This is doing what json.loads() does in Python when using the Python requests library.

      - set_fact:
          ip_info: "{{ response['content'] | from_json }}"

      - debug:
          var: ip_info['Cisco-IOS-XE-native:address']['primary']['address']
Step 9
Save and execute the playbook.

You should see this output:

TASK [set_fact] ****************************************************************
ok: [csr2]

TASK [debug] *******************************************************************
ok: [csr2] => {
    "ip_info['Cisco-IOS-XE-native:address']['primary']['address']": "10.1.13.1"
}
Step 10 (Optional)
Add a task to make it easier to access the IP address using the set_fact module. Then debug it.

      - set_fact:
          ipaddr: "{{ ip_info['Cisco-IOS-XE-native:address']['primary']['address'] }}"

      - debug:
          var: ipaddr
Save and re-run the playbook.

This is the full output you should see:

ntc@ntc-training:ansible$ ansible-playbook -i inventory rest-apis.yml --tags=ios

PLAY [PLAY 1 - ISSUE API CALL TO CSR] ******************************************

TASK [GET INTERFACE IP ADDRESS] ************************************************
ok: [csr2]

TASK [debug] *******************************************************************
ok: [csr2] => {
    "response": {
        "cache_control": "private, no-cache, must-revalidate, proxy-revalidate",
        "changed": false,
        "connection": "close",
        "content": "{\n  \"Cisco-IOS-XE-native:address\": {\n    \"primary\": {\n      \"address\": \"10.1.13.1\",\n      \"mask\": \"255.255.255.0\"\n    }\n  }\n}\n",
        "content_type": "application/yang-data+json",
        "cookies": {},
        "cookies_string": "",
        "date": "Sun, 02 Dec 2018 12:37:38 GMT",
        "failed": false,
        "json": {
            "Cisco-IOS-XE-native:address": {
                "primary": {
                    "address": "10.1.13.1",
                    "mask": "255.255.255.0"
                }
            }
        },
        "msg": "OK (unknown bytes)",
        "pragma": "no-cache",
        "redirected": false,
        "server": "nginx",
        "status": 200,
        "transfer_encoding": "chunked",
        "url": "https://csr2/restconf/data/Cisco-IOS-XE-native:native/interface=GigabitEthernet/2/ip/address"
    }
}

TASK [debug] *******************************************************************
ok: [csr2] => {
    "response['content']": {
        "Cisco-IOS-XE-native:address": {
            "primary": {
                "address": "10.1.13.1",
                "mask": "255.255.255.0"
            }
        }
    }
}

TASK [set_fact] ****************************************************************
ok: [csr2]

TASK [debug] *******************************************************************
ok: [csr2] => {
    "ip_info['Cisco-IOS-XE-native:address']['primary']['address']": "10.1.13.1"
}

TASK [set_fact] ****************************************************************
ok: [csr2]

TASK [debug] *******************************************************************
ok: [csr2] => {
    "ipaddr": "10.1.13.1"
}

PLAY [PLAY 2 - ISSUE SHOW VERSION TO NEXUS VIA API] ****************************

PLAY RECAP *********************************************************************
csr2                       : ok=7    changed=0    unreachable=0    failed=0   

This is the full playbook:

---

  - name: PLAY 1 - ISSUE API CALL TO CSR
    hosts: csr2
    connection: local
    gather_facts: no
    tags: ios

    tasks:

      - name: GET INTERFACE IP ADDRESS
        uri:
          url: https://{{ inventory_hostname }}/restconf/data/Cisco-IOS-XE-native:native/interface=GigabitEthernet/2/ip/address
          method: GET
          user: "{{ ansible_user }}"
          password: "{{ ansible_ssh_pass }}"
          return_content: yes
          validate_certs: no
          headers:
            Content-Type: application/yang-data+json
            Accept: application/yang-data+json
        register: response

      - debug:
          var: response

      - debug:
          var: response['content']

      - set_fact:
          ip_info: "{{ response['content'] | from_json }}"

      - debug:
          var: ip_info['Cisco-IOS-XE-native:address']['primary']['address']

      - set_fact:
          ipaddr: "{{ ip_info['Cisco-IOS-XE-native:address']['primary']['address'] }}"

      - debug:
          var: ipaddr
Task 2 - Using the NXOS NX-API
Step 1
Add a NEW play in your EXISTING playbook.

This task is showing you can also do a HTTP POST passing a multi-line string within the body parameter. Take note of the | that permits this.

  - name: PLAY 2 - ISSUE SHOW VERSION TO NEXUS VIA API
    hosts: nxos-spine1
    connection: local
    gather_facts: no
    tags: nxos

    tasks:

      - name: SHOW VERSION NEXUS API
        uri:
          url: https://nxos-spine1/ins
          method: POST
          user: "{{ ansible_user }}"
          password: "{{ ansible_ssh_pass }}"
          return_content: yes
          validate_certs: no
          body_format: json
          headers:
            Content-Type: application/json
            Accept: application/json
          body: |
            {
              "ins_api": {
                "version": "1.0",
                "type": "cli_show",
                "chunk": "0",
                "sid": "1",
                "input": "show version",
                "output_format": "json"
              }
            }
        register: response

      - debug:
          var: response

      - debug:
          var: response.content
Step 2
Save and execute the playbook using the "nxos" tag.

Step 3
Try debugging a few different variables from this object.

The full playbook is as follows:

---

  - name: PLAY 1 - ISSUE API CALL TO CSR
    hosts: csr2
    connection: local
    gather_facts: no
    tags: ios

    tasks:

      - name: GET INTERFACE IP ADDRESS
        uri:
          url: https://{{ inventory_hostname }}/restconf/data/Cisco-IOS-XE-native:native/interface=GigabitEthernet/2/ip/address
          method: GET
          user: "{{ ansible_user }}"
          password: "{{ ansible_ssh_pass }}"
          return_content: yes
          validate_certs: no
          headers:
            Content-Type: application/yang-data+json
            Accept: application/yang-data+json
        register: response

      - debug:
          var: response

      - debug:
          var: response['content']

      - set_fact:
          ip_info: "{{ response['content'] | from_json }}"

      - debug:
          var: ip_info['Cisco-IOS-XE-native:address']['primary']['address']

      - set_fact:
          ipaddr: "{{ ip_info['Cisco-IOS-XE-native:address']['primary']['address'] }}"

      - debug:
          var: ipaddr


  - name: PLAY 2 - ISSUE SHOW VERSION TO NEXUS VIA API
    hosts: nxos-spine1
    connection: local
    gather_facts: no
    tags: nxos

    tasks:

      - name: SHOW VERSION NEXUS API
        uri:
          url: https://nxos-spine1/ins
          method: POST
          user: "{{ ansible_user }}"
          password: "{{ ansible_ssh_pass }}"
          return_content: yes
          body_format: json
          validate_certs: no
          headers:
            Content-Type: application/json
            Accept: application/json
          body: |
            {
              "ins_api": {
                "version": "1.0",
                "type": "cli_show",
                "chunk": "0",
                "sid": "1",
                "input": "show version",
                "output_format": "json"
              }
            }
        register: response


      - debug:
          var: response

      - debug:
          var: response.content    

    ####################################################################################################
    ##############################  LAB 17 Data Collection and Reporting  ##############################
    ####################################################################################################

Lab 17 - Data Collection Modules & Reporting
Network Automation, and automation in general, is often equated with configuring devices faster, but as you've seen by now, it offers greater predictability and more deterministic outcomes.

On top of that, it also offers even great value when it comes to collecting data and reporting. In these next few tasks, you will use Ansible modules to automate the data collection process and also dynamically generate different types of reports.

Task 1 - Exploring Ansible Core Facts Modules
In the first task, you will use facts modules to gather device information such as OS version, hostname, serial number, neighbors, and IP addresses on the network devices. The modules you will use in this task are all in Ansible core. That means they come with Ansible when you install Ansible.

Each module has the name of <os>_facts.

For IOS devices, the module is ios_facts
For NXOS devices, the module is nxos_facts
For EOS devices, the module is eos_facts
For Junos devices, the module is junos_facts
Remember, you can use the ansible-doc utility on any of these modules to see how to use them and what data will be returned from them.

Step 1
Create a playbook called core-facts.yml with a single task to execute against the iosxe group of devices.

In this task in the play, use the ios_facts module to gather the device facts.

---

  - name: GATHER IOS FACTS
    hosts: iosxe
    connection: network_cli
    gather_facts: no

    tasks:
      - name: GET FACTS
        ios_facts:
Step 2
Execute the playbook.

ntc@ntc-training:ansible$ ansible-playbook -i inventory core-facts.yml

PLAY [GATHER IOS FACTS] ********************************************************

TASK [GET FACTS] ***************************************************************
ok: [csr3]
ok: [csr2]
ok: [csr1]

PLAY RECAP *********************************************************************
csr1                       : ok=1    changed=0    unreachable=0    failed=0
csr2                       : ok=1    changed=0    unreachable=0    failed=0
csr3                       : ok=1    changed=0    unreachable=0    failed=0


The task ran successfully on all three devices, but how do you see the data being collected?

By now you should know there are two options: (1) use verbose mode (running the playbook with -v) and (2) use the register task attribute with the debug module.

Step 3
Re-run the playbook using verbose mode and limit the playbook to just csr1 to make the viewing of the output a little cleaner.

ntc@ntc-training:ansible$ ansible-playbook -i inventory core-facts.yml -v --limit csr1

Using /etc/ansible/ansible.cfg as config file

PLAY [GATHER IOS FACTS] ********************************************************

TASK [GET FACTS] ***************************************************************
ok: [csr1] => {"ansible_facts": {"ansible_net_all_ipv4_addresses": ["10.0.0.51"], "ansible_net_all_ipv6_addresses": [], "ansible_net_filesystems": ["bootflash:"], "ansible_net_gather_subset": ["hardware", "default", "interfaces"], "ansible_net_hostname": "csr1", "ansible_net_image": "bootflash:packages.conf", "ansible_net_interfaces": {"GigabitEthernet1": {"bandwidth": 1000000, "description": null, "duplex": "Full", "ipv4": {"address": "10.0.0.51", "masklen": 24}, "lineprotocol": "up ", "macaddress": "2cc2.6009.d3a8", "mediatype": "RJ45", "mtu": 1500, "operstatus": "up", "type": "CSR vNIC"}, "GigabitEthernet2": {"bandwidth": 1000000, "description": null, "duplex": "Full", "ipv4": null, "lineprotocol": "down ", "macaddress": "2cc2.6049.c853", "mediatype": "RJ45", "mtu": 1500, "operstatus": "administratively down", "type": "CSR vNIC"}, "GigabitEthernet3": {"bandwidth": 1000000, "description": null, "duplex": "Full", "ipv4": null, "lineprotocol": "down ", "macaddress": "2cc2.601b.84ef", "mediatype": "RJ45", "mtu": 1500, "operstatus": "administratively down", "type": "CSR vNIC"}, "GigabitEthernet4": {"bandwidth": 1000000, "description": null, "duplex": "Full", "ipv4": null, "lineprotocol": "down ", "macaddress": "2cc2.605b.754f", "mediatype": "RJ45", "mtu": 1500, "operstatus": "administratively down", "type": "CSR vNIC"}}, "ansible_net_memfree_mb": 327297, "ansible_net_memtotal_mb": 2047264, "ansible_net_model": null, "ansible_net_neighbors": {"Gi1": [{"host": "csr2.ntc.com", "port": "Gi1"}, {"host": "eos-leaf1.ntc.com", "port": "Management1"}, {"host": "csr3.ntc.com", "port": "Gi1"}, {"host": "eos-leaf2.ntc.com", "port": "Management1"}, {"host": "eos-spine2.ntc.com", "port": "Management1"}, {"host": "eos-spine1.ntc.com", "port": "Management1"}]}, "ansible_net_serialnum": "9KXI0D7TVFI", "ansible_net_version": "16.3.1"}, "changed": false, "failed_commands": []}

PLAY RECAP *********************************************************************
csr1                       : ok=1    changed=0    unreachable=0    failed=0


Feel free to run it again on all three devices (without using limit).

Step 4
As you can see using verbose mode doesn't show the data being returned in an easy to read format. Now add the register attribute along with a new task using the debug module to print the facts to the terminal when the playbook runs.

Register the return data and use the variable ntc_ios_facts to do so.

The updated playbook should look like this:

---

  - name: GATHER IOS FACTS
    hosts: iosxe
    connection: network_cli
    gather_facts: no

    tasks:
      - name: GET FACTS
        ios_facts:
        register: ntc_ios_facts

      - debug:
          var: ntc_ios_facts
Step 5
Execute the playbook. This time not using verbose mode, but still limiting it to csr1.

ntc@ntc-training:ansible$ ansible-playbook -i inventory core-facts.yml --limit csr1

PLAY [GATHER IOS FACTS] ********************************************************

TASK [GET FACTS] ***************************************************************
ok: [csr1]

TASK [DEBUG FACTS] *************************************************************
ok: [csr1] => {
    "ntc_ios_facts": {
        "ansible_facts": {
            "ansible_net_all_ipv4_addresses": [
                "10.0.0.51"
            ],
            "ansible_net_all_ipv6_addresses": [],
            "ansible_net_filesystems": [
                "bootflash:"
            ],
            "ansible_net_gather_subset": [
                "hardware",
                "default",
                "interfaces"
            ],
            "ansible_net_hostname": "csr1",
            "ansible_net_image": "bootflash:packages.conf",
            "ansible_net_interfaces": {
                "GigabitEthernet1": {
                    "bandwidth": 1000000,
                    "description": null,
                    "duplex": "Full",
                    "ipv4": {
                        "address": "10.0.0.51",
                        "masklen": 24
                    },
                    "lineprotocol": "up ",
                    "macaddress": "2cc2.6009.d3a8",
                    "mediatype": "RJ45",
                    "mtu": 1500,
                    "operstatus": "up",
                    "type": "CSR vNIC"
                },
                "GigabitEthernet2": {
                    "bandwidth": 1000000,
                    "description": null,
                    "duplex": "Full",
                    "ipv4": null,
                    "lineprotocol": "down ",
                    "macaddress": "2cc2.6049.c853",
                    "mediatype": "RJ45",
                    "mtu": 1500,
                    "operstatus": "administratively down",
                    "type": "CSR vNIC"
                },
                "GigabitEthernet3": {
                    "bandwidth": 1000000,
                    "description": null,
                    "duplex": "Full",
                    "ipv4": null,
                    "lineprotocol": "down ",
                    "macaddress": "2cc2.601b.84ef",
                    "mediatype": "RJ45",
                    "mtu": 1500,
                    "operstatus": "administratively down",
                    "type": "CSR vNIC"
                },
                "GigabitEthernet4": {
                    "bandwidth": 1000000,
                    "description": null,
                    "duplex": "Full",
                    "ipv4": null,
                    "lineprotocol": "down ",
                    "macaddress": "2cc2.605b.754f",
                    "mediatype": "RJ45",
                    "mtu": 1500,
                    "operstatus": "administratively down",
                    "type": "CSR vNIC"
                }
            },
            "ansible_net_memfree_mb": 327363,
            "ansible_net_memtotal_mb": 2047264,
            "ansible_net_model": null,
            "ansible_net_neighbors": {
                "Gi1": [
                    {
                        "host": "csr2.ntc.com",
                        "port": "Gi1"
                    },
                    {
                        "host": "eos-leaf1.ntc.com",
                        "port": "Management1"
                    },
                    {
                        "host": "csr3.ntc.com",
                        "port": "Gi1"
                    },
                    {
                        "host": "eos-leaf2.ntc.com",
                        "port": "Management1"
                    },
                    {
                        "host": "eos-spine2.ntc.com",
                        "port": "Management1"
                    },
                    {
                        "host": "eos-spine1.ntc.com",
                        "port": "Management1"
                    }
                ]
            },
            "ansible_net_serialnum": "9KXI0D7TVFI",
            "ansible_net_version": "16.3.1"
        },
        "changed": false,
        "failed_commands": []
    }
}

PLAY RECAP *********************************************************************
csr1                       : ok=2    changed=0    unreachable=0    failed=0


Feel free to run it again on all three devices.

Step 6
Add a new task to just print (debug) the operating system (ansible_net_version) of the network devices.

This is the new task that should be added:

      - name: DEBUG OS VERSION
        debug:
          var: ntc_ios_facts['ansible_facts']['ansible_net_version']
Step 7
Execute the playbook.

The output for the new task will look like this:

TASK [DEBUG OS VERSION] ********************************************************
ok: [csr1] => {
    "ntc_ios_facts['ansible_facts']['ansible_net_version']": "17.01.01"
}


Step 8
Add a new task to print (debug) the operating system of the network devices, but do NOT use the registered variable.

This is often very confusing when just learning Ansible, but any key inside ansible_facts can be accessed directly. Let's try it.

Add the following task:

      - name: DEBUG SHORTHAND OS VERSION
        debug:
          var: ansible_net_version
Step 9
Execute the playbook limiting the run to just csr1.

The associated new output for the playbook is the following:

TASK [DEBUG OS VERSION] ********************************************************
ok: [csr1] => {
    "ntc_ios_facts['ansible_facts']['ansible_net_version']": "17.01.01"
}

TASK [DEBUG SHORTHAND OS VERSION] **********************************************
ok: [csr1] => {
    "ansible_net_version": "17.01.01"
}

Note: While you can access facts directly, using the register/debug combination provides an easy way to see exactly what's being collected in that specific task.

Step 10
Repeat Steps 1 - 9 for each device type you've been using in the labs.

Add a new play for each one. Tag each play accordingly so you can run them individually.

IMPORTANT

Note: Ensure LLDP is enabled on the NXOS switches using the feature lldp. Unfortunately, LLDP configurations do not persist through a reboot on virtual Nexus switches :(.

If you don't run the playbook, here are the commands to run on nxos-spine1 and nxos-spine2:

config t
feature lldp
end
exit
Status Check

This is a sample playbook for running against all 4 device types (IOS, NXOS, JUNOS, EOS):

---

  - name: GATHER IOS FACTS
    hosts: iosxe
    connection: network_cli
    gather_facts: no
    tags: ios

    tasks:
      - name: GET FACTS
        ios_facts:
        register: ntc_ios_facts

      - name: DEBUG FACTS
        debug:
          var: ntc_ios_facts

      - name: DEBUG OS VERSION
        debug:
          var: ntc_ios_facts['ansible_facts']['ansible_net_version']

      - name: DEBUG SHORTHAND OS VERSION
        debug:
          var: ansible_net_version

  - name: GATHER NXOS FACTS
    hosts: nxos
    connection: network_cli
    gather_facts: no
    tags: nxos

    tasks:
      - name: GET NXOS FACTS
        nxos_facts:
        register: ntc_nxos_facts

      - name: DEBUG FACTS
        debug:
          var: ntc_nxos_facts

      - name: DEBUG OS VERSION
        debug:
          var: ntc_nxos_facts['ansible_facts']['ansible_net_version']

      - name: DEBUG SHORTHAND OS VERSION
        debug:
          var: ansible_net_version

  - name: GATHER EOS FACTS
    hosts: eos
    connection: network_cli
    gather_facts: no
    tags: eos

    tasks:
      - name: GET EOS FACTS
        eos_facts:
        register: ntc_eos_facts

      - name: DEBUG FACTS
        debug:
          var: ntc_eos_facts

      - name: DEBUG OS VERSION
        debug:
          var: ntc_eos_facts['ansible_facts']['ansible_net_version']

      - name: DEBUG SHORTHAND OS VERSION
        debug:
          var: ansible_net_version

  - name: GATHER JUNOS FACTS
    hosts: vmx
    connection: netconf
    gather_facts: no
    tags: junos

    tasks:
      - name: GET FACTS
        junos_facts:
        register: ntc_junos_facts

      - name: DEBUG FACTS
        debug:
          var: ntc_junos_facts

      - name: DEBUG OS VERSION
        debug:
          var: ntc_junos_facts['ansible_facts']['ansible_net_version']

      - name: DEBUG SHORTHAND OS VERSION
        debug:
          var: ansible_net_version
Task 2 - Creating Automated Documentation and Reports
In the previous task, you looked at exploring the core facts modules that specifically perform data collection. You saw that all modules including facts modules return data; this data is JSON, and can be viewed running the playbook in verbose mode.

Now we will look at using and consuming this data to create dynamic reports and documentation.

Step 1
Create a new playbook called reports.yml. Create a play that requires the directories that are required to store the reports. This will eliminate you from using mkdir on the command line.

---

  - name: CREATE DIRECTORIES
    hosts: localhost
    connection: local
    gather_facts: no
    tags: directories

    tasks:

      - file:
          path: ./docs/csv/
          state: directory

      - file:
          path: ./docs/text/
          state: directory
Save and execute the playbook

Step 2
Our goal is to create the required Jinja2 templates to create reports that look like this for every device:

Text Report:

Hostname:      csr3
Vendor:        cisco
Model:         UNKNOWN
OS Version:    17.01.01
Serial Number:  9KIBQAQ3OPE
CSV Report:

csr3,cisco,UNKNOWN,17.01.01,9KIBQAQ3OPE
Create two new templates and save them in the templates directory: facts-text.j2 and facts-csv.j2.

facts-text.j2:

Hostname:      {{ ansible_net_hostname }}
Vendor:        {{ ntc_vendor }}
Model:         {{ ansible_net_model or "UNKNOWN" }}
OS Version:    {{ ansible_net_version }}
Serial Number:  {{ ansible_net_serialnum or "UNKNOWN" }}

facts-csv.j2:

{{ ansible_net_hostname }},{{ ntc_vendor }},{{ ansible_net_model or "UNKNOWN" }},{{ ansible_net_version }},{{ ansible_net_serialnum or "UNKNOWN" }}
Step 3
Add a new play to create reports for each IOS device (for both report types).

  - name: GATHER IOS FACTS
    hosts: iosxe
    connection: network_cli
    gather_facts: no
    tags: ios

    tasks:
      - name: GET FACTS
        ios_facts:

      - name: DUMP FACTS INTO TEXT FILE
        template:
          src: facts-text.j2
          dest: ./docs/text/{{ inventory_hostname }}.md

      - name: DUMP FACTS INTO CSV FILE
        template:
          src: facts-csv.j2
          dest: ./docs/csv/{{ inventory_hostname }}.csv
Step 4
Execute the playbook.

View all files that have been created.

Step 5
Create a 3rd play that will "assemble" all files in each respective directory and create a master report.

Note that this is running on localhost so it runs just once.

  - name: FINAL TASK
    hosts: localhost
    connection: local
    gather_facts: no
    tags: assemble

    tasks:

        - name: CREATE MASTER TEXT REPORT
          assemble:
            src: ./docs/text/
            dest: ./docs/master-text.md
            delimiter: "---"

        - name: CREATE MASTER CSV REPORT
          assemble:
            src: ./docs/csv/
            dest: ./docs/master-csv.csv
Step 6
Execute the playbook.

View all files that have been created.

Step 7
There is still one thing missing from the CSV. That is to insert the headers for the CSV.

        - name: INSERT COLUMNS INTO CSV REPORT
          lineinfile:
            path: ./docs/master-csv.csv
            line: "Hostname,Vendor,Model,OS Version,Serial Number"
            insertbefore: BOF
            state: present
This task will go just below the assemble tasks.

Step 8
Execute the playbook.

View both final master reports.

Step 9
Repeat Step 3 for all NXOS, EOS, and JUNOS devices so the master report contains all devices.

Note: The existing FINAL TASK (assemble) must remain the final task, so insert those three new plays just below the IOS play.

Step 10
Execute the playbook.

The final playbook should look like this:

---

  - name: CREATE DIRECTORIES
    hosts: localhost
    connection: local
    gather_facts: no
    tags: directories

    tasks:

      - file:
          path: ./docs/csv/
          state: directory

      - file:
          path: ./docs/text/
          state: directory

  - name: GATHER IOS FACTS
    hosts: iosxe
    connection: network_cli
    gather_facts: no
    tags: ios

    tasks:
      - name: GET FACTS
        ios_facts:

      - name: DUMP FACTS INTO TEXT FILE
        template:
          src: facts-text.j2
          dest: ./docs/text/{{ inventory_hostname }}.md

      - name: DUMP FACTS INTO CSV FILE
        template:
          src: facts-csv.j2
          dest: ./docs/csv/{{ inventory_hostname }}.csv


  - name: GATHER NXOS FACTS
    hosts: nxos
    connection: network_cli
    gather_facts: no
    tags: nxos

    tasks:
      - name: GET NXOS FACTS
        nxos_facts:

      - name: DUMP FACTS INTO FILE
        template:
          src: facts-text.j2
          dest: ./docs/text/{{ inventory_hostname }}.md

      - name: DUMP FACTS INTO FILE
        template:
          src: facts-csv.j2
          dest: ./docs/csv/{{ inventory_hostname }}.csv


  - name: GATHER EOS FACTS
    hosts: eos
    connection: network_cli
    gather_facts: no
    tags: eos

    tasks:
      - name: GET EOS FACTS
        eos_facts:

      - name: DUMP FACTS INTO FILE
        template:
          src: facts-text.j2
          dest: ./docs/text/{{ inventory_hostname }}.md

      - name: DUMP FACTS INTO FILE
        template:
          src: facts-csv.j2
          dest: ./docs/csv/{{ inventory_hostname }}.csv

  - name: GATHER JUNOS FACTS
    hosts: vmx
    connection: netconf
    gather_facts: no
    tags: junos

    tasks:
      - name: GET FACTS
        junos_facts:

      - name: DUMP FACTS INTO FILE
        template:
          src: facts-text.j2
          dest: ./docs/text/{{ inventory_hostname }}.md

      - name: DUMP FACTS INTO FILE
        template:
          src: facts-csv.j2
          dest: ./docs/csv/{{ inventory_hostname }}.csv

  - name: FINAL TASK
    hosts: localhost
    connection: local
    gather_facts: no
    tags: assemble

    tasks:

        - name: CREATE MASTER TEXT REPORT
          assemble:
            src: ./docs/text/
            dest: ./docs/master-text.md
            delimiter: "---"

        - name: CREATE MASTER CSV REPORT
          assemble:
            src: ./docs/csv/
            dest: ./docs/master-csv.csv

        - name: INSERT COLUMNS INTO CSV REPORT
          lineinfile:
            path: ./docs/master-csv.csv
            line: "Hostname,Vendor,Model,OS Version,Serial Number"
            insertbefore: BOF
            state: present
The master CSV report generated will look like this:

ntc@ntc-training:ansible$ cat docs/master-csv.csv
Hostname,Vendor,Model,OS Version,Serial Number
csr1,cisco,UNKNOWN,17.01.01,9KIBQAQ3OPE
csr2,cisco,UNKNOWN,17.01.01,9KIBQAQ3OPE
csr3,cisco,UNKNOWN,17.01.01,9KIBQAQ3OPE
eos-leaf1,arista,vEOS,4.20.0F-7058194.bloomingtonrel (engineering build),UNKNOWN
eos-leaf2,arista,vEOS,4.20.0F-7058194.bloomingtonrel (engineering build),UNKNOWN
eos-spine1,arista,vEOS,4.20.0F-7058194.bloomingtonrel (engineering build),UNKNOWN
eos-spine2,arista,vEOS,4.20.0F-7058194.bloomingtonrel (engineering build),UNKNOWN
nxos-spine1,cisco,NX-OSv Chassis,7.3(1)D1(1) [build 7.3(1)D1(0.10)],TM602622D6B
nxos-spine2,cisco,NX-OSv Chassis,7.3(1)D1(1) [build 7.3(1)D1(0.10)],TM604B14E3B
vmx1,juniper,vmx,15.1F4.15,VMX2c
vmx2,juniper,vmx,15.1F4.15,VMX63
vmx3,juniper,vmx,15.1F4.15,VMX39
ntc@ntc-training:ansible$
And the final text report will look like this:

ntc@ntc-training:ansible$ cat docs/master-text.md
Hostname:      csr1
Vendor:        cisco
Model:         UNKNOWN
OS Version:    17.01.01
Serial Number:  9KIBQAQ3OPE
---
Hostname:      csr2
Vendor:        cisco
Model:         UNKNOWN
OS Version:    17.01.01
Serial Number:  9KIBQAQ3OPE
---
Hostname:      csr3
Vendor:        cisco
Model:         UNKNOWN
OS Version:    17.01.01
Serial Number:  9KIBQAQ3OPE
---
Hostname:      eos-leaf1
Vendor:        arista
Model:         vEOS
OS Version:    4.20.0F-7058194.bloomingtonrel (engineering build)
Serial Number:  UNKNOWN
---
Hostname:      eos-leaf2
Vendor:        arista
Model:         vEOS
OS Version:    4.20.0F-7058194.bloomingtonrel (engineering build)
Serial Number:  UNKNOWN
---
Hostname:      eos-spine1
Vendor:        arista
Model:         vEOS
OS Version:    4.20.0F-7058194.bloomingtonrel (engineering build)
Serial Number:  UNKNOWN
---
Hostname:      eos-spine2
Vendor:        arista
Model:         vEOS
OS Version:    4.20.0F-7058194.bloomingtonrel (engineering build)
Serial Number:  UNKNOWN
---
Hostname:      nxos-spine1
Vendor:        cisco
Model:         NX-OSv Chassis
OS Version:    7.3(1)D1(1) [build 7.3(1)D1(0.10)]
Serial Number:  TM602622D6B
---
Hostname:      nxos-spine2
Vendor:        cisco
Model:         NX-OSv Chassis
OS Version:    7.3(1)D1(1) [build 7.3(1)D1(0.10)]
Serial Number:  TM604B14E3B
---
Hostname:      vmx1
Vendor:        juniper
Model:         vmx
OS Version:    15.1F4.15
Serial Number:  VMX2c
---
Hostname:      vmx2
Vendor:        juniper
Model:         vmx
OS Version:    15.1F4.15
Serial Number:  VMX63
---
Hostname:      vmx3
Vendor:        juniper
Model:         vmx
OS Version:    15.1F4.15
Serial Number:  VMX39
ntc@ntc-training:ansible$

    ####################################################################################################
    ####################################  LAB 18 SNMP Ansible Roles  ###################################
    ####################################################################################################

Lab 18 - SNMP Ansible Roles
Task 1 - Multi-Platform SNMP Role
In this task, you will learn how to create re-usable tasks called roles.
You will create a role for configuring SNMP communities on both IOS and NXOS.

Step 1
In order to create a new role, you need a roles sub-directory.
Create a roles directory within the ansible directory.

Now we need a directory that is equal to the role name.
Our role name is snmp, so now create a sub-directory called snmp within the roles directory.

Step 2
In the snmp dir, create a new dir called tasks. Within tasks, create a file called main.yml.

This is a REQUIRED file within a file. This is where tasks begin to execute within a role.

In the main.yml, add the following statement:

---

- include_tasks: "{{ ansible_network_os }}_deploy.yml"
Notice how it's a single include statement. This will execute a file called nxos_deploy.yml or ios_deploy.yml.

Those files need to be created now, but will configure SNMP per OS type.

Step 3
Create two new files in the tasks sub-directory called nxos_deploy.yml and ios_deploy.yml.

It should look like this:

.
├── roles
│   ├── snmp
│   │   └── tasks
│   │     ├── ios_deploy.yml
│   │     ├── main.yml
│   │     └── nxos_deploy.yml
Step 4
Open the nxos_deploy.yml file.

Use the Ansible nxos_config module to configure SNMP community strings.

---

- name: ENSURE SNMP COMMUNITIES EXIST IN NXOS
  nxos_config:
    commands:
      - "snmp-server community {{ item.community }} group {{ item.group }}"
  loop: "{{ snmp_communities }}"
Note: Here we are using a variable called snmp_communities which will be passed by the main playbook executing the role.

Step 5
Just like in the last task, open the ios_deploy.yml file and use Ansible ios_config module to configure SNMP community strings.

---

- name: ENSURE SNMP COMMUNITIES EXIST IN IOS
  ios_config:
    commands:
      - "snmp-server community {{ item.community }} {{ item.group }}"
  loop: "{{ snmp_communities }}"
Step 6
Finally, we need to create a playbook to actually use this new role.

Create a new playbook called snmp-role-pb.yml in your ansible directory.

This playbook won't have any direct tasks per se, rather it will call the "snmp" role and execute the tasks within the role.

Notice you can also select two groups from the inventory file using the following line: hosts: iosxe,nxos.

---

  - name: MULTI-PLATFORM SNMP
    hosts: iosxe,nxos
    connection: network_cli
    gather_facts: no

    roles:
      - role: snmp
        snmp_communities:
          - community: ntc-public
            group: network-operator
          - community: ntc-private
            group: network-admin
Notice now as the playbook user, you no longer need to be aware of which tasks are actually performing the change or which vendor device is used as that's all taken care of within the role.

Step 7
Save and run the playbook.

You will see the output below.

ntc@ntc-training:ansible$ ansible-playbook -i inventory snmp-role-pb.yml
PLAY [MULTI-PLATFORM SNMP] *****************************************************

TASK [snmp : include] **********************************************************
included: /home/ntc/ansible/roles/snmp/tasks/ios_deploy.yml for csr1, csr2, csr3
included: /home/ntc/ansible/roles/snmp/tasks/nxos_deploy.yml for nxos-spine1, nxos-spine2

TASK [snmp : ENSURE SNMP COMMUNITIES EXIST IN IOS] *****************************
changed: [csr3] => (item={u'group': u'network-operator', u'community': u'ntc-public'})
changed: [csr2] => (item={u'group': u'network-operator', u'community': u'ntc-public'})
changed: [csr1] => (item={u'group': u'network-operator', u'community': u'ntc-public'})
changed: [csr2] => (item={u'group': u'network-admin', u'community': u'ntc-private'})
changed: [csr3] => (item={u'group': u'network-admin', u'community': u'ntc-private'})
changed: [csr1] => (item={u'group': u'network-admin', u'community': u'ntc-private'})

TASK [snmp : ENSURE SNMP COMMUNITIES EXIST IN NXOS] ****************************
changed: [nxos-spine2] => (item={u'group': u'network-operator', u'community': u'ntc-public'})
changed: [nxos-spine1] => (item={u'group': u'network-operator', u'community': u'ntc-public'})
changed: [nxos-spine2] => (item={u'group': u'network-admin', u'community': u'ntc-private'})
changed: [nxos-spine1] => (item={u'group': u'network-admin', u'community': u'ntc-private'})

PLAY RECAP *********************************************************************
csr1                       : ok=2    changed=1    unreachable=0    failed=0
csr2                       : ok=2    changed=1    unreachable=0    failed=0
csr3                       : ok=2    changed=1    unreachable=0    failed=0
nxos-spine1                : ok=2    changed=1    unreachable=0    failed=0
nxos-spine2                : ok=2    changed=1    unreachable=0    failed=0

As you can see this is a very powerful concept and allows for the re-use of tasks. You could have had each task in the role in the playbook, but now next time you need to update community strings, you can easily call this role.

    ####################################################################################################
    #########################  LAB 19 Backing Up Configs With NTC (3rd Party)  #########################
    ####################################################################################################

Lab 19 - Backup and Restore Network Configurations Part 1
Before starting the lab we are going to go over how to add 3rd party modules to your Ansible environment. This could include open source modules or custom modules you decide to write over time.

Below are some tips on how to do it, but for this lab environment it has already been added so we don't have to apply any changes. This first Task is read-only.

Task 1 - Adding 3rd Party Modules (READ-ONLY)
Step 1
You need to perform two steps to start using 3rd party modules.

Ensure the modules you want to use (usually a repository that has been cloned) is in your Ansible module search path
Install any dependencies required by the modules (usually Python modules or packages installable via pip)
Issue the command ansible --version. This will give us a wealth of information about our Ansible environment.

ntc@ntc-training:~$ ansible --version
ansible 2.9.9
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/etc/ntc/ansible/library']
  ansible python module location = /usr/local/lib/python3.6/site-packages/ansible
  executable location = /usr/local/bin/ansible
  python version = 3.6.8 (default, Jun 11 2019, 01:16:11) [GCC 6.3.0 20170516]
You can note our configured module search path as /etc/ntc/ansible/library. Ansible will recursively search for modules in that path now.

If you have a "default" or No search path shown, open the config file that is shown in the output above, in this example we have /etc/ansible/ansible.cfg. In that file, you'll see these first few lines:

  [defaults]

  # some basic default values...

  inventory      = /etc/ansible/hosts
  library        = ADD PATH HERE
Step 2
Add a path for library - this will become your search path. Validate it with ansible --version after you make the change. If you would like to add an additional path use : to add another path to the list.

[defaults]

# some basic default values...

inventory      = /etc/ansible/hosts
library        = /home/ntc/projects/:/etc/ntc/ansible/library
Save and exit the file.

ntc@ntc-training:~$ ansible --version
ansible 2.9.9
  config file = /etc/ansible/ansible.cfg
  configured module search path = ['/home/ntc/projects', '/etc/ntc/ansible/library']
  ansible python module location = /usr/local/lib/python3.6/site-packages/ansible
  executable location = /usr/local/bin/ansible
  python version = 3.6.8 (default, Jun 11 2019, 01:16:11) [GCC 6.3.0 20170516]
Step 3
You can now just git clone any git project that has modules inside your configured search path.

It's recommended to follow the 3rd party module instructions to make sure it has met its dependencies requirements. What's important after the install is to make sure the libraries are in placed in where we have configured configured module search path = [u'/etc/ntc/ansible/library', u'/home/ntc/projects'] of the ansible.cfg file. Remember, you will need to ensure any Python dependencies are met too, e.g. pip install $package.
For the course, we have a number of repositories cloned that contain 3rd party open source Ansible modules:

ntc@ntc-training:~$ ls /etc/ntc/ansible/library/
ansible-junos-stdlib  ansible-pan  ansible-snmp  napalm  napalm-ansible  ntc-ansible
ntc@ntc-training:~$
Each one of these also required Python packages to be installed via pip including: pyntc, napalm, ntc_templates, nelsnmp just to name a few.

Task 2 - Backup Configurations
This lab will show how to use Ansible to manage network device configurations and focuses on the process of backing up and re-storing full configuration files.

We'll use two main modules to do this: one that is used to backup the configurations (ntc_show_command) in this lab and another that is used to deploy the configurations (NAPALM) in the next lab.

In this task, you will save and backup the current running configuration of all of your devices.

Step 1
Within the ansible directory, create a new directory called backups.

ntc@ntc-training:ansible$ mkdir backups
ntc@ntc-training:ansible$
Note: you could also do this with the file module if you'd like so it's fully automated!

Additionally, in the same ansible directory, create a playbook called backup.yml

ntc@ntc-training:ansible$ touch backup.yml
ntc@ntc-training:ansible$
Step 2
Open the newly created playbook in your text editor.

Create a play that'll be executed against all hosts defined in the inventory file.

---

  - name: BACKUP CONFIGURATIONS
    hosts: all
    connection: local
    gather_facts: no

Note: most 3rd party modules use connection: local because the actual connection setup happens in the Python code within the module or dependencies for that module.

Step 3
Add a variable in your playbook called backup_command. It should be a dictionary that contains 4 key-value pairs. The keys should map to an OS and the value should be the command required to gather the existing running configuration.

---

  - name: BACKUP CONFIGURATIONS
    hosts: all
    connection: local
    gather_facts: no

    vars:
      backup_command:
        eos: show run
        ios: show run
        nxos: show run
        junos: show configuration
By making an object like this, it'll allow us to use a single task to backup all configuration instead of needing a task/play per OS!

Step 4
Since we're using a 3rd party module, credentials and connection properties are handled a little differently. We need to pass them into the module.

Add a variable to handle the login to the devices. Often referred to as a provider variable, this is a dictionary that can be passed to the provider parameter of the ntc and napalm modules.

---

  - name: BACKUP CONFIGURATIONS
    hosts: all
    connection: local
    gather_facts: no

    vars:
      backup_command:
        eos: show run
        ios: show run
        nxos: show run
        junos: show configuration
      connection_details:
        username: "{{ ansible_user }}"
        password: "{{ ansible_ssh_pass }}"
        host: "{{ inventory_hostname }}"

Step 5
Add a task to backup the running configuration using the module called ntc_show_command.

Create a backups directory.

All backup files should be saved locally inside the backups directory.

---

  - name: BACKUP CONFIGURATIONS
    hosts: all
    connection: local
    gather_facts: no

    vars:
      backup_command:
        eos: show run
        ios: show run
        nxos: show run
        junos: show configuration
      connection_details:
        username: "{{ ansible_user }}"
        password: "{{ ansible_ssh_pass }}"
        host: "{{ inventory_hostname }}"

    tasks:

      - name: BACKUP CONFIGS FOR ALL DEVICES
        ntc_show_command:
          provider: "{{ connection_details }}"
          command: "{{ backup_command[ansible_network_os] }}"
          local_file: "./backups/{{ inventory_hostname }}.cfg"
          platform: "{{ ntc_vendor }}_{{ ansible_network_os }}"
          
Pay attention to how we are using variables for the platform parameter.

Supported platforms for this module actually matches anything Netmiko, a popular Python-based SSH library, supports, e.g. vendor_os like cisco_ios, cisco_nxos, juniper_junos, arista_eos, etc. Since we have those variables pre-built in our inventory file, we can use them as defined in the output above.

Save and execute the playbook.

ntc@ntc-training:ansible$ ansible-playbook -i inventory backup.yml
You will see the following output during execution (this output doesn't include Nexus):

ntc@ntc-training:ansible$ ansible-playbook -i inventory backup.yml

PLAY [BACKUP] *************************************************************************************************

TASK [BACKUP CONFIGS] *****************************************************************************************
ok: [vmx1]
ok: [eos-spine2]
ok: [eos-leaf1]
ok: [eos-leaf2]
ok: [eos-spine1]
ok: [vmx2]
ok: [vmx3]
ok: [nxos-spine1]
ok: [nxos-spine2]
ok: [csr1]
ok: [csr2]
ok: [csr3]

PLAY RECAP ****************************************************************************************************
csr1                       : ok=1    changed=0    unreachable=0    failed=0   
csr2                       : ok=1    changed=0    unreachable=0    failed=0   
csr3                       : ok=1    changed=0    unreachable=0    failed=0   
eos-leaf1                  : ok=1    changed=0    unreachable=0    failed=0   
eos-leaf2                  : ok=1    changed=0    unreachable=0    failed=0   
eos-spine1                 : ok=1    changed=0    unreachable=0    failed=0   
eos-spine2                 : ok=1    changed=0    unreachable=0    failed=0   
nxos-spine1                : ok=1    changed=0    unreachable=0    failed=0   
nxos-spine2                : ok=1    changed=0    unreachable=0    failed=0   
vmx1                       : ok=1    changed=0    unreachable=0    failed=0   
vmx2                       : ok=1    changed=0    unreachable=0    failed=0   
vmx3                       : ok=1    changed=0    unreachable=0    failed=0   

ntc@ntc-training:ansible$

Step 6
Move to the backups directory and open the newly created files to verify everything worked as expected.

Pay particular attention to the IOS configurations. In these configurations, you'll see two lines at the top of each including:

Building configuration...
Current configuration : 4043 bytes
These CANNOT be included when we re-deploy them and push full configs back to each device. This is not supported by IOS (you can try copying and pasting a full config from the CLI--you'll see this first hand)

We need an automated way to remove them from each.

Step 7
Add two tasks to cleanup the backup configs. While it's only relevant for IOS configs, there is no harm on running this against all devices.

      # this goes below the existing tasks

      - name: CLEAN UP IOS CONFIGS - LINE 1
        lineinfile:
          dest: ./backups/{{ inventory_hostname }}.cfg
          line: "Building configuration..."
          state: absent
        tags: clean

      - name: CLEAN UP IOS CONFIGS - LINE 2
        lineinfile:
          dest: ./backups/{{ inventory_hostname }}.cfg
          regexp: "Current configuration .*"
          state: absent
        tags: clean
Notice how there are now tags embedded for each of these tasks. This allows us to selectively run just these two tasks without having to run the backup task again.

Step 8
Save the playbook and run it again with the following command.

ntc@ntc-training:ansible$ $ ansible-playbook -i inventory backup.yml --tags=clean

Relevant output:


TASK [CLEAN UP IOS CONFIGS LINE 1] ******************************************************
ok: [vmx1]
ok: [eos-spine1]
ok: [eos-leaf1]
ok: [eos-leaf2]
ok: [eos-spine2]
ok: [vmx2]
changed: [csr2]
ok: [vmx3]
changed: [csr1]
changed: [csr3]

TASK [CLEAN UP IOS CONFIGS LINE 2] ******************************************************
ok: [eos-spine1]
ok: [eos-spine2]
ok: [eos-leaf2]
ok: [eos-leaf1]
ok: [vmx1]
ok: [vmx2]
changed: [csr1]
ok: [vmx3]
changed: [csr3]
changed: [csr2]
Open one or more of the new configuration files and take a look at them and notice how those lines are gone from the files.

Step 9
At the top of your playbook are two variables: backup_command and connection_details. It's not great practice to keep variables hard-coded in your playbook as you cannot re-use them in other playbooks or areas of your project.

Re-locate both of these variables to group_vars/all.yml.

The final updated playbook should look like this:

---

  - name: BACKUP CONFIGURATIONS
    hosts: all
    connection: local
    gather_facts: no

    tasks:

      - name: BACKUP CONFIGS FOR ALL DEVICES
        ntc_show_command:
          provider: "{{ connection_details }}"
          command: "{{ backup_command[ansible_network_os] }}"
          local_file: "./backups/{{ inventory_hostname }}.cfg"
          platform: "{{ ntc_vendor }}_{{ ansible_network_os }}"

      - name: CLEAN UP IOS CONFIGS - LINE 1
        lineinfile:
          dest: ./backups/{{ inventory_hostname }}.cfg
          line: "Building configuration..."
          state: absent
        tags: clean

      - name: CLEAN UP IOS CONFIGS - LINE 2
        lineinfile:
          dest: ./backups/{{ inventory_hostname }}.cfg
          regexp: "Current configuration .*"
          state: absent
        tags: clean

And group_vars/all.yml should now have both variables:

---

backup_command:
  eos: show run
  ios: show run
  nxos: show run
  junos: show configuration
connection_details:
  username: "{{ ansible_user }}"
  password: "{{ ansible_ssh_pass }}"
  host: "{{ inventory_hostname }}"
Note: in other labs, you've also seen how you can back up configurations using "core" modules. This is just another way while showing how to use 3rd party modules.

    ####################################################################################################
    ########################  LAB 20 Restoring Configs With NAPALM (3rd Party)  ########################
    ####################################################################################################

Lab 20 - Backup and Restore Network Configurations Part 2
This lab will "restore" the configuration files you previously backed up using another 3rd party Ansible module called napalm_install_config that is based off of the popular NAPALM project.

Task 1 - Restore Configuration
Step 1
Create a new playbook called restore.yml. In this file, and for the first execution, limit it to the IOS devices:

---

  - name: DEPLOY & RESTORE CONFIGS
    hosts: iosxe
    connection: local
    gather_facts: no
Step 2
Using napalm_install_config, push back these configurations. Since we didn't change anything from the original backup, the task result should be idempotent i.e. no change should actually occur.

---

  - name: DEPLOY & RESTORE CONFIGS
    hosts: iosxe
    connection: local
    gather_facts: no


    tasks:

      - name: DEPLOY CONFIGURATIONS
        napalm_install_config:
          provider: "{{ connection_details }}"
          config_file: ./backups/{{ inventory_hostname }}.cfg
          replace_config: true
          commit_changes: true
          dev_os: ios
Step 3
Execute this new play:

ntc@ntc-training:ansible$ ansible-playbook -i inventory restore.yml

PLAY [DEPLOY & RESTORE CONFIGS] **********************************************************

TASK [DEPLOY CONFIGURATIONS] ************************************************************
ok: [csr3]
ok: [csr1]
ok: [csr2]

PLAY RECAP *********************************************************************
csr1                       : ok=1    changed=0    unreachable=0    failed=0
csr2                       : ok=1    changed=0    unreachable=0    failed=0
csr3                       : ok=1    changed=0    unreachable=0    failed=0
Notice how there were NO changes. This is because you just pushed exactly what was already on the device.

The full playbook should look like this for now:

---

  - name: DEPLOY & RESTORE CONFIGS
    hosts: iosxe
    connection: local
    gather_facts: no


    tasks:

      - name: DEPLOY CONFIGURATIONS
        napalm_install_config:
          provider: "{{ connection_details }}"
          config_file: ./backups/{{ inventory_hostname }}.cfg
          replace_config: true
          commit_changes: true
          dev_os: ios

Step 4
Update the play definition of the second play to include another group. Choose either the vmx or eos group.

You can add a group in the play definition using the following syntax:

hosts: iosxe,eos
Step 5
Since we are automating more than one group, we need to parametrize the napalm task for the dev_os.

The last line in the playbook is as follows:

dev_os: ios
We need to update this to be the following since we already have the os pre-defined as a group based variable:

dev_os: "{{ ansible_network_os }}"
Step 6
Execute the playbook again:

ntc@ntc-training:ansible$ ansible-playbook -i inventory restore.yml

PLAY [BACKUP] ******************************************************************

PLAY [DEPLOY CONFIGS] **********************************************************

TASK [PUSH CONFIGS] ************************************************************
ok: [csr3]
ok: [csr1]
ok: [csr2]
ok: [eos-spine1]
ok: [eos-spine2]
ok: [eos-leaf1]
ok: [eos-leaf2]

PLAY RECAP *********************************************************************
csr1                       : ok=1    changed=0    unreachable=0    failed=0
csr2                       : ok=1    changed=0    unreachable=0    failed=0
csr3                       : ok=1    changed=0    unreachable=0    failed=0
eos-leaf1                  : ok=1    changed=0    unreachable=0    failed=0
eos-leaf2                  : ok=1    changed=0    unreachable=0    failed=0
eos-spine1                 : ok=1    changed=0    unreachable=0    failed=0
eos-spine2                 : ok=1    changed=0    unreachable=0    failed=0
IMPORTANT NOTE AGAIN:

Even though you are pushing a full configuration, there are NO changes being applied since we are applying the SAME exact configuration that already exists on the device.

Step 7
Open the stored backup configs inside the backups directory and make some changes.

For example, create a new Loopback interface on each IOS device.

Add the following lines on csr1.cfg.

!
interface Loopback10
 description added by Ansible
 ip address 1.1.1.1 255.255.255.0
!
Add the following lines on csr2.cfg.

!
interface Loopback10
 description added by Ansible
 ip address 2.2.2.2 255.255.255.0
!
Add the following lines on csr3.cfg.

!
interface Loopback10
 description added by Ansible
 ip address 3.3.3.3 255.255.255.0
!
Step 8
Update the task for the following:

Save the diffs to a file such that we can see the changes that will get applied
Do not commit the changes since we just want to see the diffs
First, create a new directory called diffs in the ansible directory.

ntc@ntc-training:ansible$ mkdir diffs
ntc@ntc-training:ansible$
This directory will store all diffs that will eventually get applied to the devices.

Step 9
Now update the napalm task with the two required changes.

          commit_changes: false
          diff_file: ./diffs/{{ inventory_hostname }}.diffs
This will ensure the changes are not applied, but we will still get back the diffs on what will be applied on the next commit.

This updated task should look like this:

      - name: DEPLOY CONFIGURATIONS
        napalm_install_config:
          provider: "{{ connection_details }}"
          config_file: ./backups/{{ inventory_hostname }}.cfg
          diff_file: ./diffs/{{ inventory_hostname }}.diffs
          replace_config: true
          commit_changes: false
          dev_os: "{{ ansible_network_os }}"
Step 10
Save and re-run the playbook using the limit flag.

ntc@ntc-training:ansible$ ansible-playbook -i inventory restore.yml --limit iosxe
Notice we added a new flag to the command being used called --limit. Since we added eos in the previous step and only made changes to the CSR routers, we can use limit to limit the scope of this job to just the Cisco IOS CSR devices.

Note how they are now changed. It doesn't mean this made the change, just that diffs are found and would be changed when commit is true.

Step 11
Navigate to the diffs directory and open the diff files.

For example, csr1.diffs will look like this.

+interface Loopback10
 +description Done with Ansible
 +ip address 1.1.1.1 255.255.255.0
Feel free to SSH to the devices to ensure the configs are not yet applied.

Step 12
Update the playbook to commit these new configurations.

Simply update commit_changes to be true.

          commit_changes: true
Step 13
Save and run the playbook.

ntc@ntc-training:ansible$ ansible-playbook -i inventory restore.yml --limit iosxe
SSH to the devices and ensure the configs are applied.

Step 14
Remove a particular configuration from the config files being used and see how there is not any "no" commands being applied. While doing this, set commit_changes=False and view the diffs first before applying.

Step 15
Notice how the playbook has hard-coded the devices to be automated. As you've seen you can modify this manually or use the "limit" flag to limit the execution to a sub-set of devices.

What if you wanted user input as in always forcing the user to pass in the device or group into the playbook on execution? You can do this with "extra vars".

Update your play definition to this:

---

  - name: DEPLOY & RESTORE CONFIGS
    hosts: "{{ device }}"
    connection: local
    gather_facts: no
This will require you to pass in a variable called device when the playbook runs.

Step 16
Re-run the playbook passing in the device variable. You have two options using either the --extra-vars (or the -e flag). Here we show an example using --extra-vars:

ntc@ntc-training:ansible$ ansible-playbook -i inventory restore.yml --extra-vars="device=csr1"

Check
Full and final playbook will look like this:

---

  - name: DEPLOY & RESTORE CONFIGS
    hosts: "{{ device }}"
    connection: local
    gather_facts: no


    tasks:

      - name: DEPLOY CONFIGURATIONS
        napalm_install_config:
          provider: "{{ connection_details }}"
          config_file: ./backups/{{ inventory_hostname }}.cfg
          diff_file: ./diffs/{{ inventory_hostname }}.diffs
          replace_config: true
          commit_changes: true
          dev_os: "{{ ansible_network_os }}"

    ####################################################################################################
    ########################  LAB 20 Restoring Configs With NAPALM (3rd Party)  ########################
    ####################################################################################################