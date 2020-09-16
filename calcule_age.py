def find_age(current_day, current_month, current_year, birth_day, birth_month, birth_year):
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if (birth_day > current_day):
        current_month -= 1
        current_day = current_date + month[birth_month-1]
        
    if (birth_month > current_month):
        current_year -=  1
        current_month += 12
        
    calculated_day = current_date - birth_day
    calculated_month = current_month - birth_month
    calculated_year = current_year - birth_year
    
    print('Years', calculated_year, ', Months', calculated_month, ', Days', calculated_day)
    
current_day = 10
current_month = 9
current_year = 2020

birth_day = 2
birth_month = 3
birth_year = 1987

find_age(current_day, current_month, current_year, birth_day, birth_month, birth_year)