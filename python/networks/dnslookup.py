#!/bin/python3
import socket

#small script that looks up a dns domain and returns IPv4 & IPv6 address

target = input("Enter domain name: ")
port = 22 # port isn't really used in here, so its 22 by default(SSH)
try:
    print("IPv6: ")
    print(socket.getaddrinfo(target,port)[0])
    print('\n')
    print("IPv4: ")
    print(socket.getaddrinfo(target,port)[3])

except:
    print("Could't find domain, try again.\nMake sure input is correct!")
