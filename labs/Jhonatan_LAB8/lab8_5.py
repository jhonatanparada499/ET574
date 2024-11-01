# lab8_5.py - Jhonatan Parada
from random import randint

def main():
    prompt = 'Enter a text: '
    text = input(prompt).title()
    n = randint(1, 10)
    
    print(f'text = {text}')
    print(f'n = {n}')
    print(f'message(text, n) will print the following:')
    message(text, n)

def message(p1,p2):
    for i in range(p2):
        print(p1)

main()