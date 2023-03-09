#!/usr/bin/python3
from sys import argv
def list_args():
    argv_len = len(argv[1:])

    if argv_len == 1:
        print(f"{argv_len} argument:")
        for i in range(1, argv_len + 1):
            print(f"{i}: {argv[i]}")
    else:
        print(f"{argv_len} arguments")
        for i in range(1, argv_len + 1):
            print(f"{i}: {argv[i]}")

if __name__ == "__main__":
    list_args()
