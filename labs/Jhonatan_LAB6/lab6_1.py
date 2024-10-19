# lab6_1.py – Jhonatan Parada

err_msg = 'invalid age'
vowels = tuple('aeuio')

ages = [
    ['baby', 2],
    ['toddler', 4],
    ['kid', 13],
    ['teenager', 20],
    ['adult', 65],
    ['elder', float('inf')] # represents infinite age
]

try: 
    user_age = int(input('Please enter your age: '))

    for age in ages:
        life_stage = age[0]
        stage_age = age[1]

        if user_age < 0:
            print(err_msg)
            break # stops for loop
        else:
            if user_age < stage_age:
                a_an = 'an' if life_stage.startswith(vowels) else 'a'
                print(f"You're {a_an} {life_stage}.")
                break # stops for loop
    
except ValueError:
    print(err_msg)    