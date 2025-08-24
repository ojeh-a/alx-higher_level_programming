#!/usr/bin/python3
def no_c(my_string):
<<<<<<< HEAD
<<<<<<< HEAD
    my_string = my_string.translate({ord(i): None for i in "Cc"})
    return (my_string)
=======
	rem_char = "Cc"
	new_string = "".join(char for char in my_string if char not in rem_char)
	return new_string
>>>>>>> de9e906 (update from ubuntu)
=======
	rem_char = "Cc"
	new_string = "".join(char for char in my_string if char not in rem_char)
	return new_string
>>>>>>> de9e906 (update from ubuntu)
