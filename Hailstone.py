#  File: Hailstone.py
 
#  Description:  Calculates the max cycle length of hailstone sequences in a user defined range. 
 
#  Evan Yacek
 
#  Date Created: 9/16/2015
 
#  Date Last Modified: 9/20/2015
 
 
def main():
 
   #Prompt the user to enter the starting number and ending number
   lo = int(input("Enter starting number of the range:"))
   hi = int(input("Enter ending number of the range:")) 
 
   #make sure that they are both positive, and that the starting number is less than the ending number. 
   if(lo <= 0 or hi <= 0):
      lo = int(input("Enter starting number of the range:"))
      hi = int(input("Enter ending number of the range:"))
   if(hi <= lo):
      lo = int(input("Enter starting number of the range:"))
      hi = int(input("Enter ending number of the range (greater than the starting number):"))
 
 
 
  #Define variable that I will be working with
   num = lo
   maxCycle = 0
   max_num = 0
 
  # The outer loop will find the numbers through the user given range
   while(num <= hi):
    n = num
    cycleLength = 0
    
 
 
  # The inner loop will calulate the cycle length for each of those numbers. 
    while(n > 1):
     if (n % 2 == 0):
      n = n // 2
      cycleLength = cycleLength + 1
     else:
      n = 3 * n + 1
      cycleLength = cycleLength + 1
 
  # Now we check to see if the newest cycle found will be greater than the previous.
    if(cycleLength > maxCycle):
     maxCycle = cycleLength
     lo = num
    num = num + 1
    
    
  #Find the maximum number if cycles are equal
    if(cycleLength == maxCycle):
     max_num = max(lo,num)
     
    
 
  # Return maxmimum number and maxiumum cycle, subtracting by one to account for the num +1 in loop. 
   print("The number", max_num-1  , "has the longest cycle length of" , maxCycle)
 
 
main()
