# lab11_3a.py - Jhonatan Parada

import string

chars = [c for c in string.ascii_lowercase]
nums = [n for n in range(1, 26 + 1)]

charNum = dict(zip(chars, nums))

for k,v in charNum.items(): 
    print(k,v, end='|')
else: print()