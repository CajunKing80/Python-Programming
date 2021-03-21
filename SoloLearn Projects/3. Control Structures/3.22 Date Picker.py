# You are making a date picker for a website and need to output all the years in a given period.
# Write a program that takes two integers as input and outputs the range of numbers between the two inputs as a list.
# The output sequence should start with the first input number and end with the second input number, without including it.

# Sample Input
# 2005
# 2011

# Sample Output
# [2005, 2006, 2007, 2008, 2009, 2010]


a = int(input())
b = int(input())
#your code goes here

c = []

for year in range(a,b):
    c.append(year)

print (c)