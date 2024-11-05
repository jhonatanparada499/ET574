# lab8_4.py - Jhonatan Parada
import lab8_3

def helloNum(n):
    par_err = '[n] parameter must be and integer'
    if not isinstance(n, int):
        print(par_err)
        return

    for i in range(n):
        lab8_3.hello()

if __name__ == '__main__':
    helloNum(3)