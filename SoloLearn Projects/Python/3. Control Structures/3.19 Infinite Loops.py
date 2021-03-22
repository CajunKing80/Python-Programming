# The given code uses an infinite loop to continuously take user input.
# During each iteration, the user input is added to the items list.

# Change the code to end the loop when the user enters 0.
# Output the resulted list after the while loop ends.

# Sample Input
# 1
# 2
# 3
# 0

# Sample Output
# [1, 2, 3]

items = []

while True:

    n = int(input())
    if n == 0:
        break
    
    items.append(n)

print(items)