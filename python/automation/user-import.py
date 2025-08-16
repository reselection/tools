import subprocess
import csv
from sys import platform

## Checks the OS, this script will only work on Linux.
if platform not in ('linux', 'linux2'):
    print(f'This script does not support {platform}')
    exit()

## Script for csv user creation, adds to group, sets shell & home
## Linux

def import_file(user_file):
    ## Prepares and opens the file for data manipulation.
    with open(user_file) as data:
        userdata = csv.DictReader(data)
        rows = list(userdata)
    
    ## Checks if groups exist
    for row in rows:
        group_name = row['group']
        result = subprocess.run(['getent', 'group', group_name], capture_output=True)
        if result.returncode != 0:
            create_group(group_name)

    ## Ask add/remove
    option = input("Add or remove users? (add / remove) ").lower()
    if option in ('add', 'a'):
        create_users(rows)
    elif option in ('remove', 'r'):
        delete_users(rows)

def create_users(users):
    ## Ask verbose once
    verbose = input("Verbose Y/n: ").lower() == 'y'
    for user in users:
        if verbose:
            print(f"Adding user: {user['username']}")

        result = subprocess.run([
            "useradd",
            "-m",
            "-d", user['home_dir'],
            "-s", user['shell'],
            "-g", user['group'],
            "-c", user['full_name'],
            user['username']
        ])

        if result.returncode != 0:
            print(f"Failed to add {user['username']}")
            continue

def delete_users(users):
    check = input("Delete ALL users from CSV? Y/n: ").lower()
    if check != 'y':
        print("Aborting...")
        return

    for user in users:
        username = user.get('username')
        if not username:
            continue
        print(f"Deleting user: {username}")
        subprocess.run(
            ["deluser", "--remove-home", username],
            check=True
        )


import_file('users.csv')
