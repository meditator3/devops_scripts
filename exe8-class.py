from argparse import ArgumentParser
import time
parser = ArgumentParser(description="shows how long device was open or with err, plus timestamps")
parser.add_argument('filename', help="the file to read")

args = parser.parse_args()
#print(args.filename)
device_timetable = []
with open(args.filename) as f:
    lines = f.readlines()
    #print(lines)
    for line in lines:
        if "Device State: " in line:
            device_timetable.append(line.split(" "))
            #print(line)
            #print("*************\n")
#0- month
#1= day
#2= timestamp
#7= device state
for state in device_timetable:
    if "ON" in state[7]:
        time_on = state[2]
    if state[7]=="ERR" or state[7]=="OFF":
        time_off = state[2]
    difference = time.mktime(time_off) - time.mktime(time_on)
    print(f"Device was on for {difference} seconds")
        
print(device_timetable[0][2],device_timetable[0][7])

