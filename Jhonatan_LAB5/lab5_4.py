err_message = 'Invalid Input.'
try:
    input_range = int(input("Enter a range: "))
    try:
        input_num = int(input("Enter an integer number: "))
        nums_list = [num for num in range(1, input_range + 1)]

        print(f'Multiplication Table of {input_num}')
        for num in nums_list:
            print(f'{num}\t*\t{input_num}\t=\t{num * input_num}')

    except ValueError:
        print(err_message)
except ValueError:
    print(err_message)