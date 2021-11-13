import datetime
import calendar

start = datetime.date(1901,1,1)
end = datetime.date(2001,1,1)

date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
sundays = 0

for date in date_generated:
    if calendar.day_name[date.weekday()] == 'Sunday' and date.day == 1:
        sundays += 1
print(sundays)
