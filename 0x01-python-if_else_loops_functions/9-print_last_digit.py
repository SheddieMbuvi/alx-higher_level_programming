#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
        last = number % 10
        number = -number
        print("{:d}".format(last), end="")
        return last
    else:
        last = number % 10
        print("{:d}".format(last), end="")
        return last
