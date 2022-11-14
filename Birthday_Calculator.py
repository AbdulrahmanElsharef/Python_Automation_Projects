import datetime

def birthdate():
    '''function that takes a user birthdate and
print how many days left to the birthday
args : today , date of birth , number of days
'''
    today = datetime.date.today()
    date = datetime.date(int(input("birthdate_year :")), int(
        input("birthdate_month :")), int(input("birthdate_day :")))
    num_day = date-today
    return f"you have {abs(num_day.days)} for birthdate".title()


days = birthdate()
print(days)

# birthdate_year :2023
# birthdate_month :6
# birthdate_day :30
# You Have 237 For Birthdate

