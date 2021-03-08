#!/usr/bin/env python3

#Keegan Nave 
#tested with python3 and linux

def div4(number):
    if(number % 4 == 0):
        return True
    else:
        return False


def div100(number):
    if(number % 100 == 0):
        return True
    else:
        return False

def div400(number):
    if(number % 400 == 0):
        return True
    else:
        return False

def leap_check(number):
    if(div4(number) == True):
        if(div100(number) == True):
            if(div400(number) == True):
                return True
            
            else:
                return False
        else:
            return True
    else:
        return False

if __name__ == "__main__":

  
    year = int(input("Please enter your year: "))
    result = leap_check(year)

    if(result == True):
        print("It is a leap year")
    else:
        print("It isnt a leap year")

