#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_integers = set()
    for n in my_list:
        if isinstance(n, int):
            uniq_integers.add(n)
    sum_uniq_integers = sum(uniq_integers)
    return sum_uniq_integers
