#!/usr/bin/python3
def search_replace(my_list, search, replace):
    modified_list = []
    for element in my_list:
        if element == search:
            modified_list.append(replace)
        else:
            modified_list.append(element)
    return modified_list
