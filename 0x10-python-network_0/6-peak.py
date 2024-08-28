#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds a peak element in a list of unsorted integers"""
    
    def binary_peak(start, end):
        """Helper function to perform binary search for a peak"""
        if start == end:
            return list_of_integers[start]

        mid = (start + end) // 2

        # Check if mid is a peak
        if ((mid == 0 or 
             list_of_integers[mid] >= list_of_integers[mid - 1]) and
            (mid == len(list_of_integers) - 1 or 
             list_of_integers[mid] >= list_of_integers[mid + 1])):
            return list_of_integers[mid]

        if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            return binary_peak(start, mid - 1)

        # Otherwise, peak lies in the right half
        return binary_peak(mid + 1, end)

    if not list_of_integers:
        return None

    return binary_peak(0, len(list_of_integers) - 1)
