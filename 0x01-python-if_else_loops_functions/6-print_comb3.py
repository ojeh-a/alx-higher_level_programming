#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i + 1, 10):
        print("{}{}".format(i, j), end=', ' if i != 8 or j != 9 else '\n')
