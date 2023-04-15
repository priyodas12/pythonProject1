import time

for i in range(10):
    print(i)

print("2nd for loop")

for i in range(4,16):
    print(i)

print("3rd for loop")

for i in range(100,150,5):
    print(i)


for i in range(100,0,-1):
    time.sleep(.1)
    print(i)