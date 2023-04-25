import time
from math import floor
shakespeare = open("shakespeare.txt", "r").read()
# shakespeare.txt comes from https://ocw.mit.edu/ans7870/6/6.006/s08/lecturenotes/files/t8.shakespeare.txt

# time in seconds
target_time = 200

method1_total_time = 0
method1_attempts = 0
method2_total_time = 0
method2_attempts = 0


# uses a string for desired text
def method1(text):
    global method1_total_time
    global method1_attempts
    chars = 0
    t1 = time.time()

    for char in text:
        if char in "abc":
            chars += 1
    
    t2 = time.time()
    method1_total_time += (t2-t1)
    method1_attempts += 1


# uses a variable for desired text
def method2(text):
    global method2_total_time
    global method2_attempts
    looking_for = "abc"
    chars = 0
    t1 = time.time()

    for char in text:
        if char in looking_for:
            chars += 1
    
    t2 = time.time()
    method2_total_time += (t2-t1)
    method2_attempts += 1


print("runing one of each method to get an idea of how many attempts to run...")

t1 = time.time()
method1(shakespeare)
method2(shakespeare)
t2 = time.time()

attempts = floor(target_time / (t2 - t1))

print(f"running one of each method takes {t2-t1}, so running {attempts} of each...")

for i in range(attempts):
    method1(shakespeare)
    method2(shakespeare)

print("avg time per attempt:")
print(f"method 1: {method1_total_time / method1_attempts}")
print(f"method 2: {method2_total_time / method2_attempts}")
print("raw times:")
print(f"method 1: {method1_total_time}")
print(f"method 2: {method2_total_time}")
