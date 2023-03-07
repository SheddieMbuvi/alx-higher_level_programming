#!/usr/bin/python3
for characters in range(97, 123):
    if characters != 101 and characters != 113:
        print("{:c}".format(characters), end="")
