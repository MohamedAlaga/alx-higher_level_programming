#!/usr/bin/python3
"""
module to make a class that inherts from a list
"""


class MyList (list):
    """
    class that in inherits from a list
    """

    def print_sorted(self):
        """
        print ascending sorted list
        """
        print(sorted(self))
