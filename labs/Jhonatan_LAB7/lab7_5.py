# lab7_5.py - Jhonatan Parada
import random

prompt_1 = 'Enter the number of grades in the list: '
prompt_2 = 'Enter the passing grades:'
err_msg = 'Invalid Input.'
min_grade = 1
max_grade = 100

lst_len = 0
pass_grade = 0
all_grades = []
pass_grades = []

lst_len = input(prompt_1)
while not isinstance(lst_len, int):
    try:
        lst_len = int(lst_len)
        pass_grade = input(prompt_2)
        
        while not isinstance(pass_grade, int):
            try:
                pass_grade = int(pass_grade)
            except:
                print(err_msg)
                pass_grade = input(prompt_2)            
    except:
        print(err_msg)
        lst_len = input(prompt_1)

for i in range(lst_len):
    new_grade = random.randint(min_grade, max_grade)
    all_grades.append(new_grade)

    if new_grade >= pass_grade: 
        pass_grades.append(new_grade)

print(f'Updated List: {pass_grades}')
print(f'Original List: {all_grades}')