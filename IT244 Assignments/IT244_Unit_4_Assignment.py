#Magnitude Manufacturing Report Header


print ("\n|======================================================================================================================|")
print ("\n|                                                                                                                      |")
print ("\n|                  Magnitude Manufacturing Employee Annual Raises and Bonuses Report                                   |")
print ("\n|                                                                                                                      |")
print ("\n|======================================================================================================================|")
print ()


#Set variables to be used, according to the assignment directions
employeeRecordsList = list ()
payRaisesList = list ()
jobCodeA = list ()
jobCodeB = list ()
jobCodeC = list ()
count = 0
hitCap = False

#Employee records will be stored in a nested list. Each record consists of the following fields in this order: Employee Name, Employee Code, Performance Code and Current Salary.
#(Hint: Items in a nested list can be accessed by using multiple indices such as Employees[3][2].)
#There are three valid Employee Codes: A, B, and C. 
#There are three valid Performance Codes: 1, 2 and 3 with 1 being the lowest rating.

#Nested List of Employee Records for Magnitude Manufacturing
employeeRecords = [["Ben",'B',58221,2],["Vicki",'C',2,39300],["Frankie",'C',2,25000],["Britta",'B',3,42500], ["Dean",'C',1,20000],["Pierce",'A',1,63500],["Alex",'C',2,22300], 
                  ["Kevin",'C',3,38750],["Neal",'C',1,39750], ["Leonard",'A',3,65000],["Annie",'B',2,53500],["Troy",'C',3,38940],["Shirley",'A',2,75350],["Jeff",'C',1,24800], 
                  ["Abed",'C',3,18750],["Garrett",'A',2,68750], ["Elroy",'B',2,58750], ["Todd",'C',1,28150], ["Jerry",'B',2,38200], ["Buzz",'B',3,58750]]

#Job Code Bonus dictionary. Dictionary uses key to value pairs. 
employeeCode = {"A": 2000, "B": 1750, "C": 1500}

#Job Code Salary Caps dictionary: 
salaryCap = {"A": 75000, "B": 60000, "C": 40000}

#Performance Code Salary Increase
performanceCode = {"1": .01, "2": .02, "3": .04}


#Each employee will have their salary increased based on the Performance Code assigned to them. Salaries may not exceed the salary cap for the given Employee Code. If a new salary 
#exceeds the cap, the cap value is used as the new salary. Update the employee's salary in the employee's record. 

#for employee in employeeRecords: 

for employee in employeeRecords: 
    newSalary = (employee[3]*performanceCode[str(employee[2])]+employee[3]) 
    Cap = salaryCap[employee[1]]
    if (newSalary>Cap):
        newSalary = Cap
        hitCap = True

#Store employee new salary as currency and append to the empty employeeRecordsList
# this does not need to be within the salary cap IF statement above - it's part of the for loop going through employee records
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
    #break
    employeeRecords[count][3] = newSalary
    count = count + 1

#Salary Cap Report

print ('------------------------------------------------------------------------------------------------------------------------')
print ('These employees hit their salary cap:')
print ('------------------------------------------------------------------------------------------------------------------------')
print ()

print ("{:<15}{:<10}{:<20}".format("Name", "Code", "Salary"))
for employee in employeeRecordsList:
    if(employee[5]==True):
        print ("{:<15}{:<10}{:<20}".format(employee[0],employee[1],employee[4]))


print ('------------------------------------------------------------------------------------------------------------------------')
print ('Salary Report')
print ('------------------------------------------------------------------------------------------------------------------------')
print ()

print("{:<15}{:<10}{:<20}".format("Name", "Job Code", "Performance Code", "Old Salary", "New Salary" ))
if len(employeeRecordsList)!=0:
    for emp in employeeRecordsList:
        empRecord = [emp[0],emp[1],emp[2],'${:,.2f}'.format(emp[3]),emp[4]]
        print ("{:<15}{:<10}{:<20}{:<20}{:<20}".format(empRecord[0], empRecord[1], empRecord[2], empRecord[3], empRecord[4]))
    pass

print ('------------------------------------------------------------------------------------------------------------------------')
print ('Bonus Report')
print ('------------------------------------------------------------------------------------------------------------------------')
print ()

print ("{:<20}{:<20}.".format("Name", "Bonus" ))
for employee in employeeRecords: 
    if employee[2]>=2:
        bonusRecord = (employee[0],'${:,.2f}'.format(employeeCode[employee[1]]))
        print ("{:<20}{:<20}.".format(bonusRecord[0], bonusRecord[1] ))
    pass

#Define Statistics Variables

average = 0
sum = 0
recordCount = 0
payIncreaseSet = set()
bonusList = list()

print ('------------------------------------------------------------------------------------------------------------------------')
print ('Statistics:')
print ('------------------------------------------------------------------------------------------------------------------------')
print ()

#Average of the employees with a C code

sumOfEmployeeBonuses = 0
empCount = len(jobCodeC)
averageEmployeeBonus = 0

for employee in jobCodeC:
    sumOfEmployeeBonuses = sumOfEmployeeBonuses + employee[5]
    averageEmployeeBonus = sumOfEmployeeBonuses / empCount
    pass

print ("Average of C Code Employee Bonuses: ", '${:,.2f}'.format(averageEmployeeBonus))

for employee in employeeRecordsList:
    newSalary = (employee[3]*performanceCode[str(employee[2])])+employee[3]
    Cap = salaryCap[employee[1]]
    if (newSalary>Cap):
        newSalary = Cap
    diff = newSalary - employee[3]
    payIncreaseSet.add(diff)
    sum = sum + diff
    recordCount = recordCount + 1
    average = sum / recordCount
    pass

print ("Average salary increase for all divisions: ", '${:,.2f}'.format(average))

payIncreaseList = list(payIncreaseSet)
n = len(payIncreaseList)
payIncreaseList.sort()

if n % 2 == 0:
    median1 = payIncreaseList [n // 2]
    median2 = payIncreaseList [n // 2 - 1]
    median = (median1 + median2) / 2
else:
    median = payIncreaseList[n//2]
print ('Median of pay increases is: ' + '${:,.2f}'.format(median))

for employee in employeeRecords: 
    if employee[2]>=2:
        bonusList.append(employeeCode[employee[1]])


#Import built-in Python collections library

from collections import Counter

print("Mode value of all bonuses given:  ", '${:,.2f}'.format(Counter(bonusList).most_common(1)[0][0])) # Returns the highest occurring item 

bonusAverage = (680,740,810,averageEmployeeBonus)

maxAverage = max(bonusAverage)
minAverage = min(bonusAverage)

sortedTuple = sorted(bonusAverage, reverse=True)

print ("The highest division average of all bonuses given: ", '${:,.2f}'.format(maxAverage))
print ("The lowest division average of all bonuses given: ", '${:,.2f}'.format(minAverage))

print ('Division Bonus Rankings: ')
rankNumber = 0
for row in sortedTuple:
    rankNumber = rankNumber + 1
    print ("Rank", rankNumber, "average ", '${:,.2f}'.format(row))

print ("\n|======================================================================================================================|")
print ("\n|                                                                                                                      |")
print ("\n|====================================================END OF REPORT=====================================================|")
print ("\n|                                                                                                                      |")
print ("\n|======================================================================================================================|")
print ()

