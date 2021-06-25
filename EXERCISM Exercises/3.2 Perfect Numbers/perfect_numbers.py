def classify(number):

    if number <= 0:
        raise ValueError('Not a natural number')
    
    aliquot_sum = sum([x for x in range(1,number) if number % x == 0])

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    elif aliquot_sum < number: 
        return "deficient"
