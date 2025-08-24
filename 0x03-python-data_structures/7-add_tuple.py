#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
def add_tuple(tuple_a=(), tuple_b=()):
    add = ()
    tuple_1 = tuple_a + (0, 0)
    tuple_2 = tuple_b + (0, 0)
    add_tuple = tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
    return (add_tuple)
=======
=======
>>>>>>> de9e906 (update from ubuntu)

def add_tuple(tuple_a=(), tuple_b=()):

    tuple_1 = (tuple_a + (0, 0))[:2]
    tuple_2 = (tuple_b + (0, 0))[:2]

    a1, a2 = tuple_1
    b1, b2 = tuple_2
    return ((a1 + b1, a2 + b2))
<<<<<<< HEAD
>>>>>>> de9e906 (update from ubuntu)
=======
>>>>>>> de9e906 (update from ubuntu)
