# Define the function Ubbi Dubbi, where every vowel is preface with 
def ubbi_dubbi(word):
    
    #Varibale placeholder for user input
    output = []

    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)
    
    return ''.join(output)

print(ubbi_dubbi('python'))