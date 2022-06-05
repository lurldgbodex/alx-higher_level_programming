#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        max_no = my_list[0]
        for nums in my_list:
            if nums > max_no:
                max_no = nums
        return max_no
