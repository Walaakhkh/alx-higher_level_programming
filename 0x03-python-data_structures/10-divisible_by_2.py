#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Use a list comprehension to create a new list of boolean values
    return [True if number % 2 == 0 else False for number in my_list]
