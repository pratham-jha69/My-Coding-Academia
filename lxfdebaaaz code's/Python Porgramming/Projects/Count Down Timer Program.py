import time
my_time= int(input("Enter the time in seconds: "))

for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = (x // 60) % 60
    hours = x//3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}",end="\r",flush=True)
    time.sleep(1)
print("Time's up!")
