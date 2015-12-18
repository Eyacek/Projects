# File: Deal.py

# Description: Program that calculates the probability of switching doors vs not switching doors in Game in which there are 3 doors and one is chosen

# Student Name: Evan Yacek

# Student UT EID: ety78

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 10/5/15

# Date Last Modified: 10/5/15






import random




def main():
  
  
	gameNumber = int( input ("Enter number of times you want to play: ")) #Prompt User
	switchWins = 0                                                        #Define Variables
	newGuess = 0
	
 
 
  
	print("")
  
	print("  Prize      Guess       View    New Guess")                   #Format Columns
 
	for x in range (1, gameNumber + 1):                                   #Outer For loop through user defined range of games
		prize = random.randint(1, 3)
		guess = random.randint(1, 3)
		view = random.randint(1, 3)                                       #Generate random integers for prize,guess, and view
	
	
		while (view == prize or view == guess):                           #While loop until view is different than prize and guesss
			view = random.randint(1, 3)
	  
    
	
		for y in range(1,4):                                              # For loop to obtain value for newGuess
			if(y != view) and (y != guess):
				newGuess = y
	  
		if (newGuess == prize):                                           #Count the number of times won if the doors were switched
			switchWins += 1
		
		print("   ", prize, "        ", guess, "        ", view, "	    ", newGuess)      #Format output
		x += 1
		
	print("")
	print("Probability of winning if you switch = ", "{:.2f}".format(round(switchWins/gameNumber, 2)))               #Format output and caculate probabilities
	print("Probability of winning if you do not switch = ", "{:.2f}".format(round(1 - switchWins/gameNumber,2)))

main()