# SECTION 2: FLOW CONTROL

# ========================================================================

# print ('Hello World') 

# print ('What is your name? ') #ask the user for their name
# myName = input()
# print ('It is nice to meet you, ' + myName)
# print ('The length of your name is: ')
# print (len(myName))

# print ('What is your age? ') #ask the user for their age
# myAge = input()
# print ('You will be ' + str(int(myAge) + 1) + ' in a year.')

# ========================================================================

# If, Else and Elif Statements
 
# ========================================================================

# name = 'Bob'
# if name == 'Alice':
#     print ('Hi Alice')
# print ('Done')

# password = 'swordfish'
# if password == 'swordfish':
#     print ('Access Granted')
# else: 
#     print ('Access Denied')

# name = 'Bob'
# age = 3000
# if name == 'Alice':
#     print ('Hi Alice')
# elif age < 12:
#     print ('You are not Alice')
# elif age > 2000:
#     print ('You are too old to be Alice')
# elif age > 100:
#     print ('You are Alice')

# ========================================================================

# spam = 0
# while spam < 5:
#     print ('Hello World')
#     spam = spam + 1

# name = ''
# while name != 'your name':
#     print ('Please type your name')
#     name = input()
# print ('Thank You')

# name = ''
# while True:
#     print ('Please type your name')
#     name = input()
#     break
# print ('Thank You')

# spam = 0 
# while spam < 5:
#     spam = spam + 1
#     if spam == 3: 
#         continue 
#     print ('spam is ' + str(spam))

# ========================================================================

# print ('My name is ')
# for i in range(5):
#     print ('Jeremy 5 Times ' + str(i))

# ========================================================================

# total = 0
# for num in range(101):
#     total = total + num
# print (total)

# ========================================================================

# SECTION 3 FUNCTIONS

# ========================================================================

# Built-In functions
# print()
# input()
# len()

# Modules = Standard Library
# Not built-in functions, must be "called" on
#     math module
#     random module
#         random.randit(1,100)
#     sys module
#         sys.exit()
#     os module
#     pyperclip module
#     math module

# Import modules using the import statement

# import sys 
# print ('Hello')
# sys.exit()
# print ('Goodbye')

# #3rd Part Modules

# import pyperclip 

# pyperclip.copy("Hello World!")
# pyperclip.paste()

# ========================================================================

# WRITING YOUR OWN FUNCTIONS

# ========================================================================

# def hello(): 
# #def statement defines a function 
# #functions clean up code by removing duplicate code
#     print ('Howdy!')
#     print ('Howdy!!')
#     print ('Hello There.')

# hello()
# hello()
# hello()

# def hello(name):                # Argument = The value passed in a function
#     print ('Hello ' + name)     # Parameter = THe variable inside the function

# hello('Alice')
# hello('Bob')

# print ('Hello has ' + str(len('hello')) + ' letters in it.')

# ========================================================================

# def plusOne(num): #define the function plusOne with a variable of num
#     return num + 1 #function returns the num variable and adds 1 to it

# newNumber = plusOne(50) #create a new variable named newNumber and pass plusOne to it
# print(newNumber)

# print('Hello', end=' ') # Keywords include end and sep 
# print('World')

# print('Hello', 'World')
# print('Hello', 'World', sep='ABC')

# ========================================================================

# spam = 42 # Global Variable

# def eggs():
#     spam = 42 # Local Variable

# def spam():
#     eggs = 99
#     bacon()
#     print (eggs)
#     print ()

# def bacon():
#     ham = 101
#     eggs = 0

# spam()

# def spam():
#     eggs = 'Hello'
#     print (eggs)
#     print ()

# eggs = 42
# spam()
# print (eggs)
# print ()

# ========================================================================

# SECTION 4 HANDLING ERRORS WITH TRY/EXCEPT

# ========================================================================

# def div42by(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: You Tried to Divide By Zero')

# print(div42by(2))
# print(div42by(12))
# print(div42by(0))
# print(div42by(1))

# =========================================================================

# Numbber Guessing Game

from random import randint

def guessing_game():
    answer = randint(0,1000)

    while True:
        user_guess = int(input('Pick a Number, 1 - 1000: '))

        if user_guess == answer:
            print(f'Right! The answer is {user_guess}')
            break 

        elif user_guess < answer: 
            print(f'Your guess of {user_guess} is too low!')

        else: 
            print(f'Your guess of {user_guess} is too high!')

guessing_game()