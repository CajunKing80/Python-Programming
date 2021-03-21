def leap_year(year):
    
    
    if year < 0:
        raise ValueError('The Year Cannot Be a Negative Value.')
    

    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

year = int(input())
leap_year(year)