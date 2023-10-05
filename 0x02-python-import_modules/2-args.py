#!/usr/bin/python3
if __name__ == '__main__':
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
