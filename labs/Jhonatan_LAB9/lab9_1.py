# lab9_1.py - Jhonatan Parada

def printList(p):
    if not isinstance(p, list): return
    print(*p)

def main():
    lst = ['apple', 'banana', 'cherry   ']
    printList([lst])

main()