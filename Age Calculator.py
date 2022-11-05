import datetime


def Age_Calculator():
    '''create a python function that takes user birthdate and prints
how old he is
'''
    today = datetime.date.today()
    birthyear,birthmonth,birthday=int(input("enter your bithyear : ")),int(input("enter your bithmonth : ")),int(input("enter your bithday : "))
    my_age = list(birthyear-today.year,birthmonth-today.month,birthday-today.day)
    return f"you have {(my_age)} years".title()


age = Age_Calculator()
print(age)
