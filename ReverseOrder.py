import time
n = int(input ("Enter the number you want to countdown from: "))

for i in range(n, 0, -1):
    time.sleep(1)
    print(i)