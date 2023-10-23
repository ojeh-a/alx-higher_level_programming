#!/user/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            if count < x:
                print('{}'.format(my_list[i]), end='')
                count += 1
            print()
            return (count)
        excep IndexError:
            print('')
            return (count)
