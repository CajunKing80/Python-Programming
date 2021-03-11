
#return the highest element in a list

def highest_element(lst):

    highest = lst[0]
    test = [1,5,8,9,11,16,1599,19,55,99]
    
    # for i in lst: 
    #     if i > highest: 
    #         highest = i 
    # return highest 

    return max(lst)

test = [1,5,8,9,11,16,1599,19,55,5500,99]

print (highest_element(test))