def armstrong(number):
    
    list_num = []
    
    for x in str(number):
        
        list_num.append(int(x) ** len(str(number)))
    return sum(list_num) == number

print(armstrong(153))