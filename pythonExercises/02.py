"""

• Write a script that figures out the number of business days between
two dates. Business days should only take into account weekends, not holidays.

"""
import pandas as pd
from datetime import datetime
from random import randrange as rr

""" For USER input """
# print('Please Enter the first date')
# year1 = int(input("Enter year of first date : "))
# month1 = int(input("Enter number of month for first date : "))
# day1 = int(input("Enter number of day of the second date : "))
# month2 = int(input("Enter number of month for second date : "))
# day2 = int(input("Enter number of day of the second date : "))
# start = datetime(year1, month1, day1)
# end = datetime(year1, month1, day1)
"""--------------------------"""


# GET RANDOM DATES
start = datetime(2018, rr(1, 3), rr(1, 30))
end = datetime(2018, rr(4, 7), rr(1, 30))
index = pd.date_range(start, end)


print('Start Day -- ', start, '\nLast Day  -- ', end)

business_days = []
for i in index:
    # 0 is for Monday , 6 is for Sunday
    day = datetime.weekday(i)
    if day >= 5:
        continue
    business_days.append(i)

print('Total days between dates -- ', index.shape[0])
print('Business days between dates -- ', len(business_days), '\n')

