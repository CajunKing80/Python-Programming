# Let's imagine you want to buy an ice-cream for 10 of your friends.
# Write a program that will take the money you have and the price of one ice-cream, and will output the remaining money only if you can buy that ice-cream for your all 10 friends.

# Sample Input
# 80
# 7

# Sample Output
# 10

# Explanation
# To buy 10 ice-creams you need 7*10 = 70.
# The remaining money is 80-70 = 10. 

money = int(input())
price = int(input())

total = price*10
#your code goes here