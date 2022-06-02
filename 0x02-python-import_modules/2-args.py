#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args_len = len(sys.argv)
    if args_len == 1:
        print("0 arguments.")
    elif args_len == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(args_len - 1))
    for args in range(1, args_len):
        print("{}: {}".format(args, sys.argv[args]))
