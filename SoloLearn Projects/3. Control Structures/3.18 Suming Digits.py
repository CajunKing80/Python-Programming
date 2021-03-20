#  given program calculates and outputs the number of digits in a given number using a while loop.
# n = int(input())

# length = 0

# while n > 0:

#     n //= 10

#     length += 1

    

# print(length) 
# PY
# During each iteration, the loop uses floor division to divide the given number by 10, thus dropping one digit.
# The process continues until the number has no more digits (n>0).

# You need to change the code to calculate and output the sum of all digits of the input number.

# Sample Input
# 643

# Sample Output
# 13

# Explanation
# The sum of the digits of 643 is 6+4+3 = 13. 


n = int(input())

length = 0

for i in str(n): 
    length += int(i)
    
print(length)