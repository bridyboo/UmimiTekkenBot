import win32api as wapi
import time

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    keyList.append(char)

def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    if 'H' in keys:
        return 'H'
    elif 'B' in keys:
        return 'B'
    elif 'W' in keys:
        return 'W'
    elif 'Z' in keys:
        return 'Z'
    elif ' ' in keys:
        return ' '
    else:
        return 'W'