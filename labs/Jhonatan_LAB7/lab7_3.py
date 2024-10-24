# lab7_3.py - Jhonatan Parada
start, stop, step = 1, 100, 1
for_sum = 0
while_sum = 0

for n in range(start, stop + step, step):
    for_sum += n
else:
    print(f'Sum = {for_sum}')

while start != (stop + step):
    if start % 2 == 0: while_sum += start
    start += step
else:
    print(f'Sum = {while_sum}')