# lab12_3.py - Jhonatan Parada

file_target = 'data//Presidents4.txt'

presidents = (
    'George Washington',
    'John Adams',
    'Thomas Jefferson'
)

def write_to_file(file_target, content):
    if not isinstance(content, (list, tuple, str)):
        print(f'{content} must be an iterable')
        return

    if isinstance(content, (list, tuple)):
        content = '\n'.join(content)

    try:
        file_target = open(file_target, 'w')
    except FileNotFoundError:
        print(f'{file_target} not found'); return
    
    file_target.write(content)
    file_target.close()

write_to_file(file_target, presidents)

# def append_