#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str):
        return str
    else:
        nstr = str[:].replace(str[n], '')
        return nstr
