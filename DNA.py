#  File: DNA.py

#  Description: Returns longest common DNA sequences between pairs of DNA from a txt file

#  Evan Yacek

#  Date Created: 10/11/2015

#  Date Last Modified: 10/13/2015


def main():
  # open file for reading
  in_file =  open ("./dna.txt", "r")

  # read number of pairs
  num_pairs = in_file.readline()
  num_pairs = num_pairs.strip()
  num_pairs = int (num_pairs)
  
  print('Longest Common Sequences')    # Print Header
  print('')
  
  # read each pair of dna strands
  for i in range (num_pairs):
    st1 = in_file.readline()
    st2 = in_file.readline()

    # remove white space from either end
    st1 = st1.strip()
    st2 = st2.strip()

    # make both strands upper case
    st1 = st1.upper()
    st2 = st2.upper()
	
    max_substring = [ ] # Set variable for list of longest sub string

  
    if (len(st1) > len(st2)):  #If the first string is greater than the second
      dna = len(st1)
      
      while(dna > 1):           #While loop through length of first strand 
      
        
        if(len(max_substring) > 0):  #Check to see if longest substring is found
          break
        
        
        count = 0   
   
        for n in range(dna + count, len(st1)+ 1): # For loop through first strand length to see if substring of equal length, and if so append
          
          if(st2.find(st1[count: count + dna]) > -1):
            max_substring.append(st1[count: count + dna])
            
          count += 1
         
        dna -= 1  

    
    else:             #If second string is longer than the first one
      dna = len(st2)
      
      while(dna > 1):           # while loop through length of second strand
        if(len(max_substring) > 0):
          break
          
        count = 0
        
        for m in range(dna + count , len(st2)+1): #For loop through second strand length
		 
          if(st1.find(st2[count: count + dna]) > -1):
            max_substring.append(st2[count: count + dna])
            
          count += 1
          
        dna -= 1
        
        
        
        
      
    
	
    print("Pair %d:" %(i + 1), end='')  #Print out Results
    
    if max_substring:
      for let in max_substring:
        print('\t%s' %let)
        
    else:
      print("\tNo Common Sequence Found")
    print('')
    
     
        
  
  in_file.close()
  
  
main()
      
