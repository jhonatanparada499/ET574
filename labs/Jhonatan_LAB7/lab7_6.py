# lab7_6.py - Jhonatan Parada
prompt_1 = 'Enter a number n1: '
prompt_2 = 'Enter a nubmer n2: '
err_msg = 'Invalid Input'
equality = 'n1 == n2'

sprtr = '|'
n_step = 1
n1 = 0
n2 = 0

n1 = input(prompt_1)
while not isinstance(n1, int):
    try:
        n1 = int(n1)
        n2 = input(prompt_2)
        while not isinstance(n2, int):
            try:
                n2 = int(n2)
            except:
                print(err_msg)
                n2 = input(prompt_2)
    except:
        print(err_msg)
        n1 = input(prompt_1)

if n1 == n2: print(equality)
else:
    if n1 > n2: n_step = -n_step

    for n in range(n1, n2 + n_step, n_step):
        print(n, end=sprtr)
    else:
        print()