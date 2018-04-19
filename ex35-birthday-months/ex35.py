import json, calendar
from collections import Counter

monthList = []

with open('birthdays.json') as json_data:
    d = json.load(json_data)

for birthday in d.values():
    blist = birthday.split("/")
    month = blist[0]
    monthList.append(calendar.month_name[int(month)])

c = Counter(monthList)
print(dict(c))
