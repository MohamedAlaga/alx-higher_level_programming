#!/usr/bin/python3
"""
module to read a file
"""
def read_file(filename=""):
    """
    function to read a file
    """
    with open (filename,encoding='utf-8') as f :
        read_file = f.read()
        print(read_file)
