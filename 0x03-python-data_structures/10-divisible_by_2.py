#!/usr/bin/python3 
def divisible_by_2(my_list=[]):
result = [num % 2 == 0 for num in my_list]
    return result

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 6]
    result = divisible_by_2(my_list)
    print(result)
