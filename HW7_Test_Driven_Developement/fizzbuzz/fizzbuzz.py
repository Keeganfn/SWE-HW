#!/usr/bin/env python3

#Keegan Nave 
#tested with python3 and linux

def mult3(number):
    if(number % 3 == 0):
        return True 
    else:
        return False 
 
def mult5(number):
    if(number % 5 == 0):
        return True 
    else:
        return False 
    
def output(number):

    if(mult3(number) == True and mult5(number) == True):
        return "FizzBuzz"

    elif(mult3(number) == True):
        return "Fizz"

    elif(mult5(number) == True):
        return "Buzz"

    else:
        return number




if __name__ == "__main__":
    
    for i in range(1, 101):
        print(output(i))
