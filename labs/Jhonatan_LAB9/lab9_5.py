# lab9_5.py - Jhonatan Parada
from random import randint

def average(*grades):
    return sum(grades) / len(grades)

def main():
    x= randint(-100,-1)
    y = randint(0,1)
    z = randint(1, 100)
    
    stat_grades = (95, 87, 83, 74)
    rand_grades = (x, y, z)

    # average(*rand_grades) = average(x, y, z)
    # average(rand_grades) = average((x, y, z))

    print(
        f'Average of {str(stat_grades)[1:-1]}:',
        f'{average(*stat_grades):.2f}',
        sep=' '
    )

    print(
        f'Average of any three random numbers,',
        f'{str(rand_grades)[1:-1]}:',
        f'{average(*rand_grades):.2f}',
        sep=' '
    )

main()