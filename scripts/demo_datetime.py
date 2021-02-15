import datetime

now = datetime.datetime.now()
now_string = str(now.strftime("%Y-%m-%d_%A_%H%M%S"))

datenow = datetime.datetime.now()
timestamp = '%04d%02d%02d' % (datenow.year, datenow.month, datenow.day)

# %Y = Year
# %M = Month
# %d = Day
# %A = Day of the week
# %H = Hour
# %M = Minute
# %S = Second
print(timestamp)
print(now)
print(now_string)
