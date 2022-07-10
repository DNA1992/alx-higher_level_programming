#!/usr/nin/python3


def uniq_add(my_list=[]):
    x = 0
    uniq = set(my_list)
    for y in uniq:
        x += y
    return x
