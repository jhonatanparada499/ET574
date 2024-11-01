# lab8_4.py - Jhonatan Parada

# This could be done:
# [import lab8_3] or [from lab8_3 import hello],
# but the function call [hello()] in lab8_3
# should be removed.

def hello(): print('Hello World')

def helloNum(n):
    par_err = '[n] parameter must be and integer'
    if not isinstance(n, int):
        print(par_err)
        return

    for i in range(n):
        hello()

helloNum(3)