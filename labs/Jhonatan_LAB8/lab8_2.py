# lab8_2.py - Jhonatan Parada
import random
import math

result_msg = 'Square root of'
start, stop = 1, 100

num = random.randint(start, stop)

print(f'{result_msg} {num} = {math.isqrt(num)}')