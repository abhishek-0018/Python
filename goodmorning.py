import time
timespan=time.strftime('%H:%M:%S')
print(timespan)
timespan=int(time.strftime('%H'))
if timespan<12:
    print("Good Morning")
elif timespan<18:
    print("Good Afternoon")
else:
    print("Good Evening")