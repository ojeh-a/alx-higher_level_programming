#!/usr/bin/python3
<<<<<<< HEAD
for i in range(0, 9):
    for j in range(i + 1, 10):
        print("{}{}".format(i, j), end=', ' if i != 8 or j != 9 else '\n')
=======

for first_number in range(9):
    for second_number in range(first_number + 1, 10):
        print(f"{first_number}{second_number}", end='\n'
              if first_number == 8 and second_number == 9
                else ', ')
>>>>>>> de9e906 (update from ubuntu)
