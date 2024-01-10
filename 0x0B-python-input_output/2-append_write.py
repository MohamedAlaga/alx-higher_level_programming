#!/usr/bin/python3
"""
module to append to a file
"""
def append_write(filename="", text=""):
    with open(filename,'a',encoding='utf-8') as f :
        i = 0
        while(f.write(text)):
            i += 1
            return i