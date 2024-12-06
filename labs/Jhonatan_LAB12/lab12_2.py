# lab12_2.py - Jhonatan Parada

def create_file(full_name, content=''):
    if not isinstance(full_name, str):
        print(f'{full_name} must be a string')
        return

    if not isinstance(content, (list, tuple, str)):
        print(f'{content} must be a string or iterable')
        return

    if isinstance(content, (list, tuple)):
        content = '\n'.join(content)

    try:
        new_file = open(full_name, 'x')
    except FileNotFoundError:
        print(f'{full_name} not found'); return
    except FileExistsError:
        print(f'{full_name} already exists'); return

    new_file.write(content)
    new_file.close

def main():
    # .sh (Unix, bash)
    new_file_1 = 'data//Presidents2.txt'
    # .sh (Unix, bash)
    new_file_2 = 'data//Presidents3.txt'

    # .bat (Windows, cmd, powershell )
    # my_file_1 = 'data\\Presidents2.txt'

    # .bat (Windows, cmd, powershell )
    # my_file_2 = 'data\\Presidents3.txt'

    presidents = (
        'George Washington',
        'John Adams',
        'Thomas Jefferson'
    )

    create_file(new_file_1, presidents[:2])
    create_file(new_file_2, presidents)

if __name__ == '__main__': main()