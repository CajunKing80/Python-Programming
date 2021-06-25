def is_armstrong_number(number):
    
    list_num = []
    
    for x in str(number):
        
        list_num.append(int(x) ** len(str(number)))
    return sum(list_num) == number

print(is_armstrong_number(9926314))