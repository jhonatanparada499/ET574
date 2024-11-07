# lab8_6.py - Jhonatan Parada
from random import randint

def main():
    n = randint(1, 10)
    numList = list(range(1, n + 1))
    print(numList)
    print(middle(numList))

def middle(l):
    if not isinstance(l, list): return

    if len(l) > 1: l = l[1:-1]
    return l

main()