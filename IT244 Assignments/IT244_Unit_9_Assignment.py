
#UNIT 9 ASSIGNMENT

#Import required modules
import csv
import pickle

#Create a list to pickle the 2 data files

SCATData = []

#Open the first file
f = open('IT244_Unit_9_SCATData1.csv ')
csv_file = csv.reader(f)

#Append the records lists by columns
for column in csv_file:
    SCATData.append(column[0])
    SCATData.append(column[1])
f.close()

#Open the second file
f = open('IT244_Unit_9_SCATData2.csv ')
csv_file = csv.reader(f)

#Append the records lists by columns
for column in csv_file:
    SCATData.append(column[0])
    SCATData.append(column[1])
f.close()

#Display the combined data into one list
print ('Combined data from two SCAT Files: ', SCATData)

#Open the file for pickling
f = open('pickle0', 'wb')

#Dump the list to file
pickle.dump(SCATData,f, protocol=0)
f.close()

f = open('pickle2', 'wb')
pickle.dump(SCATData,f, protocol=2)
f.close()

#Load information from file
data = pickle.load(f)
f.close()

#Display pickled data
print ('Display the pickled data for protocol 0: ', data)

f = open('pickle2', 'rb')

data = pickle.load(f)

f.close()

print ('Display the pickled data for protocol 2: ', data)

#END OF UNIT 9
