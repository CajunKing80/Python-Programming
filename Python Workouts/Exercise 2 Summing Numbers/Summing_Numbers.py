def mysum(*numbers):
    output = 1000
    for number in numbers:
         output += number
    return output

print(mysum(100, 200, 300, 400))