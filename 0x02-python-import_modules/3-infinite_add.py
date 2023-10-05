#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    number = len(sys.argv) - 1
    add = 0

    for i in range(1, number + 1):
        argument = int(sys.argv[i])
        add += argument

    print("{}".format(add))
