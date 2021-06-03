# =================================================================================================
# EASY ============================================================================================
# =================================================================================================


# print('\n===================================================== EASY =======================================================================')
# alphabet = []

# for letter in 'abcdefghijklmnopqrstuvwxyz': 
#     alphabet.append(letter)
# print(alphabet)

# alphabet = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']
# print (alphabet)
# print('==================================================================================================================================\n')

# =================================================================================================
# MEDIUM ==========================================================================================
# =================================================================================================

# Conditional List Comprehension

# print('\n======= MEDIUM: CONDITIONAL =======')
# number = []

# for num in range(20):
#     if num % 2 != 0:
#         number.append(num)
# print(number)

# number_list = [number for number in range(20) if number % 2 != 0]
# print (number_list)
# print('======= MEDIUM: CONDITIONAL =======\n')

# # Nested List Comprehension

# print('\n============ MEDIUM: NESTED ============')
# numbers = []
# for number in range(100):
#     if number % 2 == 0:
#         if number % 5 == 0:
#             numbers.append(number)
# print (numbers) 

# listOfNumbers = [number for number in range(100) if number % 2 == 0 if number % 5 == 0]
# print (listOfNumbers)
# print('============ MEDIUM: NESTED ============\n')

# =================================================================================================
# HARD ============================================================================================
# =================================================================================================

print('\n=========================================== HARD ===========================================')

perfect = []
abundant = []
deficient = []

for number in range(29): 
       
    aliquot_sum = 0
    
    for x in range(1,number):
        if (number % x == 0):
            aliquot_sum = aliquot_sum + x

    if aliquot_sum == number:
        perfect.append(number)
    elif aliquot_sum > number:
        abundant.append(number)
    elif aliquot_sum < number: 
        deficient.append(number)

print (f'Perfect   : {perfect} \nAbundant  : {abundant} \nDeficient : {deficient}')
print('============================================================================================\n')

number = int()
aliquot_sum = sum([x for x in range(1,number) if number % x == 0])
newList = [perfect.append(number) if aliquot_sum == number else abundant.append(number) if aliquot_sum > number else deficient.append(number) for number in range(1,29)]
print (f'Perfect   : {perfect} \nAbundant  : {abundant} \nDeficient : {deficient}')
print('============================================================================================\n')