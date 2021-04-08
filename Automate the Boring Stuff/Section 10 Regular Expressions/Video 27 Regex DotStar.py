import re

beginsWithHelloRegex = re.compile(r'^Hello')
beginsWithHelloRegex.search('Hello there')
beginsWithHelloRegex.search('He said Hello') == None # Python shell interpreter

endsWithWorldRegex = re.compile(r'world!$')
endsWithWorldRegex.search("Hello world!")

allDigitsRegex = re.compile(r'^\d+$')
allDigitsRegex.search('24242342342342')
allDigitsRegex.search('2424234x2342342') == None # Python shell interpreter

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat')
atRegex = re.compile(r'.{1,2}at')
atRegex.findall('The cat in the hat sat on the flat mat')

'First Name: Jeremy  Last Name: King'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
nameRegex.findall('First Name: Jeremy  Last Name: King') # Returns TUPLES

serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
nongreedy.findall(serve)
greedy = re.compile(r'<(.*)>')
greedy.findall(serve)

prime = 'Serve the public trust. \nProtect the innocent. \nUphold the law.'
prime 

dotStar = re.compile(r'.*')
dotStar.search(prime) # Python shell interpreter
dotStar = re.compile(r'.*', re.DOTALL)
dotStar.search(prime) # Python shell interpreter

vowelRegex = re.compile(r'[aeiou]')
vowelRegex.findall('Jeremy, why is your programming book talk about RoboCop so much') #Python shell interpreter
vowelRegex = re.compile(r'[aeiou]', re.IGNORECASE)
vowelRegex.findall('Al, why is your programming book talk about RoboCop so much') #Python shell interpreter