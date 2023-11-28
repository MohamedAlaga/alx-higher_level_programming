#!/usr/bin/python3
def no_c(my_string ):
    newString = ""
    for idx in range(len(my_string)):
        print( "old string is :"+ my_string+",new is "+newString )
        if my_string[idx] != 'c' or my_string[idx] != 'C':
            newString+=(my_string[idx])
    my_string = newString
