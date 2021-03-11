def hex_output():
    decNum = 0
    hexNum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexNum)):
        decNum += int(digit, 16) * (16 ** power)
    print(decNum)

hex_output()