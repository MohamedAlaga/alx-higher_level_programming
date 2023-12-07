#!/usr/bin/python3


class MyInt(int):
    def __eq__(self, __value: object) -> bool:
        return not super().__eq__(__value)
