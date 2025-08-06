#!/usr/bin/python3
import random
number = random.randint(-10, 10)
<<<<<<< HEAD
if (number < 0):
    print("{} is negative".format(number))
elif (number == 0):
    print("{} is zero".format(number))
else:
    print("{} is positive".format(number))
=======
# YOUR CODE HERE
if number > 0:
    print(f"{number} if positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
>>>>>>> de9e906 (update from ubuntu)
