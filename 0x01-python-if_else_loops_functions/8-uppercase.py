def uppercase(s):
    result = ""
    for letter in s:
        if 'a' <= letter <= 'z':
            letter = chr(ord(letter) - ord('a') + ord('A'))
        result += letter
    print(result)
