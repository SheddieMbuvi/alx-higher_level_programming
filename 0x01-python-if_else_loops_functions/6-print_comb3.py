#!/usr/bin/python3
for i in range(0, 8):
    for j in range(0, 10):
        if i < j:
            print("{:d}{:d}, ".format(i, j), end="")
print("{:02d}".format(89))
