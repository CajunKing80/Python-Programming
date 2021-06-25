def is_pangram(sentence):
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letters_in_sentence = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for letter in sentence.lower(): 
        if letter in alphabet:
            letters_in_sentence[alphabet.index(letter)] += 1

    for number in letters_in_sentence:
        if number == 0:
            return False
    return True    

is_pangram()