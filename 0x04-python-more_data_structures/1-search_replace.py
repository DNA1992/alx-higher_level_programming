#!/usr/bin/python3


def search_replace(my_list, search, replace):
    newLis = []
    for x in my_list:
        if x == search:
            newLis += [replace]
        else:
            newLis += [x]
    return newLis
