#WeekNamePrintV1.py

weekStr = "周一周二周三周四周五周六周日"
weekId = eval(input("请输入星期数字："))
pos = (weekId - 1 ) * 2
print(weekStr[pos: pos + 2])