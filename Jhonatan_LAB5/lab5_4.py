num_padding = 4
err_message = 'Invalid Input.'
try:
    input_range = int(input("Enter a range: "))
    try:
        input_num = int(input("Enter an integer number: "))
        nums_list = list(range(1,input_range + 1)) # [num for num in range(1, input_range + 1)] #

        print(f'Multiplication Table of {input_num}')
        for num in nums_list:
            row = f'{num}\t*\t{input_num}\t=\t{num * input_num}'
            print(row.expandtabs(num_padding)) 

    except ValueError:
        print(err_message)
except ValueError:
    print(err_message)