import datetime
def Age_Calculator():
    '''create a python function that takes user birth year & month & day and prints
how old he is
args:name,birthday,birthmonth,birthyear
return : current age in years&monthand days
'''
    name = input("please enter your name :".title())
    today = datetime.date.today()
    birthday, birthmonth, birthyear = int(input("enter your bithday : ".title())), int(
        input("enter your bithmonth : ".title())), int(input("enter your bithyear : ".title()))
    # input birth year& month and day
    my_age_year, my_age_month, my_age_day = abs(
        birthyear-today.year), abs(birthmonth-today.month), abs(birthday-today.day)
    # get current age from today-my_birthdate
    nex_birthdate = datetime.date(today.year+1, birthmonth, birthday)
    #birth date in next year
    num_day = nex_birthdate-today
    print(
        f"congratulations {name} your age is {my_age_year} years & {my_age_month} month and {my_age_day} days".title())
    print(
        f"congratulations {name} your next birthdate after {num_day.days} days ".title())
Age_Calculator()

# Please Enter Your Name :ahmed hasan
# Enter Your Bithday : 27
# Enter Your Bithmonth : 3
# Enter Your Bithyear : 1973
# Congratulations Ahmed Hasan Your Age Is 49 Years & 8 Month And 22 Days
# Congratulations Ahmed Hasan Your Next Birthdate After 142 Days   