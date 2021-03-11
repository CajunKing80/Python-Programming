
#UNIT ^ ASSIGNMENT

#Temperature Conversion
def tempConvert (temps, tempScale): 
    if tempScale == "F":
        temps[0] = ((temps[1] - 32) * 5/9)
        temps[2] = ((temps[1] - 32) * 5/9 + 273.15)
        return (temps)
    elif tempScale == "C":
        temps[1] = ((temps[0] * 9/5) + 32)
        temps[2] = ((temps[0] + 273.15))
        return (temps)
    else:
        temps[1] = ((temps[2] - 273.15) * 9/5 +32)
        temps[0] = (temps[2] - 273.15)
        return (temps)

#Set Flags
programRunning = True

#Dictionary holding the values for the temperature inputs
tempScaleCodes = {"C":"Celcius", "F":"Fahrenheit", "K":"Kelvin"}

print ('Temperature Scales: ', tempScaleCodes)
print ()

#User inputs temperature and scale values
userTemp = input('Enter a Temperature Value: ')
userScale = input('Enter a Single Letter to Indicate the Temperature Scale (C, F, or K): ')
sentinelValue = input('Enter "X" to Quit or Press Enter to Convert the Temperatures. ')
print ()

if sentinelValue == "X":
    programRunning = False

#If a valid temperature was entered, convert temperatures
while programRunning: 
    userScale = (userScale.upper())
    userTemp = int(userTemp)
    #Define temperature variables
    tempC = 0
    tempF = 0
    tempK = 0
    #Create temperature list
    temps = [tempC, tempF, tempK]
    if userScale == "C":
        temps[0] = userTemp
    elif userScale == "F":
        temps[1] = userTemp
    elif userScale == "K":
        temps[2] = userTemp
    else:
        print ('Invalid Temperature Scale Entered. Scale Must Be C, F, or K.')
        programRunning = False 
    if programRunning: 
        print ('You Entered', userTemp, " degrees ", tempScaleCodes[userScale], ">>>")
    break


tempConvert(temps, userScale)

print ('The Temperature in Celcius is ', temps[0])
print ('The Temperature is Fahrenheit is ', temps[1])
print ('The Temperature in Kelvin is ', temps[2])
print ()


print ('Thank You For Using the Temperature Conversion Program. Have a Nice Day')
print ()

#END OF UNIT 6 ASSIGNMENT