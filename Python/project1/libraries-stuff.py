import time # we need to import the lib first

now = time.localtime()
print(now)
#time.struct_time(tm_year=2023, tm_mon=4, tm_mday=7, tm_hour=11, tm_min=47, tm_sec=56, tm_wday=4, tm_yday=97, tm_isdst=1)

# create a timer
start_time = time.localtime()
print(f"Timer started at {time.strftime('%X', start_time)}")
#^^ .strftime() brings me in a certain format (XX:XX:XX)

# Wait for user to stop timer
input("Press any key to stop Timer")
#now this will register via stop_time
stop_time = time.localtime()

difference = time.mktime(stop_time) - time.mktime(start_time)
#mktime() converts it to format of seconds

print(f"Timer stopped at {time.strftime('%X', stop_time)}")
print(f"Total Time : {difference} Seconds ")

"""
i dont need to grab the whole "time" module, rather just what i need
"""

from time import localtime, mktime, strftime # this is shadowed  probably
# it is used differently than .time method
# see #2 for continuation.


