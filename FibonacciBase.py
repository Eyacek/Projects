#  File: FibonacciBase.py

#  Description: Converts integer number into fibonacci base number

#  Student Name: Evan Yacek

#  Student UT EID: ety78 

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 11/9/2015

#  Date Last Modified: 11/10/2015


def convert_fib_base(num):

    if num == 0:           #If user entered number is zero return zero
	    return[0]

    fibonacci_numbers = [2, 1]  #Create first terms for Fibonnacci sequence
    fibBase = []                #Create empty list to append ones and zeros 
    
        
		
    while(fibonacci_numbers[0]< num):     # While loop through range of numbers
	    fibonacci_numbers[0:0] = [sum(fibonacci_numbers[:2])]
    for x in fibonacci_numbers:
	    if x <= num:
		    fibBase , num = fibBase + [1], num - x #Append ones to fibBase
	    else:
		    fibBase.append(0)                          #Append zeros to fibBase
    return fibBase if fibBase[0] else fibBase[1:]      # Return lists of fibonnacci base numbers
	
	   
def main():
    integer = int(input("Enter a integer:"))          #Prompt User
    x = convert_fib_base(integer)                     #Convert fibonacci base
    y = ''.join(str(i) for i in x)                    #Convert list to string
    print(integer, "=" , y ,"(fib)")                  #Print string

main()
			
			
