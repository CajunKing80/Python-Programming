
# Imagine a vending machine that sells fruits. Each fruit has its own number, starting from 0.
# Write a program for the vending machine, which will take n number as input from the customer and return the fruit with that index.
# fruits = ["apple", "cherry", "banana", "kiwi", "lemon", "pear", "peach", "avocado"] 
# PY
# If n< 0 or n>7 (the index of last fruit ), the program outputs "Wrong number".

# Sample Input:
# 2

# Sample Output:
# banana 

fruits = ["apple", "cherry", "banana", "kiwi", "lemon", "pear", "peach", "avocado"]
num = int(input())
#your code goes here

if num < 0 or num > 7:
	print ('Wrong number')
else:
	print(fruits[num])