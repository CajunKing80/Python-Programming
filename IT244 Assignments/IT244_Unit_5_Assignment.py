#UNIT 5 ASSIGNMENT (Using the UNit 4 Assignment as a template)

#Program Requirements: 
    #For the UNit 5 Assignment your HR program will need to require the user to enter the correct user ID and password to run the program. The login information is as follows: 
        #UserID: Student
        #Password: Python123

#Set UserID
userIDIncorrect = True

#Prompt for user to enter the UserID
userID = input('Please Enter the User ID: ')
print ()

#If User ID is incorrect, prompt user to re-enter the credentials
while userIDIncorrect:
    if (userID != "Student"):
        print ('The User ID You Entered Is Incorrect. Please Try Again. ')
        userID = input('Please Enter the User ID: ')
        print ()
    else: 
        userIDIncorrect = False

#Set Password
passwordIncorrect = True

#Prompt for user to enter the password
password = input("Please Enter the Password: ")
print ()

#If password is incorrect, prompt user to re-enter the credentials
while passwordIncorrect: 
    if (password != "Python123"):
        print ('THe Password You Entered Is Incorrect. Please Try Again. ')
        password = input("Please Enter the Password: ")
        print ()
    else:
        passwordIncorrect = False

#Once the correct UserID and password have been entered, the program will open
#Employee records are stored in the supplied .csv file, IT244_Unit_5_Data.csv. 
#Each record consists of the following fields in this order: Employee Name, Employee Code, Performance Code, and Current Salary. This data must be read into your program from this file.

f = open ("IT244_Unit_5_Data.csv", "r")
employeeRecordsFromFile = f.read ()
f.close ()

#Create a nested list of data from the employee record file

employeeRecords = [b.split(',') for b in employeeRecordsFromFile.split('\n')]

#Variables Created From Unit 4 Assignment. Defining the variables and lists.

employeeRecordsList = list ()
payRaisesList = list ()
jobCodeA = list ()
jobCodeB = list ()
jobCodeC = list ()
count = 0
hitCap = False
employeeCode = {"A": 2000, "B": 1750, "C": 1500}
salaryCap = {"A": 75000, "B": 60000, "C": 40000}
performanceCode = {"1": .01, "2": .02, "3": .04}

#Each employee will have their salary increased based on the Performance Code assigned to them. Salaries may not exceed the salary cap for the given Employee Code. If a new salary 
#exceeds the cap, the cap value is used as the new salary. Update the employee's salary in the employee's record. 

#for employee in employeeRecords: 

for employee in employeeRecords: #Salary cap calculations
    salaryWork = int(employee[3]) #salaryWork is pulling in the Current Salary
    newSalary = (salaryWork*performanceCode[str(employee[2])]+salaryWork) 
    Cap = salaryCap[employee[1]]
    if (newSalary>Cap):
        newSalary = Cap
        hitCap = True

#Store employee new salary as currency and append to the empty employeeRecordsList
    employeeRecordsList.append((employee[0],employee[1],employee[2],employee[3],'${:,.2f}'.format(newSalary),hitCap))

#All employees who have a Performance Code of 2 or higher will receive the bonus amount tha corresponds with their Employee Code. If Empoyee Code is A, set bonus for performance code, else set to 0

    if employee[1]=='A':
        if employee[2]>=2:
            jobCodeA.append((employee[0],employee[1],employee[2],employee[3],'${:,.2f}'.format(newSalary),employeeCode[employee[1]]))
        else: 
            jobCodeA.append((employee[0],employee[1],employee[2],employee[3],'${:,.2f}'.format(newSalary),0))
    elif employee[1]=='B':
        if employee[2]>=2:
            jobCodeB.append((employee[0],employee[1],employee[2],employee[3],'${:,.2f}'.format(newSalary),employeeCode[employee[1]]))
        else:
            jobCodeB.append((employee[0],employee[1],employee[2],employee[3],'${:,.2f}'.format(newSalary),0))
#If employeeCode is C, set bonus level A for Performance Code >= 2

    elif employee[1]=='C':
        if employee[2]>=2:
            jobCodeC.append((employee[0],employee[1],employee[2],employee[3],'${:,.2f}'.format(newSalary),employeeCode[employee[1]]))
        else: 
            jobCodeC.append((employee[0],employee[1],employee[2],employee[3],'${:,.2f}'.format(newSalary),0))
    employeeRecords[count][3] = newSalary
    count = count + 1

#Open the file for writing the report of employees reaching their salary caps
f = open("JKing_Reports.txt", "w+")

#Write the Report Header
f.write ("Magnitude Manufacturing Company")
f.write ("\r\n")
f.write ("-------------------------------------------------------------------------------------------------------------------------")
f.write ("\r\n")


#Salary Cap Report Heading and Section

f.write ('\r\n')
f.write ('------------------------------------------------------------------------------------------------------------------------')
f.write ('\r\n')
f.write ('These employees hit their salary cap:')
f.write ('\r\n')
f.write ('------------------------------------------------------------------------------------------------------------------------')
f.write ('\r\n')
f.write ()

f.write ("{:<15}{:<10}{:<20}".format("Name", "Code", "Salary"))
for employee in employeeRecordsList:
    if(employee[5]==True):
        f.write ("{:<15}{:<10}{:<20}".format(employee[0],employee[1],employee[4]))
        f.write ('\r\n')
f.write ('------------------------------------------------------------------------------------------------------------------------')
f.write ('\r\n')


if len(employeeRecordsList)!=0:
    for emp in employeeRecordsList:
        empRecord = [emp[0],emp[1],emp[2],'${:,.2f}'.format(emp[3]),emp[4]]
        pass


#Define Statistics Variables

average = 0
sum = 0
recordCount = 0
payIncreaseSet = set()
bonusList = list()


#Statistics Heading and Section

f.write ('\r\n')
f.write ('------------------------------------------------------------------------------------------------------------------------')
f.write ('\r\n')
f.write ('Statistics: ')
f.write ('\r\n')
f.write ('------------------------------------------------------------------------------------------------------------------------')
f.write ('\r\n')
f.write ()

#Average of the employees with a C code

sumOfEmployeeBonuses = 0
empCount = len(jobCodeC)
averageEmployeeBonus = 0

for employee in jobCodeC:
    sumOfEmployeeBonuses = sumOfEmployeeBonuses + employee[5]
    averageEmployeeBonus = sumOfEmployeeBonuses / empCount
    pass

averageofCBonuses = ('${:,.2f}'.format(averageEmployeeBonus))
f.write ("Average of C Bonuses = ")
f.write (averageOfCBonuses)
f.write ("\r\n")

#Loop through the employee records to calculate the average salary icrease value

for employee in employeeRecordsList:
    salaryWork = int(employee[3])
    newSalary = (salaryWork*performanceCode[str(employee[2])])+salaryWork
    Cap = salaryCap[employee[1]]
    if (newSalary>Cap):
        newSalary = Cap
    diff = newSalary - salaryWork
    payIncreaseSet.add(diff)
    sum = sum + diff
    recordCount = recordCount + 1
    average = sum / recordCount
    pass

#Display the average salary increase value

averageSalaryIncreaseForAll = str('${:,.2f}'.format(average))
f.write ("Average salary increase for all divisions: ")
f.write (averageSalaryIncreaseForAll)
f.write ("\r\n")

#List of elements to calculate the median

payIncreaseList = list(payIncreaseSet)
n = len(payIncreaseList)
payIncreaseList.sort()

if n % 2 == 0:
    median1 = payIncreaseList [n // 2]
    median2 = payIncreaseList [n // 2 - 1]
    median = (median1 + median2) / 2
else:
    median = payIncreaseList[n//2]
f.write ('Median of pay increases is: ' + '${:,.2f}'.format(median))
f.write ("\r\n")

#Create the Bonus List to calculate the mode

for employee in employeeRecords: 
    if employee[2]>=2:
        bonusList.append(employeeCode[employee[1]])

#Import built-in Python collections library

from collections import Counter

modeString = ('${:,.2f}'.format(Counter(bonusList).most_common(1)[0][0])) # Returns the highest occurring item 
f.write ("Mode value of all bonuses given: ")
f.wrtie (modeString)
f.write ("\r\n")

bonusAverage = (680,740,810,averageEmployeeBonus)

maxAverage = max(bonusAverage)
minAverage = min(bonusAverage)

sortedTuple = sorted(bonusAverage, reverse=True)

#Write out the highest and lowest division amounts from tuple values

maxAverage = str('${:,.2f},'.format(maxAverage))
minAverage = str('${:,.2f},'.format(minAverage))

f.write ("The highest division average of all bonuses given: ")
f.write (maxAverageString)
f.write ("\r\n")
f.write ("The lowest division average of all bonuses given: ")
f.write (minAverageString)
f.write ("\r\n")
f.write ("\r\n")

#Use sorted tuple to write out the average values of all the divisions 

f.write ('Division Bonus Rankings: ')
f.write ("\r\n")
rankNumber = 0
for row in sortedTuple:
    rankNumber = (rankNumber + 1)
    rankNumberString = str(rankNumber)
    f.write ("Rank - ")
    f.write (rankNumberString)
    f.write (" / ")
    f.write ("average: ")
    f.write ("\r")
    rowString = str('${:,.2f}'.format(row))
    f.write (rowString)
    f.write ("\r\n")


#CLOSE THE REPORT

f.close ()

#OPEN THE BONUS REPORT CSV FILE

f = open ("JKing_Bonus.csv", "w+")

#WRITE THE REPORT HEADER TO THE .CSV FILE

f.write ("Magnitude Manufacturing Company")
f.write ("\r")
f.write ("-------------------------------------------------------------------------------------------------------------------------")
f.write ("\r")

#BONUS INFORMAITON

f.write ("{:<20}{:<20}".format("Name", "Bonus"))
f.write ("\r")

#LOOP THROUGH EMPLOYEES TO F.WRITE OUT EVERY EMPLOYEE WHO HAD A BONUS WITH THEIR BONUS

for employee in employeeRecords:
    if employee[2]>="2":
        bonusRecord = (employee[0],str(employeeCode[employee[1]]))
        f.write ("{:<20}{:<20}".format(bonusRecord), bonusRecord[1])
        f.write ("\r")
f.write ("-------------------------------------------------------------------------------------------------------------------------")
f.write ("\r")


#CLOSE THE BONUS CSV FILE

f.close ()

#PRINT BOTH REPORTS

print ("\r\n")
file_o = open ("JKing_Reports,txt")    #Creates object "file_o" to access the first file
content = file_o.read()                #File is read using the created object "file_o"
print (content)                        #Prints the file "file_o"
file_o = close                           #Closes the file "file_o"


file_o = open ("JKing_Bonus.csv")      #Creates object "file_o" to access the second file
content = file_o.read()                #File is read using the created object "file_o"
print (content)                        #Prints the file "file_o"
file_o = close                         #Closes the file "file_o"


print ("END OF PROGRAM: BOTH REPORTS HAVE BEEN CREATED")
print ("THIS ASSIGNMENT WAS A MENTAL NINJA")

#END OF ASSIGNMENT 5
