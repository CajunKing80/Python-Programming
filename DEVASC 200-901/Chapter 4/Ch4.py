# ===============================================================================================================================================================================================
# ===============================================================================================================================================================================================

# Define PYTHON FUNCTIONS

# def devnet():
#     print ('Simple Function')

# devnet()

# print (max(50, 100, 5, 77, 101)) #Built-In function

# def sub (arg1, arg2):
#     result = arg1 - arg2
#     print (result)

# sub (10, 15)

# def hello(*args):
#     for arg in args: 
#         print ('Hello ', arg, "!")

# hello ('RJ', 'Caleb', 'Mason')

# def hello (**kwargs):
#     for key, value in kwargs.items():
#         print ('Hello', value, "!")

# hello (kwarg1='RJ', kwarg2='Caleb', kwarg3='Mason')

# ===============================================================================================================================================================================================
# ===============================================================================================================================================================================================

# Define PYTHON CLASSES

# CLASSES

# class Router:
    # pass is an empty placeholder to define the class for assigning attributes later!
    
    # Router Class
#     def __init__ (self, model, swversion, ip_add):
   
#         #I nitialize the variables
#         self.model = model
#         self.swversion = swversion
#         self.ip_add = ip_add

# rtr1 = Router ('iosV', '15.6.7', '10.10.10.1')
# print(rtr1.model)
# print(rtr1.swversion)
# print(rtr1.ip_add)

# rtr1 = Router ('isr4221', '16.9.5', '10.10.10.5')
# print(rtr1.model)
# print(rtr1.swversion)
# print(rtr1.ip_add)

# METHODS

# class Router:
#     """Router Class"""
#     def __init__ (self, model, swversion, ip_add):
#         self.model = model
#         self.swversion = swversion
#         self.ip_add = ip_add

#     def getdesc(self): #METHOD
#         """return a formatted description of the router"""
#         desc = f'Router Model              :{self.model}\n'\
#                f'Software Version          :{self.swversion}\n'\
#                f'Router Management Address :{self.ip_add}'
#         return desc

# rtr1 = Router ('iosV', '15.6.7', '10.10.10.1')
# rtr2 = Router ('isr4221', '16.9.5', '10.10.10.5')

# print ('Rtr1\n', rtr1.getdesc(), '\n', sep='') #Call the getdesc() method to the print function to display the Router class info for rtr1, formatted to Rtr1
# print ('Rtr2\n', rtr2.getdesc(), sep='')

# INHERITANCE

# class Router:
#     '''Router Class'''
#     def __init__ (self, model, swversion, ip_add):
#         self.model = model
#         self.swversion = swversion
#         self.ip_add = ip_add

#     def getdesc(self):
#         '''return a formatted description of the router'''
#         desc = f'Router Model              :{self.model}\n'\
#                f'Software Version          :{self.swversion}\n'\
#                f'Router Management Address :{self.ip_add}'
#         return desc

# class Switch(Router):
#     def getdesc(self):
#         '''return a formatted description of the switch'''
#         desc = f'Switch Model              :{self.model}\n'\
#                f'Software Version          :{self.swversion}\n'\
#                f'Switch Management Address :{self.ip_add}'
#         return desc 

# rtr1 = Router ('iosV', '15.6.7', '10.10.10.1')
# rtr2 = Router ('isr4221', '16.9.5', '10.10.10.5')
# sw1 = Switch ('Cat9300', '16.9.5', '10.10.10.8')

# print ('Rtr1\n', rtr1.getdesc(), '\n', sep='')
# print ('Rtr2\n', rtr2.getdesc(), '\n', sep='')
# print ('Sw1\n', sw1.getdesc(), '\n', sep='')

# ===============================================================================================================================================================================================
# ===============================================================================================================================================================================================

# PYTHON MODULES

# import math 
# print(dir(math))
# help(math)
# help(math.sqrt)
# print (int(math.sqrt(81)))
# print (math.sqrt(81))
# from math import sqrt, tan
# print(sqrt(100))

# import calendar as cal
# print (cal.month(2021, 9, 9, 1))

# Creating and importing your own Python modules
    #Save the Class blocks from above into the same directory and name {device.py}
    #import the individual methods from that class

# from device import Router, Switch

# rtr1 = Router ('iosV', '15.6.7', '10.10.10.1')
# rtr2 = Router ('isr4221', '16.9.5', '10.10.10.5')
# sw1 = Switch ('Cat9300', '16.9.5', '10.10.10.8')

# print ('Rtr1\n', rtr1.getdesc(), '\n', sep='')
# print ('Rtr2\n', rtr2.getdesc(), '\n', sep='')
# print ('Sw1\n', sw1.getdesc(), '\n', sep='')

# ===============================================================================================================================================================================================
# ===============================================================================================================================================================================================