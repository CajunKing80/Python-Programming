# MyFirstTestRepository

#IT244-01 UNIT 2 ASSIGNMENT

print ('Enter a date between January 1, 1753 and December 31, 2399:')
print ()
print ('Enter a Year (YYYY):')
year = (input())

if (year < "1753") or (year > "2399"):
    print ("Invalid date for this program. Date must be between January 1, 1753 and December 31, 2399. Try again.")
else:
    print ('Enter a Month (MM):')
    month = (input ())
    print ('Enter a Day (DD):')
    dateNumber = int(input())


    if (month == "01"):
        monthCode = 0
    elif (month == "02"):
        monthCode = 3
    elif (month == "03"):
        monthCode = 3
    elif (month == "04"):
        monthCode = 6
    elif (month == "05"):
        monthCode = 1
    elif (month == "06"):
        monthCode = 4
    elif (month == "07"):
        monthCode = 6
    elif (month == "08"):
        monthCode = 2
    elif (month == "09"):
        monthCode = 5
    elif (month == "10"):
        monthCode = 0
    elif (month == "11"):
        monthCode = 3
    elif (month == "12"):
        monthCode = 5
 

    userYearYY = (year[-2:])
    userYearYY = int(userYearYY)
    userYearCC = (year[:2])
    userYearCC = int(userYearCC)


    if (int(year) % 400 == 0) or ((int(year) % 4 == 0) and (int(year) % 100 != 0)):        
            print ('This date falls in a leap year.')
            if (month == "01") or (month == "02"):
                leapCode = 1
            else:
                leapCode=0
    else:
        print ('This date does not fall in a leap year.')


    if userYearCC == 17:
            centuryCode = 4
    elif userYearCC== 18:
            centuryCode = 2
    elif userYearCC == 19:
            centuryCode = 0
    elif userYearCC == 20:
            centuryCode = 6
    elif userYearCC == 21:
            centuryCode = 4
    elif userYearCC == 22:
            centuryCode = 2
    elif userYearCC == 23:
            centuryCode = 0
    else:
            centuryCode = 0
         

    yearCode = ((int(userYearYY/4) + userYearYY) % 7)
     
  
    dayOfWeek = (yearCode + monthCode + centuryCode + dateNumber - leapCode) % 7
 

    if dayOfWeek == 0:
        print ("The day of the week is Sunday.")
    elif dayOfWeek == 1:
        print ("The day of the week is Monday.")
    elif dayOfWeek == 2:
        print ("The day of the week is Tuesday.")
    elif dayOfWeek == 3:
        print ("The day of the week is Wednesday.")
    elif dayOfWeek == 4:
        print ("The day of the week is Thursday.")
    elif dayOfWeek == 5:
        print ("The day of the week is Friday.")
    elif dayOfWeek == 6:
        print ("The day of the week is Saturday.")

#END OF ASSIGNMENT
