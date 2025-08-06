#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
<<<<<<< HEAD

    """
    This function replaces an element of a list at a specific position

    Parameters:
    - my_list: list of integers.
    - idx: index to be replaced
    - element: replacement.
    """

    if idx < 0 or idx >= len(my_list):
        return (my_list)
    my_list[idx] = element
    return (my_list)
=======
	if idx < 0:
		return my_list
	elif idx > len(my_list):
		return my_list
	else:
	 my_list[idx] = element
	 return my_list
>>>>>>> de9e906 (update from ubuntu)
