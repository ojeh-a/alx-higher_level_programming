#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []

    for i in range(list_length):
        try:
            divide = my_list_1[i] / my_list_2[i]
        except ValueError:
            divide = 0
            continue
        except TypeError:
            print("wrong type")
            divide = 0
            continue
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
            continue
        except IndexError:
            print("out of range")
            divide = 0
            continue
        finally:
            new_list.append(divide)
            list_length = len(new_list)
    return new_list
