#!/usr/bin/python3
"""
module for combaring ints
"""


class MyInt(int):
    """
    class inherst from int
    """

    def __eq__(self, __value: object) -> bool:
        """
        return false if value equal
        """

        return not super().__eq__(__value)

    def __ne__(self, __value: object) -> bool:
        """
        return true if values not equivelent
        """
        return not super().__ne__(__value)
