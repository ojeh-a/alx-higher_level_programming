#!/usr/bin/python3
<<<<<<< HEAD
def multiple_returns(sentence):
    length = len(sentence)
    if sentence == "":
        first = None
    else:
        first = sentence[0]
    return (length, first)
=======

def multiple_returns(sentence):
    length = len(sentence)

    if sentence == "":
        first_character = None
    else:
        first_character = sentence[0]
    return ((length, first_character))
>>>>>>> de9e906 (update from ubuntu)
