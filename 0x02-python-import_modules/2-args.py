#!/usr/bin/python3
if __name__ == '__main__':
<<<<<<< HEAD
<<<<<<< HEAD
    import sys

    number = len(sys.argv) - 1

    if (number == 1):
        print("1 argument:")

    elif (number == 0):
        print("0 arguments.")

    else:
        print("{} arguments:".format(number))

    for i in range(1, number + 1):
        argument = sys.argv[i]
        print("{}: {}".format(i, argument))
=======
=======
>>>>>>> de9e906 (update from ubuntu)
	from sys import argv
	number_of_arguments = len(argv)

	if number_of_arguments > 1:
		if number_of_arguments == 2:
			print(f"{number_of_arguments - 1} argument")
		else:
			print(f"{number_of_arguments - 1} Arguments")
		for argument in range(number_of_arguments - 1):
			print(f"{argument + 1}: {argv[argument + 1]}")

	else:
		print(f"0 Arguments")
<<<<<<< HEAD
>>>>>>> de9e906 (update from ubuntu)
=======
>>>>>>> de9e906 (update from ubuntu)
