#!/usr/bin/python3
def fizzbuzz():
<<<<<<< HEAD
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
=======
	for number in range(100):
		number += 1
		if number % 3 == 0 and number % 5 == 0:
			print("FizzBuzz", end=' ')
			continue
		elif number % 3 == 0:
			print("Fizz", end=' ')
			continue
		elif number % 5 == 0:
			print("Buzz", end=' ')
			continue
		print(number, end=' ')
>>>>>>> de9e906 (update from ubuntu)
