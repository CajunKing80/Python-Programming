# Write a program that will be used in a robot that categorizes items by their color.
# Each color corresponds to a box with a specific number.
# For simplicity, our program will handle 3 colors:
# red goes to box #1
# green goes to box #2
# black goes to box #3

# Your program needs to take a color as input and output the corresponding box number.

# Sample Input
# green

# Sample Output
# 2 

color = input()
# your code goes here

def robot():

    if color == "red": 
        print('1')
    elif color == "green": 
        print('2')
    elif color == "black":
        print('3')

robot()