#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        counter = 0
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            counter += 1
        print()
    except IndexError:
        print()
        return counter
    return counter
