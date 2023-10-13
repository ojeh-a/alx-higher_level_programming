#!/usr/bin/python3
def roman_to_int(roman_string):
    st = roman_string
    if st is None or not str:
        return None
    int_dict = {"I": 1, "V": 5, "X": 10, "L":
                50, "C": 100, "D": 500, "M": 1000}
    int_value = 0
    for i in range(len(st)):
        if i < len(st) - 1 and int_dict[st[i]] < int_dict[st[i + 1]]:
            int_value -= int_dict[st[i]]
        else:
            int_value += int_dict[st[i]]
    return int_value
