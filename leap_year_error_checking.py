#!/usr/bin/env python3

#Keegan Nave 
#tested with python3 and linux



flag = True

#gets user input and does error checking
while(flag):
    flag = False
    year = input("Please enter your year: ")
    
    if(not year.isdigit()):
        print("Not a valid year, try again")
        flag = True

    else:
        year = int(year)

#implements the logic from my flowchart 
if(year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print(str(year) + " is a leap year.")

        else:
            print(str(year) + " is not a leap year.")

    else:
        print(str(year) + " is a leap year.")

else:
    print(str(year) + " is not a leap year.")
