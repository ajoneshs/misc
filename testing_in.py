import time

shakespeare = open("shakespeare.txt", "r").read()
# shakespeare.txt comes from https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt
chars = 0

t1 = time.time()

for i in range(10):
    chars = 0
    for char in shakespeare:
        if char in "abc":
            chars += 1

t2 = time.time()

for i in range(10):
    chars = 0
    for char in shakespeare:
        if char == "a" or char == "b" or char == "c":
            chars += 1

t3 = time.time()

print(f"method 1 time: {t2-t1}")
print(f"method 2 time: {t3-t2}")

print("retrying method 1...")

t4 = time.time()

for i in range(10):
    chars = 0
    for char in shakespeare:
        if char in "abc":
            chars += 1

t5 = time.time()

print(f"method 1 tried again time: {t5-t4}")

print("retrying method 2...")

t6 = time.time()

for i in range(10):
    chars = 0
    for char in shakespeare:
        if char == "a" or char == "b" or char == "c":
            chars += 1

t7 = time.time()

print(f"method 2 tried again time: {t7-t6}")

# seems like doing `looking_for in "string"` is faster than `looking_for == "s" or looking_for == "t" or ...`