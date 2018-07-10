#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: DNA_random.py 
@time: 2018/07/08
@software: PyCharm  
"""  
import random
import pandas as pd
import time

start_time = time.time()
all_original_bases = []
all_replace_bases = []
all_strand1 = []
all_strand2 = []

for _ in range(10):
    # bases = ['A', 'T', 'C', 'G']
    bases = 'ATCG'
    bases_choice = [random.choice(bases) for _ in range(12)]
    original_bases = bases_choice[:]
    all_original_bases.append("".join(original_bases))
    bases_choice.reverse()
    # bases_choice = random.sample(bases, 20)
    pattern = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    replace_bases = [pattern[x] if x in pattern else x for x in bases_choice]
    all_replace_bases.append(''.join(replace_bases))

    strand1 = replace_bases[:6]
    strand2 = replace_bases[6:]

    all_strand1.append(''.join(strand1))
    all_strand2.append(''.join(strand2))

    # print(str(original_bases))
    # # print(str(bases_choice))
    # print(str(replace_bases))
    # print(strand1)
    # print(strand2)

print(all_original_bases)
# print(all_replace_bases)
print(all_strand1)
print(all_strand2)

data_frame = pd.DataFrame({
    'strand1': all_original_bases,
    'strand2': all_strand1,
    'strand3': all_strand2
})

data_frame.to_csv("test.csv", index=False, sep=',')

stop_time = time.time()
print('#'*20)
print('运行时间是：', stop_time-start_time)

