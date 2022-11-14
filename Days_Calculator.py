import datetime


def Days_Calculator():
    '''create a python function that takes 2 dates and prints how
    many days between the 2 dates'''
    fdate, ldate = input("enter first date :"), input("enter second date :")
    fdate, ldate = fdate.split(" "), ldate.split(" ")
    date_1 = datetime.date(int(fdate[-1]), int(fdate[1]), int(fdate[0]))
    date_2 = datetime.date(int(ldate[-1]), int(ldate[1]), int(ldate[0]))
    delta = date_2-date_1
    print(f"number of days is {delta.days} ")


Days_Calculator()
# # enter first date :24 2 2022
# # enter second date :13 10 2022
# # number of days is 231
