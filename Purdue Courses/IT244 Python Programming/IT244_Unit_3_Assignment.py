
count = 0
total = 0
varGrade = 0
average = 0

#Program starts with a welcome banner instructingthe user to hit enter to begin

print ('Welcome the Grade Averager. Enter 999 at any time to end this program.')

#Loop containing the number of assignments being entered for each student

serviceCode = (input())

while (serviceCode != '999'):

    print ('Please Enter a Name: ') #User inputs either a teachers name
    teacherName = (input())

    print ('Please enter a service code: ') #User enters a teacher or student code
    serviceCode = (input())


    if (serviceCode == "t") or (serviceCode == "T"):
        print ('Please Enter a Room Number: ') #User enters a room number
        roomNumber = int(input())

        print ('How many assignments for this class? ') #User inputs the number of assignments to enter
        assignment = int(input())

    elif (serviceCode == "s") or (serviceCode == "S"):
        print ('Please Enter a Room Number: ')
        roomNumber = int(input())

        print ('Enter assignment grade 1: ')
        assignment1 = int(input())
        total = total + assignment1
        count = count + 1
        print("Total = ", total)

        print ('Enter assignment grade 2: ')
        assignment2 = int(input())
        total = total + assignment2
        count = count + 1
        print("Total = ", total)

    elif (serviceCode != "T") or (serviceCode != "t") or (serviceCode != "S") or (serviceCode != "s"):
        print ('Sorry, invalid service code. Valid codes are T or S')
        serviceCode = (input())
        print ('Please enter a service code: ')
        serviceCode = (input())

    if (serviceCode == '999'):
        print ('Do you want to finalize grades for room ', roomNumber, '? (Y/N): ')
        finalizeGrades = (input())
        average = total / count
        print()
        print ("Class average is:" , average)
        print()
        break
     

while (serviceCode != '999'):

    print ('Please Enter a Room Number: ') #User inputs either a teachers name
    roomNumber = int(input())

    print ('How many assignments for this class? ') #User inputs the number of assignments to enter
    assignment = int(input())

    print ('Please Enter a Name: ') #User inputs either a teachers name
    name = (input())

    print ('Please enter a service code: ') #User enters a teacher or student code
    serviceCode = (input())

    if (serviceCode == "t") or (serviceCode == "T"):
        print ('Please Enter a Room Number: ') #User enters a room number
        roomNumber = int(input())

    elif (serviceCode == "s") or (serviceCode == "S"):
        print ('Please Enter a Room Number: ')
        roomNumber = int(input())

        print ('Enter assignment grade 1: ')
        assignment1 = int(input())
        total = total + assignment1
        count = count + 1
        print("Total = ", total)

        print ('Enter assignment grade 2: ')
        assignment2 = int(input())
        total = total + assignment2
        count = count + 1
        print("Total = ", total)

        print ('Enter assignment grade 3: ')
        assignment3 = int(input())
        total = total + assignment3
        count = count + 1
        print("Total = ", total)

    elif (serviceCode != "T") or (serviceCode != "t") or (serviceCode != "S") or (serviceCode != "s"):
        print ('Sorry, invalid service code. Valid codes are T or S')
        serviceCode = (input())
        print ('Please enter a service code: ')
        serviceCode = (input())

    if (serviceCode == '999'):
        print ('Do you want to finalize grades for room ', roomNumber, '? (Y/N): ')
        finalizeGrades = (input())
        average = total / count
        print()
        print ("Class average is:" , average)
        print()
        break