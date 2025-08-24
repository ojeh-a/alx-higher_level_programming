#!/usr/bin/python3
def new_in_list(my_list, idx, element):
<<<<<<< HEAD
<<<<<<< HEAD
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    new_list = my_list.copy()
    new_list[idx] = element
    return (new_list)
=======
=======
>>>>>>> de9e906 (update from ubuntu)
	new_list = my_list[:]

	if idx < 0:
		return new_list
	elif idx > len(my_list):
		return new_list
	else:
		new_list[idx] = element
		return new_list
<<<<<<< HEAD
>>>>>>> de9e906 (update from ubuntu)
=======
>>>>>>> de9e906 (update from ubuntu)
