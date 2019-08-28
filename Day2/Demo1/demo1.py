#DayDayUpQ2.py
dayfractor = 0.005
dayUp = pow(dayfractor + 1, 365)
dayDown = pow(dayfractor + 1, 365)
print("向上：{:.2f} 向下：{:.2f}".format(dayUp, dayDown))