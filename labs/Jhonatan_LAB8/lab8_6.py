# lab8_6.py - Jhonatan Parada
from random import randint

def main():
    n = randint(1, 10)
    numList = list(range(1, n + 1))
    print(middle(numList))

def middle(l):
    if not isinstance(l, list): return
    
    msg_1 = 'No changes made to list.'
    msg_2 = 'List length'
    lst_len = len(l)
    new_lst = l.copy()

    if lst_len <= 1: print(msg_1)
    else: new_lst = new_lst[1:-1]

    print(f'{msg_2} = {lst_len}', l, sep='\n')
    return new_lst

main()