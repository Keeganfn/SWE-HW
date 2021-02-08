#!/usr/bin/env python3

#Keegan Nave 
#tested with python3 and linux



def get_volume(x, y, z):
    #checks that valid numbers have been entered
    try:
        x = float(x)
        y = float(y)
        z = float(z)
    except ValueError:
        print("Not a valid number, try again")
        return;

    #checks that numbers are positive
    if(x < 0 or y < 0 or z < 0):
        print("The number you entered is negative, try again")
        return;

    #returns volume
    else:
        volume = x * y * z
        print(volume)
        return volume


if __name__ == "__main__":
    print(get_volume(5.5,5,5))

    
