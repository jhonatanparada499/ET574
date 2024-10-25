# lab7_7.py - Jhonatan Parada
err_msg = 'Invalid Input'
stop_char = '0'
prompt = f'Enter a number or {stop_char} to stop: '
nums_lst = []

input_val = input(prompt)

while input_val != stop_char:
    try:
        input_val = int(input_val)
        nums_lst.append(input_val)
        input_val = input(prompt)
    except:
        try:
            input_val = float(input_val)
            nums_lst.append(input_val)
            input_val = input(prompt) 
        except:
            print(err_msg)
            input_val = input(prompt)
else:
    if not nums_lst:
        pass
    else:
        lst_sum = sum(nums_lst)
        lst_averg = lst_sum / len(nums_lst)

        if len(str(lst_averg)) <= 3: # minimumm float value is 0.1 (1 decimal) (3 characters)
            lst_averg = int(lst_averg)

        print(f'Sum = {lst_sum}')
        print(f'Average = {lst_averg}')
        print('Number (s) entered:\n',*nums_lst)