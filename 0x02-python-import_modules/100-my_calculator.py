#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    args_count = len(argv) - 1
    if args_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    operator = argv[2]
    b = argv[3]
    if operator == "+":
        print("{0} + {1} = {2}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{0} - {1} = {2}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{0} * {1} = {2}".format(a, b, mul(a, b)))
    elif operator == "/":
        print("{0} / {1} = {2}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
