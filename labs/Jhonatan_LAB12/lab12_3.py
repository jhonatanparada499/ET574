# lab12_3.py - Jhonatan Parada

def modify_file(file_target, action, content=''):
    if not isinstance(file_target, str):
        print(f'{file_target} must be a string')
        return
    
    if not isinstance(action, str):
        print(f'{action} must be a string')
        return
    
    if not isinstance(content, (list, tuple, str)):
        print(f'{content} must be a string or iterable')
        return

    if isinstance(content, (list, tuple)):
        content = '\n'.join(content)

    actions = ('write', 'append')
    action = action.lower()

    if not action in actions:
        print(f'{action} is not a valid action')
        print(f'valid actions: {actions}')
        return
    
    if action == 'append':
        content = '\n' + content

    try:
        file_target = open(file_target, action[0])
    except FileNotFoundError:
        print(f'{file_target} not found'); return
    
    file_target.write(content)
    file_target.close()