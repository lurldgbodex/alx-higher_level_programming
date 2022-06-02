#!/usr/bin/python3
def remove_char_at(str, n):
    nstr = str[:].replace(str[n], '')
    return nstr
