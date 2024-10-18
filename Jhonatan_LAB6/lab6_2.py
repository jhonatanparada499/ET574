# lab6_2.py – Jhonatan Parada

user_grtng = 'thank you for logging in again!'
admin_grtng = 'would you like to see a status report?'
no_users_msg = 'We need to find some users.'

usernames = [
    'tom',
    'jerry',
    'bob',
    'dora',
    'admin'
]

# usernames.clear()

if not usernames:
    print(no_users_msg)
else:
    for username in usernames:
        if username != 'admin':
            print(f"Hello {username.capitalize()}, {user_grtng}")
        else:
            print(f"Hello {username.upper()}, {admin_grtng}")
    