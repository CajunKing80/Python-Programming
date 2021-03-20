# A shop is running a promotion today! If an item's price is an odd number, you get that item for free!

# You use a list to store the prices of all items in the shopping cart.
# The given code uses a while loop to iterate over the list, calculates the price of all the items in the list, and output the result.

# Change the code to skip the odd prices, calculate the sum of only the even prices and outputs the result.

items = [23, 555, 666, 123, 128, 4242, 990]

sum = 0
n = 0
while n < len(items):

    n += 1
    num = items[n]

    if num % 2 == 1:
        continue
    else:
        sum += num
    
print(sum)


# items = [23, 555, 666, 123, 128, 4242, 990]
# items_new = []
# total =0 
# length = 0
# n = 0
# while n < len(items):

#     for num in items:
#         n += 1
#         if num % 2 == 0:
#             items_new.append(num)
#         else:
#             continue

# for item in items_new:
#     total = total + items_new

# print(total)