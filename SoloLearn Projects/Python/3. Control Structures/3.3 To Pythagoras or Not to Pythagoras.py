# Pythagoras theorem says: In a right-angled triangle, the square of the hypotenuse side is equal to the sum of squares of the other two sides.

# Write a program that takes lengths of triangle sides as inputs, and output whether our triangle is right-angled or not. If the triangle is right-angled, the program should output "Right-angled", and "Not right-angled" if it's not.

# Sample Input
# 3
# 4
# 7

# Sample Output
# Not right-angled 

side1 = int(input())
side2 = int(input())
side3 = int(input())
#your code goes here

if (side1)**2 + (side2)**2 == (side3)**2:
    print('Right-angled')
else: 
    print('Not right-angled')