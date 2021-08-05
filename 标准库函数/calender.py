import calendar

calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.firstweekday())
# print(calendar.calendar(2021,2,1,6))
print(calendar.month(2021, 4, 2, 1))
print(calendar.monthcalendar(2021, 4))
print(calendar.monthrange(2021, 4))
c = calendar.calendar(2021)
print(c)
c1 = calendar.TextCalendar(2021)
print(c1)
c2 = calendar.HTMLCalendar(2021)
print(c2)
