#!/usr/bin/python3
"""
module to write to a file
"""
def write_file(filename="", text=""):
    with open(filename,encoding="utf-8") as f :
        f.write(text)