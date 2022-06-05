#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for nums in my_list:
        if nums % 2 == 0:
            my_list[nums] = True
        else:
            my_list[nums] = False
    return my_list
