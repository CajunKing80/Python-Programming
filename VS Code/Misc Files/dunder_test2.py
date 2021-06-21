from dunder_test import get_name

def get_name_2():
    print("Dunder Test 2 __name__ is set to: {}" .format(__name__))

if __name__ == '__main__':
    get_name()