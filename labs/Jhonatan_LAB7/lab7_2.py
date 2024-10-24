# lab7_2.py - Jhonatan Parada
start, end, step = 1, 1000, 1

for n in range(start, end + step, step):
    is_even = n % 2 == 0
    is_mult_of_3 = n % 3 == 0

    if is_even and is_mult_of_3: print(n, end=' ')
else: print()

while start != (end + step):
    is_even = start % 2 == 0
    is_mult_of_3 = start % 3 == 0

    if is_even and is_mult_of_3: print(start, end=' ')
    start += 1
else: print()