import time
import calendar
localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)

time = time.asctime()
print(time)

print(calendar.month(1994,8))

print(calendar.leapdays(2016,2019))
"""Prints number of leap days between 2 years"""

print(calendar.isleap(2019))
"""Prints true if the year is leap or false if not"""
