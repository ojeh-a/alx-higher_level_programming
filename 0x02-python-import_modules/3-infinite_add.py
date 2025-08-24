#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
if __name__ == '__main__':
    import sys

    number = len(sys.argv) - 1
    add = 0

    for i in range(1, number + 1):
        argument = int(sys.argv[i])
        add += argument

    print("{}".format(add))
=======
=======
>>>>>>> de9e906 (update from ubuntu)
if __name__ == "__main__":
	from sys import argv
	result = 0
	for arg in range(1, len(argv)):
		result = int(argv[arg]) + result
	print(result)	
<<<<<<< HEAD
>>>>>>> de9e906 (update from ubuntu)
=======
>>>>>>> de9e906 (update from ubuntu)
