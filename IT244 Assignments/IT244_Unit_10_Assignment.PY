#UNIT 10 ASSIGNMENT

from temperature import Temperature 

programRunning = True

temperatureValues = {"C":"Celcius","F":"Fahrenheit","K":"Kelvin"}

print ('Temperature Scales: ', temperatureValues)
print ()

sentinelValue = input ("Press 'x' at any time to exit. Press Enter to convert temperatures.")
print ()

if sentinelValue == "x'":
    programmRunning = False

while programmRunning:
    tempEntered = input('Enter a Temperature Value: ')
    if (tempEntered == 'x'):
        programmRunning = False
    else:
        tempScale = input('Enter a Singular Letter to Indicate the Temperature Scale (C, F, or K): ')
        if (tempScale == 'x'):
            programmRunning = False
   
    if programmRunning:
        tempScale = (tempScale.upper())
        if (((tempScale == "C") or (tempScale == "F")  or (tempScale == "K")) and (tempEntered.isdigit())):
            tempEntered = int(tempEntered)
            temps = []
            processTemps = Temperature(tempEntered, tempScale, temps)
            temps = processTemps.storeTemps()
            convertTemps = Temperature(tempEntered, tempScale, temps)
            tempConverted = convertTemps.convertTemp()
            print ("You Entered ", tempEntered, " degrees ", temperatureValues[tempScale], " >>> ")
            print ("The Temperature in Celsuis is ", tempConverted[0])
            print ("The Temperature in Fahrenheit is ", tempConverted[1])
            print ("The Temperature in Kelvin is ", tempConverted[2])
            print ()

        else:
            if tempEntered.isdigit():
                print ('Invalid data entered. Temperature scale must be C, F, or K.')
            else: 
                print ('Invalid data entered. Temperature value must be numeric')

print ("Thank You For Using The Temperature Conversion Program.")

#TEMPERATURE MODULE

class Temperature():
    def __init__(self,tempEntered,tempScale,temps):
        self.tempEntered = tempEntered
        self.tempScale = tempScale
        self.temps = temps

    def storeTemps(self):
        tempC = 0
        tempF = 0
        tempK = 0
        temps = [tempC, tempF, tempK]

        if self.tempScale == "C":
            temps[0] = self.tempEntered
        elif self.tempScale == "F":
            temps[1] = self.tempEntered
        elif self.tempEntered == "K":
            temps[2] = self.tempEntered
        return temps

    def convertTemp(self):
        if self.tempScale == "F":
            self.temps[0] = ((self.temps[1] - 32) * 5/9)
            self.temps[2] = ((self.temps[1] - 32) * 5/9 + 273.15)
        elif self.tempScale == "C":
            self.temps[1] = ((self.temps[0] * 9/5) + 32)
            self.temps[2] = ((self.temps[0] + 273.15))
        else:
            self.temps[1] = ((self.temps[2] - 273.15) * 9/5 +32)
            self.temps[0] = (self.temps[2] - 273.15)
        return (self.temps)