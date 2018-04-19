import json, calendar
from collections import Counter

from bokeh.plotting import figure, show, output_file

monthList = []

with open('scientist_birthdays.json') as json_data:
    d = json.load(json_data)

for birthday in d.values():
    blist = birthday.split("/")
    month = blist[0]
    monthList.append(int(month))

c = Counter(monthList)
birthdays = dict(c)

p = figure()

keys = list(birthdays.keys())
vals = list(birthdays.values())
print(keys)

p.vbar(x=keys, top=vals, width=0.5)

show(p)
