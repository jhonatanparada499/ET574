# lab11_1.py - Jhonatan Parada

stuInfo = {
    'name': 'John Smith',
    'gpa': 3.456,
    'age': 20
}

for k,v in stuInfo.items(): 
    print(f'{k.upper()}\t{v}')
else: print()

stuInfo.update({'gpa': 4.0})

for k in stuInfo.keys(): 
    print(f'{k.upper()}\t{stuInfo[k]}')
else: print()

stuInfo.setdefault('major', 'CSIS')

for v in stuInfo.values(): 
    print(v, end='|') 
else: print('\n')

stuInfo.pop('gpa')
del stuInfo['age']

print(stuInfo)