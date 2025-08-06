#!/usr/bin/python3
<<<<<<< HEAD
def print_last_digit(number):
    if (number < 0):
        number = -1 * number
    number = (number % 10)
    print("{}".format(number), end='')
    return (number)
=======

def print_last_digit(number):
	last_digit = abs(number) % 10
	print(last_digit, end='')
	return last_digit

>>>>>>> de9e906 (update from ubuntu)
