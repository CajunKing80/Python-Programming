######################################################
############ Lesson 32 Reading CSV Files #############
######################################################

import csv

with open ('filename.csv', 'r') as file: 
    reader = csv.reader(file) # create a comma separated file within the same directory to test this lesson of code
    for row in reader:
        print(row[1])

######################################################
############ Lesson 33 Writing CSV Files #############
######################################################      

import csv

with open ('filename.csv', 'a') as csvfile: 
    writer = csv.writer(csvfile)
    csvdata = (5, 'Anne', 'Amsterdam')
    writer.writerow(csvdata)

with open ('filename.csv', 'w') as file: # add additional argument of newline='' to remove default lines between data lines
    writer = csv.writer(file)
    writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
    for x in range (1,101):
        writer.writerow([x, x**2, x**3, x**4])

######################################################
####### Lesson 34 Using CSV Custom Dilimeters ########
######################################################

import csv

with open ('filename.csv', 'r') as f:
    reader = csv.reader (f, delimiter = ':', lineterminator = '\n')
    for row in reader:
        print(row)

######################################################
############ Lesson 35 Using CSV Dialects ############
######################################################

import csv

with open ('filename.csv', 'r') as f:
    reader = csv.reader (f, delimiter = ':', lineterminator = '\n')
    for row in reader:
        print(row)

print(csv.list_dialects())

csv.register_dialect ('hashes', delimeter = '#', quoting = csv.QUOTE_NONE, lineterminator = '\n')

with open ('filename', 'r') as csvfile:
    reader = csv.reader (csvfile, dialect = 'hashes')
    for row in reader: 
        print (row)

with open ('filename', 'a') as csvfile: 
    writer = csv.writer (dialect = 'hashes')
    writer.writerow(('spoon', 3, 1.5))
    print (row)

######################################################
############ Lesson 38 Assignment Answer 1 ###########
######################################################

with open ('filename', 'r') as file: 
    devices = f.read().splitlines()
    print(devices)

myList = ()

for item in devices: 
    tmp = item.split(':')
    print (tmp)
    myList.append(tmp)

print (tmp)

######################################################
############ Lesson 39 Assignment Answer 2 ###########
######################################################

import csv

with open ('filename') as file: 
    reader = csv.reader (file, delimeter = ':')
    myList = list()
    for row in reader: 
        print (row)
        myList.append(row)

print (myList)

