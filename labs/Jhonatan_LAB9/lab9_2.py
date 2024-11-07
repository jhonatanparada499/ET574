# lab9_2.py - Jhonatan Parada

def nameFormat(first, middle, last):
    print(f'{first} {middle[0]}. {last}'.title())

def main():
    nameFormat('john', 'stu', 'smith')
    nameFormat(last='Kennedy', first='john', middle='fitzgerald')

main()