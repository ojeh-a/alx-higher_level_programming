#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for element in row:
            print('{:d}'.format(element), end=' '
                  if element != row[-1] else '')
        print()
=======
=======
>>>>>>> de9e906 (update from ubuntu)

def print_matrix_integer(matrix=[[]]):
	for row in matrix:
		[print(element, end=' ' if element != row[-1] else '') for element in row]
		print()
<<<<<<< HEAD
>>>>>>> de9e906 (update from ubuntu)
=======
>>>>>>> de9e906 (update from ubuntu)
