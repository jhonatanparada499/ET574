# lab12_3.py (script part)
from modules import file

def main():    
    # .sh (Unix, bash)
    my_file_target = 'data//Presidents4.txt'

    # .bat (Windows, cmd, powershell )
    # my_file_target = 'data\\Presidents4.txt'

    presidents = (
        'George Washington',
        'John Adams',
        'Thomas Jefferson',
        'James Madison',
        'James Monroe',
        'John Quincy Adams'
    )

    file.modify(my_file_target, 'write', presidents[:3])
    file.modify(my_file_target, 'append', presidents[3:])
    file.print_content(my_file_target, 'loop')

if __name__ == '__main__': main()