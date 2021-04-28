# Tom has done pull ups every day and recorded his results. He recorded each day's results in a new line, so that each line represents each day he has done pull ups.
# Create a program that takes n number as input and outputs the n-th days result (starting from 0).

# Sample Input
# 4

# Sample Output
# Day 4, 9 pull ups 


file = open("/usercode/files/pull_ups.txt")
n = int(input())

#your code goes here
list = file.readlines()
print (list[n])

file.close()
