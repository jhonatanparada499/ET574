# lab8_1.py - Jhonatan Parada
import math

dnmntr_err = 'Denominator cannot be zero. Try again.'
result = None

def program():
    prompt_1 = 'Enter a numerator: '
    prompt_2 = 'Enter a denominator: '
    prompt_err = 'Invalid Input'
    num_1 = ''
    num_2 = ''

    num_1 = input(prompt_1)
    while not isinstance(num_1, (int,float)):
        try:
            num_1 = eval(num_1)
            num_2 = input(prompt_2)

            while not isinstance(num_2, (int,float)):        
                try:
                    num_2 = eval(num_2)
                except:
                    print(prompt_err, end='\n\n')
                    num_2 = input(prompt_2)  
        except:
            print(prompt_err, end='\n\n')
            num_1 = input(prompt_1)
    
    return num_1, num_2

nmrtr, dnmntr = program()

while result == None:
    if dnmntr != 0:
        result = math.fmod(nmrtr, dnmntr) 
        print(f'{nmrtr} mod {dnmntr} = {int(result)}')
    else:
        print(dnmntr_err, end='\n\n')
        nmrtr, dnmntr = program()