#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
<<<<<<< HEAD
    if my_list is not None:
        my_list = reversed(my_list)
        for i in (my_list):
            print("{:d}".format(i))
=======
	[print(f"{item}") for item in reversed(my_list)]
>>>>>>> de9e906 (update from ubuntu)
