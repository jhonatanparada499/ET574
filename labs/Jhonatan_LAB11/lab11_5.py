# lab11_5.py - Jhonatan Parada

def createUser(**kwargs): return kwargs

def printUser(user):
    for k, v in user.items():
        print(f'{k}: {v}')

user_1 = createUser(
    name='John',
    age=43,
    job='Programmer',
    hobby='Biking'
)
printUser(user_1); print()

user_2 = createUser(
    name='Sara',
    age=20,
    school='QCC',
    major='CSIS'
)
printUser(user_2)