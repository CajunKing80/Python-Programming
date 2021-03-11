# Write a program that takes a number as input and
# - returns its double, if the number is even
# - returns its triple, if the number is odd
# - returns 0, if number is 0

# Sample Input:
# 1

# Sample Output:
# 3 

number = int(input())
#your code goes here

if number %2 == 0:
    print(number * 2)
elif number %2 != 0: 
    print(number * 3)
elif number == 0:
    print(number)