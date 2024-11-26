# lab11_4.py - Jhonatan Parada
class Stu:
    def __init__(self, name, gpa):
        self.stuInfo = {
            'name': name,
            'gpa': gpa
        }
    
stu_1 = Stu('tom cat', 3.456)
stu_2 = Stu('jerry mouse', 4.0)
stu_3 = Stu('Sponge bob', 3.99)

stuClass = [stu_1.stuInfo, stu_2.stuInfo, stu_3.stuInfo]

print('All students in this list:')
print(stuClass, end='\n\n')
print('All students information:')
for stuInfo in stuClass:
    print(
        'Student',
        stuClass.index(stuInfo) + 1,
        stuInfo
    )
else: print()

print('All gpa information:')
for stuInfo in stuClass:
    print(stuInfo['gpa'], end='|')
else: print('\n')

stuClass[-1]['gpa'] = 4.0
stu_4 = Stu('John Smith', 3.99)
stuClass.append(stu_4.stuInfo)

print('All updated information:')
for stuInfo in stuClass:
    print(
        f'{stuInfo['name']:<15}{stuInfo['gpa']:>5.2f}'
    )