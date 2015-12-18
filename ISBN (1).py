#  File: ISBN.py

#  Description: Returns if a given isbn is valid in an external txt file

#  Evan Yacek

#  Date Created: 10/18/2015

#  Date Last Modified: 10/20/2015


def remove_hyphen(h):         #define a function to remove all the "-" from each ISBN
  
  h = h.split("-")
  return ''.join(h)


def isValid(isbn):
  

  
  newIsbn = [] #set empty list for new formated isbns
  
  
  isbn = remove_hyphen(isbn.lower()) #converts all characters to lower case and removes the hyphens
  
  
  #If check to see if length is isbn is length 10 and that that it contains numbers with a digit or x as the last number
  
  if not ((len(isbn) == 10) and isbn[:-1].isdigit() and(isbn[-1] == 'x' or isbn[-1].isdigit())):
    return False
	
  for x in range(len(isbn)): # For loop through length of isbn
   
    
   if((ord(isbn[x]) >= 48) and (ord(isbn[x]) <= 57)):#If the digit is between numbers 0-9 append to new isbn
      newIsbn.append(eval(isbn[x]))
    
   elif(isbn[x] == 'x'):       #If the x character is there replace with 10 and append
      newIsbn.append(10)
    
    
  if(len(newIsbn) != 10):     #Check to make sure new isbn length is 10
    return False

  
  s1 = [newIsbn[0]]           #Set s1 to first term in new isbn
  
  for num in range(1,10):
    s1.append(int(s1[num-1]) + int(newIsbn[num])) #append each partial sum
	
  s2 = [s1[0]]                                #set s2 to first value of s1
  
  for num in range(1,10):
    s2.append(int(s2[num-1]) + int(s1[num]))      #append each partial sum of s1 to s2

  if s2[-1] % 11 == 0: #if the last digit of s2, the total sum, is divisible by 11 return True
    return True
  else:
    return False
  
      
 

def main():

  
  in_file = open('isbn.txt', 'r')         #Open both Files
  out_file = open('isbnOut.txt', 's')
  
   
  for line in in_file:                    #check to see if isbns are valid with isValid function
    if(isValid(line.strip())):
      out_file.write(line.strip() + '  valid\n')
    else:
      out_file.write(line.strip() + '  invalid\n')
  
  
  infile.close()                        #close both files
  outfile.close()
  
main()
