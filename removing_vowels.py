import string
import random
import time
import numpy as np
import math
import pandas as pd

# About
# This started as a way to test if any time would be saved in 
# searching for vowels if the vowel list was arranged by most to least 
# common vowels.
# I found that arranging the list by vowel frequency made a small, but 
# statistically significantly difference
# It is slowly being adapted into a reusable system to compare 
# the efficiency of different algorithm's or built-in functions.

# parameters
sample_size = 2000
confidence_level = 0.99
target_runtime = 60*5 # in seconds

# hp.txt is the full text of Harry Potter and the Sorcerer's Stone
hp = open('hp.txt', 'r').read()
# total of 439,742 characters

# for testing with random strings
# this will obviously have appx equal frequency that each vowel appears
#exstr = ''.join([random.choice(string.ascii_letters) for i in range(1000)])

# vowels in order from most to least used
evbf = ['e', 'a', 'o', 'i', 'u']
evbf_str = ''.join(evbf)
# erv = ['a', 'e', 'i', 'o', 'u']
# vowels in order from least to most used
erv = evbf.copy()
erv.reverse()
print(erv)
erv_str = ''.join(erv)

run_stats = {'vbf': [], 'vbf_str': [], 'rv': [], 'rv_str': []}
total_time_per_method = {'vbf': 0, 'vbf_str': 0, 'rv': 0, 'rv_str': 0}
avg_time_per_method = {'vbf': 0, 'vbf_str': 0, 'rv': 0, 'rv_str': 0}
all_sample_times = {'vbf': [], 'vbf_str': [], 'rv': [], 'rv_str': []}
std_dev_per_method = {'vbf': 0, 'vbf_str': 0, 'rv': 0, 'rv_str': 0}
cis_per_method = {'vbf': [], 'vbf_str': [], 'rv': [], 'rv_str': []}


def vbf(input_string):
    return ''.join([char for char in input_string if char not in evbf])
def vbf_str(input_string):
    return ''.join([char for char in input_string if char not in evbf_str])
def rv(input_string):
    return ''.join([char for char in input_string if char not in erv])
def rv_str(input_string):
    return ''.join([char for char in input_string if char not in erv_str])


def run_n_times(n, exstr):
    for i in range(n):
        ta = time.perf_counter()
        vbf(exstr)
        tb = time.perf_counter()
        vbf_str(exstr)
        tc = time.perf_counter()
        rv(exstr)
        td = time.perf_counter()
        rv_str(exstr)
        te = time.perf_counter()

        vbf_time = tb - ta
        total_time_per_method['vbf'] += vbf_time
        all_sample_times['vbf'].append(vbf_time)

        vbf_str_time = tc - tb
        total_time_per_method['vbf_str'] += vbf_str_time
        all_sample_times['vbf_str'].append(vbf_str_time)

        rv_time = td - tc
        total_time_per_method['rv'] += rv_time
        all_sample_times['rv'].append(rv_time)

        rv_str_time = te - td
        total_time_per_method['rv_str'] += rv_str_time
        all_sample_times['rv_str'].append(rv_str_time)


# located this far into the program to ignore "fixed costs" of runtime
starting_time = time.time()

run_n_times(sample_size, hp)

# takes total time from total_time_per_method and uses it to calculate averages
for method, times in total_time_per_method.items():
    avg_time_per_method[method] = times / sample_size

for method, times in all_sample_times.items():
    # the ddof=1 means np.std is using sample standard deviation
    std_dev_per_method[method] = np.std(times, ddof=1)


def ci_calculator(sample_means, sample_std_devs, confidence_level, sample_size):
    for method in sample_means:
        plus_minus = confidence_level * (sample_std_devs[method] / math.sqrt(sample_size))
        cis_per_method[method] = [sample_means[method] - plus_minus, sample_means[method] + plus_minus]
    return cis_per_method


cis_per_method = ci_calculator(avg_time_per_method, std_dev_per_method, confidence_level, sample_size)

stats = {key: [avg_time_per_method[key]] + cis_per_method[key] for key in avg_time_per_method}

# to give values in ms instead of seconds
adjustment = 1000
table = [[j * adjustment for j in i] for i in stats.values()]
df = pd.DataFrame(table, columns=['avg runtime', 'lower CI', 'upper CI'], index=stats.keys())
print(f"{confidence_level}% confidence interval and n = {sample_size}")
print("All values below are in ms")
print(df.round(2))

# used to figure out how many samples to run for a given target runtime
print('\n\n')
time_delta = time.time() - starting_time
print(f"execution time: {time_delta}")
print(f"time per sample: {time_delta/sample_size}")
print(f"samples for {target_runtime/60} minute execution: {target_runtime/(time_delta/sample_size)}")


# used to see if hp vowel frequency matches typical vowel frequency; it does
# most to least common vowels: e, a, o, i, u
'''
zero_list = [0 for i in range(len(erv_str))]
hp_vowel_freq = dict(zip(evbf, zero_list))

for char in hp:
    if char in evbf_str:
        hp_vowel_freq[char] += 1

#print(hp_vowel_freq)
'''