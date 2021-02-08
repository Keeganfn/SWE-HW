#!/usr/bin/env python3

#Keegan Nave 
#tested with python3 and linux



def combine(first, last):

    try:
        first = str(first)
        last = str(last)
    except ValueError:
        print("You entered an invalid string, try again")
        return

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

    
