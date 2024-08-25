#!/usr/bin/python3
class MyList(list):
    """Class that inherits from list with an additional method to
    print the list sorted."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
