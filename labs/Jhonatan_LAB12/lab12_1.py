# lab12_1.py - Jhonatan Parada

def print_file_content(file_path, mode):
    if not isinstance(file_path, str):
        print(f'{file_path} must be a string'); return
    
    if not isinstance(mode, str):
        print(f'{mode} must be a string'); return

    try: file_obj = open(file_path)
    except FileNotFoundError:
        print('file path not found'); return

    modes = ('loop', 'list')
    mode = mode.lower()
    
    if not mode in modes:
        print(f'{mode} is not a valid mode')
        print(f'valid modes: {modes}')
        file_obj.close()
        return

    # print the contents using loop or list
    if mode == 'loop':
        for line in file_obj:
            print(line.strip())

    elif mode == 'list':
        print(*file_obj.readlines(),sep='')

    file_obj.close()

def main():
    # .sh (Unix, bash)
    my_file_path = 'data//Presidents.txt'

    # .bat (Windows, cmd, powershell )
    # my_file_path = 'data\\Presidents.txt'

    print('Using Loop:')
    print_file_content(my_file_path, 'loop')
    print('\nUsing List:')
    print_file_content(my_file_path, 'list')

if __name__ == '__main__': main()