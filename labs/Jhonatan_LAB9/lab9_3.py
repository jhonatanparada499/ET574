# lab9_3.py - Jhonatan Parada

def nameFormat(last, first, m=None):
    if m: return f'{last}, {first}, {m[0]}.'.title()
    return f'{last}, {first}'.title()

def main():
    name_1 = nameFormat(first='james', last='bond')
    name_2 = nameFormat(first='henry', m='indiana',
                        last='jones')
                        
    print(name_1, name_2, sep='\n')

main()