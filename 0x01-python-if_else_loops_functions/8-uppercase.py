#!/usr/bin/python3
def uppercase(str):
    result = ""
    for letter in str:
        if 'a' <= letter <= 'z':
            letter = chr(ord(letter) - ord('a') + ord('A'))
        result += letter
    print(result)
