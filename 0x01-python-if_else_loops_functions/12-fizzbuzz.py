#!/usr/bin/python3
def fizzbuzz():
    integer = 1
    while (integer <= 100):
        if (integer % 3 == 0 and integer % 5 == 0):
            print("FizzBuzz", end=" ")
        elif (integer % 5 == 0):
            print("Buzz", end=' ')
        elif (integer % 3 == 0):
            print("Fizz", end=' ')
        else:
            print("{}".format(integer), end=' ')
        integer += 1
