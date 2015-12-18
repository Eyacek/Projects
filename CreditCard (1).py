#  File: CreditCard.py

#  Description: Returns the type and if the credit card is valid from a user entered credit card number

#  Student Name: Evan Yacek

#  Student UT EID: ety78

#  Course Name: CS 303E

#  Unique Number:  50475

#  Date Created: 10/21/2015

#  Date Last Modified: 10/23/2015



def is_valid(creditNumber):                                  #Determines if Credit Card is Valid using Luhn's Test
    num = [int(val) for val in str(creditNumber)][::-1]      #[::1] will reverse the order here
    return (sum(num[0::2]) + sum(sum(divmod(x*2,10)) for x in num[1::2])) % 10 == 0 #divmod here splits two numbers so we can complete our summing of the odds
    


	
def cc_type(creditNumber):  #Determines type of Credit Card
  
  diglist = []
  creditLength2 = len(str(creditNumber))
  
  for x in range (creditLength2):               #Append each number to the list
    diglist.append(creditNumber % 10)
    creditNumber = creditNumber // 10
	
  
  
  for x in range (creditLength2 // 2):                      #Flip to read left to right
    diglist[x],diglist[creditLength2 - 1 - x] = diglist[creditLength2 - 1 - x], diglist[x]
	
	
  
  
  d15 = (diglist[0])                                       #Create strings of first, second, third, and fourth numbers
  d14 = str(diglist[0])+str(diglist[1])
  d13 = str(diglist[0])+str(diglist[1]) + str(diglist[2])
  d12 = str(diglist[0])+str(diglist[1])+str(diglist[2])+str(diglist[3])
  
  if (d14 == '34' or d14 == '37'):
        type = "American Express"
  elif (d12 == '6011' or d13 == '644' or d14 == '65'):  #Determine type of card if string matches
        type = "Discover"
  elif (d14 >= '50' and d14 <= '55'):
        type = "MasterCard"
  elif d15 == 4:
        type = "Visa"
  else:
        type = ""

  return type
   

def main():

  creditNumber = int(input('Enter a 15 or 16-digit credit card number: ')) #Prompt the user to enter Credit Card Number
  length2 = len(str(creditNumber))
  
   
  if (length2 < 15 or length2 > 16):                   #Check to see if Credit Card is proper length
        print("")
        print ("Not a 15 or 16-digit number")
        return ''
  
  if(is_valid(creditNumber)):                          #Check to see if Valid using predefined funcion, if so print. Else Invalid.
    print("")
    print('Valid ' + cc_type(creditNumber) + ' credit card number')
  else:
    print("")
    print('Invalid credit card number')

  
main()