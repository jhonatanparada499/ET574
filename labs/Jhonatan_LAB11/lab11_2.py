# lab11_2.py - Jhonatan Parada

rank = {
    1:"Freshman",
    2:"Sophmore",
    3:"Junior",
    4:"Senior"
}

years = input(
    f'Enter the # of years in the school <1-{len(rank)}>: '
)

try: 
    years = int(years)
except:
    print('Invalid input')

if isinstance(years, int):
    if 1 < years > len(rank):
        print('Invalid years.')
    else: 
        print(f'Year {years} = {rank[years]}')