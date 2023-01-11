# Question
# 1. Find the first recurring data and return

# input: [1,2,3,4,1,5,6,7]
# output: 1

# 2-approach

# ist

from typing import *
import time

time_1 = time.perf_counter_ns()
def find_recur(arr: List) -> int:
    for num in arr:          
        if arr.count(num) > 1:
            return num

# Time_complexity = O(n^2)
# space = 0(1)

print(find_recur([1,2,3,4,1,5,6,7]))
time_2 = time.perf_counter_ns()
print(time_2- time_1) 

def find_recur_2(arr: List) -> int:
    hash_table = dict

    for num in arr:
        
        if hash_table[num]:
            return num
        else:
            hash_table[num] = num
print(find_recur_2([1,2,3,4,1,5,6,7]))
time_3 = time.perf_counter_ns()
print(time_3 - time_2) 

# space_complexity = O(n)
# Time = 0(1)
