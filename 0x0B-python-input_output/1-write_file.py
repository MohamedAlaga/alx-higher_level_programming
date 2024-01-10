#!/usr/bin/python3
"""
module to write to a file
"""
def write_file(filename="", text=""):
    with open(filename,encoding="utf-8") as f :
        i = 0
        while(f.write(text)):
            i+=1
        return i