import time
time.sleep(1)
timestart=int(input("enter the time to start the countdown: "))
for i in range(timestart,-1,-1):
    print(i)
    time.sleep(1)
print("Happy New Year!")
