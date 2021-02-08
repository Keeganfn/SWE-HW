#!/usr/bin/env python3

#Keegan Nave 
#tested with python3 and linux



def average_list(user_list):

   #checks for empty list
    if(len(user_list) == 0):
        print("You entered an empty list, try again")
        return
 
    count = 0
    total = 0
    #checks to see if it is a valid number, if it is we increment count and add to total
    for i in user_list:
        try:
            i = float(i)
        except ValueError:
            print("You had an invalid number, try again")
            return
        count+=1
        total+=i

    #checks to make sure we dont divide by 0 and returns answer
    if(total != 0):
        print(total/count)
        return total/count
    else:
        print("You entered a list with only 0's, try again")
        return 

   

    

if __name__ == "__main__":

    test = [1, 2, 3, 4]

    print(average_list(test))

    
