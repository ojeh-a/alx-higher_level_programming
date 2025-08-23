#!/usr/bin/python3
def roman_to_int(roman_string):
    arabic = 0
    if roman_string is None or not str:
        return None
    numerical_values = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    for i in range(len(roman_string)):
        letter = roman_string[i]
        
        if i < len(roman_string) - 1 and numerical_values[letter] < numerical_values[roman_string[i + 1]]:
            arabic = arabic - numerical_values[letter]
        else:
            arabic = arabic + numerical_values[letter]
    return arabic
