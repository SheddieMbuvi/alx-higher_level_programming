#!/usr/bin/python3
import calculator_1
import sys
if __name__ == "__main__":
    lim = len(sys.argv)
    if lim == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])

        if sys.argv[2] == "+":
            print("{:d} + {:d} = {:d}".format(a, b, calculator_1.add(a, b)))
        elif sys.argv[2] == "-":
            print("{:d} - {:d} = {:d}".format(a, b, calculator_1.sub(a, b)))
        elif sys.argv[2] == "*":
            print("{:d} * {:d} = {:d}".format(a, b, calculator_1.mul(a, b)))
        elif sys.argv[2] == "/":
            print("{:d} / {:d} = {:d}".format(a, b, calculator_1.div(a, b)))
        else:
            print(f"Unknown operator. Available operators: +, -, * and /")
    else:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
