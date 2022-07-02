#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newi = list(my_list)
    if idx < 0:
        return newi
    elif idx > len(my_list) - 1:
        return newi
    else:
        new_list(idx) = element
        return newi
