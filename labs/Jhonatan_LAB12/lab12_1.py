# lab12_1.py - Jhonatan Parada

# .sh (Unix, bash)
my_file_path = 'data//Presidents.txt'

# .bat (Windows, cmd, powershell )
# my_file_path = 'data\\Presidents.txt'

def print_file_content(file_path, mode):
    if not isinstance(file_path, str):
        print(f'{file_path} must be a string'); return
    
    if not isinstance(mode, str):
        print(f'{mode} must be a string'); return

    modes = ('loop', 'list')
    mode = mode.lower()

    try: file_obj = open(file_path, 'r')
    except FileNotFoundError:
        print('file path not found'); return
    
    if not mode in modes:
        print('invalid mode')
        file_obj.close()
        return

    # print the contents using loop or list
    if mode == 'loop':
        for line in file_obj:
            print(line.strip())

    elif mode == 'list':
        print(*file_obj.readlines(),sep='')

    file_obj.close()

print_file_content(my_file_path, 'loop')
print_file_content(my_file_path, 'list')