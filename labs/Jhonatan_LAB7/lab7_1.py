# lab7_1.py - Jhonatan Parada
err_msg = "Invalid Input."
int_mult = 10 # integer multiple 
str_mult = "multiple of ten" # string multiple title
is_input_mult = False

prmpt = (
    f"Enter an integer number,"
    f" and I'll tell you if it's a {str_mult}: "
)

int_input = input(prmpt)
while not isinstance(int_input, int):
    try:
        int_input = int(int_input)
    except:
        print(err_msg)
        int_input = input(prmpt)

is_input_mult = int_input % int_mult == 0
a_not = 'a' if is_input_mult else 'not'

print(f'{int_input} is {a_not} {str_mult}.')