import datetime
import calendar
from datetime import time
# import datetime module
today = datetime.date.today()
# use dat.today function
print(today)
# 2022-11-03
print(today.year)
# 2022
print(today.month)
# 11
print(today.day)
# 3
print(today.weekday())
# 3
# 0 index from mondya
print(today.isoweekday())
# 4
# 1 index from mondya
print(calendar.day_name[today.weekday()])
# Thursday
# print today name
day=datetime.timedelta(days=5)
print(today-day)
# 2022-10-29
date=datetime.date(2023,10,1)
days_num=date-today
print(f"number of days for product is ** {days_num.days} days **".title())
# Number Of Days For Product Is ** 332 Days **
print(540+100+70+10+20)