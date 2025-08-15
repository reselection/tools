import os
import subprocess
import csv

## Checks the OS, this script will only work on Linux.
from sys import platform
if platform in('linux','linux2'):
    pass
elif platform not in ('linux','linux2'):
    print(f'This script does not support',platform)
    exit()

## Script for csv user creation, adds to group, sets shell & home
## Linux

def import_file(user_file):
    ## Main function
    ## Prepares and opens the file for data manipulation.
    ## Sends data over to other functions depending on input supplied
    with open(user_file) as data:
        userdata = csv.DictReader(data)
        rows = list(userdata)
 
    option = input("Add or remove users? (add / remove) ").lower()
    if option in('add','a'):
        create_users(rows)
    elif option in ('remove','r'):
        delete_users(rows)


def create_users(users):
    ## Ask verbose once
    verbose = input("Verbose Y/n: ").lower() == 'y'

    for user in users:
        if verbose:
            print(f"Adding user: {user['username']}")

        result = subprocess.run([
            "sudo"
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


def delete_users(*args):
    pass

def add_users_group(*args):
    pass

def remove_users_group(*args):
    pass

import_file('users.csv')