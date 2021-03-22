# You are given a list of items.
# Write a program that takes a num number as input, reassigns the element with that index in the list to the value "x" and outputs the updated list.

# For example, for a given list [1, 2, 3, 4, 5] and input 3, the output should be:
# [1, 2, 3, "x", 5]

items  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = int(input())
# your code goes here

print(items)
items[num]="x"
print(items)