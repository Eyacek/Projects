#  File: Goldbach.py

#  Description: Outputs prime combinations of even numbers in a user defined range. In accordance to Goldbachs Conjecture

#  Evan Yacek

#  Date Created: 9/20/2015

#  Date Last Modified: 9/23/2015








def is_prime (n):               #Here I define my is_prime function so that I can call on it later
  limit = int (n ** 0.5) + 1
  divisor = 2
  while (divisor < limit):
    if (n % divisor == 0):
      return False
    divisor = divisor + 1
  return True
  
def main():
  
  lo = int(input("Enter the lower limit:")) # prompt the user to enter the range
  hi = int(input("Enter the upper limit:"))
  
  while (lo > hi) or (lo < 4) or (lo % 2 != 0) or (hi % 2 != 0): #Error check to maker numbers are even, greater than 4, and logical
    lo = int(input("Enter the lower limit:")) 
    hi = int(input("Enter the upper limit:"))
	
  num1 = lo                                    # Define variable I will be using
    
  while num1 <= hi:                            # Outer while loop through range (lo,hi)
      print(num1, end = '')
      n = 2
        
      while n <= (num1 // 2):                  #Inner loop to find prime combination num1 = n + n2 
          if not is_prime(n):                  #If n is not prime increase its value until is
              n += 1
          n2 = num1 - n                        #n2 will be the second prime number which is found by subtracting the first prime number n from num1
          if is_prime(n2):                     #check to see if n2 is prime
              if (n <= n2):                    #If check to not repeat vaules already found ex (3,5),(5,3)
                    
                  print(' =', n, '+', n2, end = '') #Print the prime number chain
             
          n += 1
      num1 += 2
      print()
    
           
main()
  
