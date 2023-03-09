#!/usr/bin/python3
from sys import argv
def list_args():
    argv_len = len(argv)

    if argv_len == 1:
        print("{} arguments.".format(0))

    elif argv_len == 2:
        print("{} argument:".format(argv_len - 1))
        for i in range(1, argv_len):
            print(f"{i}: {argv[i]}")
    else:
        print("{} arguments:".format(argv_len - 1))
        for i in range(1, argv_len):
            print(f"{i}: {argv[i]}")

if __name__ == "__main__":
    list_args()
