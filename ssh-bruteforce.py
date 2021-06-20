#!/bin/python3

import socket
import time

host = input("Enter IP address ")
if not host:
    print("Please enter a IP address.")
    quit()
port = input("Enter port: ")
if not port:
    port = 22
username = input("username: ")
if not username:
    username = open("data/usernames.txt","r")
    users = username.read()
wordlist = open("data/rockyou.txt",'r')




