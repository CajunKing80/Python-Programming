# for loops allow you to easily iterate through lists.

# Given a list of numbers, output their sum.

# Sample Input
# 1 3 7 5

# Sample Output
# 16

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0
#your code goes here
for item in list:
	sum = sum + item
print(sum)