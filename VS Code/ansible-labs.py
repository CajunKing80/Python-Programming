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

