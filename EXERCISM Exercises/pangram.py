import string

def is_pangram():

    var = input()

    for character in var: 
        if character not in var:
            return False
        else: 
            return True

is_pangram()
print(is_pangram)