# lab7_1.py - Jhonatan Parada
prmpt = "Enter an integer number, and I'll tell you if it's a multiple of ten: "
err_msg = "Invalid Input."

int_mult = 10 # integer multiple 
str_mult = "multiple of ten." # string multiple

int_input = input(prmpt)

while not isinstance(int_input, int):
    try:
        int_input = int(int_input)
        a_not = 'a' if int_input % int_mult == 0 else 'not'
        print(f'{int_input} is {a_not} {str_mult}')
    except:
        print(err_msg)
        int_input = input(prmpt)