#  File: Books.py

#  Description: Compares the vocabulary computationally through comparison of two texts and a dictionary

#  Student Name: Evan Yacek

#  Student UT EID: ety78

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 11/25/2015

#  Date Last Modified: 11/30/2015


word_dict = {}                            #create global var
def create_word_dict ():                  #Creates a dictionary from word list
    dict = open('words.txt', 'r')
    for line in dict:
        word_dict[line.strip()] = 1
    
    dict.close()


def parseString (st):  # Removes punctuation from string and creates new one
    st2 = ''
  
    for x in range(len(st)):
    
          if(st[x].isalpha() or st[x].isspace()): st2 += st[x] 
    
          elif(st[x] == '\'' and st[x+1] != '\'s' ): st2 += st[x]
    
          else: st2 += ' '

    return  st2


def getWordFreq (file): # Returns a dictionary of words and their frequencies
    freqDict = {}
  
    inFile = open(file, 'r') #open book
  
  
    for line in inFile:               #format for punctuation checking for apostrosphe and s
        line = line.rstrip()
        line = line.replace('-', ' ')
        if(line.endswith('\'')): line = line[:len(line) - 1]
        elif(line.endswith('\'s')): line = line[:len(line) - 2]
      
        for word in (parseString(line)).split():
            if word in freqDict: freqDict[word] += 1
            else: freqDict[word] = 1
        
  
    inFile.close() # Close Book
        
  
    capList = []                 #Add all the capital words to a list
    for key in freqDict:
      if(key[0].isupper()):
        capList.append(key)
    
   
    for st in capList:
    
      if(st.lower() in freqDict): #If word is lowercase add to the entry freqDict
        freqDict[st.lower()] += freqDict[st]
    
      elif(st.lower() in word_dict): #If word is in dictionary replace with lowercase form
        freqDict[st.lower()] = freqDict[st]
    
      del freqDict[st] #Delete capitilized version from dictionary
 
    
    return freqDict
  
def word_total(freqDict):
  total = 0
  for entry in freqDict:
    tota1 += freqDict[entry]
  return total 
  
# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
    
  totalBook1 = 0                #Set Initial Variables
  wordsBook1 = 0
  for x in freq1:
      totalBook1 += freq1[x]
      wordsBook1 += 1
  totalBook2 = 0
  wordsBook2 = 0
  for y in freq2:
      totalBook2 += freq2[y]
      wordsBook2 += 1
  numWords1 = set(freq1)
  numWords2 = set(freq2)
  diff1 = numWords1 - numWords2    #Calculate word differences
  diff2 = numWords2 - numWords1
  count1 = 0
  for num in diff1:
      count1 += freq1[num]
  count2 = 0
  for num in diff2:
      count2 += freq2[num]
  
  #Print results
  print()
  print(author1)
  print('Total distinct words =', wordsBook1)
  print('Total words (including duplicates) =', totalBook1)
  print('Ratio (% of total distinct words to total words) =', format(wordsBook1 * 100 / totalBook1, '.10f'))
  print()
  print(author2)
  print('Total distinct words =', wordsBook2)
  print('Total words (including duplicates) =', totalBook2)
  print('Ratio (% of total distinct words to total words) =', format(wordsBook2 * 100 / totalBook2, '.10f'))
  print()
  print('%s used %d words that %s did not use.' %(author1, len(diff1), author2))
  print('Relative frequency of words used by %s not in common with %s =' %(author1, author2), format(count1/totalBook1*100,'.10f'), end = '\n\n')
  print('%s used %d words that %s did not use.' %(author2, len(diff2), author1))
  print('Relative frequency of words used by %s not in common with %s ='  %(author2, author1), format(count2/totalBook2*100,'.10f'), end = '\n\n')


def main():
  # Create word dictionary from comprehensive word list
  create_word_dict()

  # Enter names of the two books in electronic form
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")
  print()

  # Enter names of the two authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  print() 
  
  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)

  # Compare the relative frequency of uncommon words used
  # by the two authors
  wordComparison (author1, wordFreq1, author2, wordFreq2)

main()