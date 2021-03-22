# Given the age of a person as input, you need to output their age group.
# Here are the age groups you need to handle:
# Child: 0 to 11
# Teen: 12 to 17
# Adult: 18 to 64
# Senior: 65+

# Sample Input
# 42

# Sample Output
# Adult 

age = int(input())
# your code goes here

def boolean_age():

    if age in range (0,11):
        print('Child')
    elif age in range (12,17):
        print('Teen')
    elif age in range (18,64):
        print('Adult')
    else: 
        print('Senior')

boolean_age()