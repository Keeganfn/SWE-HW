#!/usr/bin/env python3

#Keegan Nave 
#tested with python3 and linux



def combine(first, last):

    #checks that they can be converted to strings
    try:
        first = str(first)
        last = str(last)
    except ValueError:
        print("You entered an invalid string, try again")
        return

    #checks that the strings are only letters and combines them 
    if(first.isalpha() and last.isalpha()):
        print(first + " " + last)
        return first + " " + last
    else:
        print("You entered an invalid string, try again")
        return
        

if __name__ == "__main__":
    
    first = "John"
    last = "Smith"

    print(combine(first, last))

    
