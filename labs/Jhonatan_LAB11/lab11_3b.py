# lab11_3b.py - Jhonatan Parada

import string
from lab11_3a import charNum

chars = [c for c in string.ascii_uppercase]
nums = [n for n in range(100, 2600 + 100, 100)]

numChar = dict(zip(nums, chars))

for k,v in numChar.items(): print(k,v,end='|')
else: print()

charNum.update(numChar)

print(charNum)