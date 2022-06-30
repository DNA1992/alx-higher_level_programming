#!/usr/bin/python3
def uppercase(str):
    strup = ""
    for x in range(len(str)):
        if ord(str[x]) >= ord('a') and ord(str[x]) <= ord('z'):
            strup = ord(str[x]) - 32
        else:
            strup = ord(str[x])
            print("{:c}".format(strup), end="")
        print()
