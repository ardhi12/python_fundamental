# built in modul adalah modul-modul yang sudah tersedia di dalam python 
# https://docs.python.org/3/library/datetime.html
import datetime

now = datetime.datetime.now()
date = now.strftime('%d %B  %Y')

print(now)
print(date)