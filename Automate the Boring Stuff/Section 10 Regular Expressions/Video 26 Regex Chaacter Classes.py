import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneRegex

variable = 0

phoneRegex.search(variable)

phoneRegex.finall(variable)

digitRegex = re.compile(r'0|1|2|3|4|5|6|7|8|9')

lyrics = ('lyrics to the 12 days of xmas')

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall(lyrics)

# Create your own regex 

vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall()

doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
doubleVowelRegex.findall('RoboCop eats baby food')