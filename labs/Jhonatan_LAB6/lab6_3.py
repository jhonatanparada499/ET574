# lab6_3.py – Jhonatan Parada

current_users = [
    'Admin',
    'napolEON',
    'jhonatan',
    'DAVID',
    'caroLine'
]

new_username = input("Enter your user name: ")

for username in current_users:
    if username.lower() == new_username.lower():
        print(f"Sorry {new_username}, that name is taken.")
        print(f"Current users: {current_users}")
        break # loop stops and else statement is ignored
else: 
    print(f"Great, {new_username} is still available.")
    current_users.append(new_username)
    print(f"Updated users: {current_users}")
