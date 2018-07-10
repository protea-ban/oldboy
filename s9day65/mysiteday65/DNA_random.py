#!/usr/bin/env python  
#-*- coding:utf-8 -*-  
""" 
@file: DNA_random.py 
@time: 2018/07/08
@software: PyCharm  
"""  
import random

# bases = ['A', 'T', 'C', 'G']
bases = 'ATCG'
bases_choice = [random.choice(bases) for _ in range(12)]
original_bases = bases_choice[:]
bases_choice.reverse()
# bases_choice = random.sample(bases, 20)
pattern = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
replace_bases = [pattern[x] if x in pattern else x for x in bases_choice]

strand1 = replace_bases[:6]
strand2 = replace_bases[6:]

print(str(original_bases))
# print(str(bases_choice))
print(str(replace_bases))
print(strand1)
print(strand2)