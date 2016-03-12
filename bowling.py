#  File: Bowling.py
#  Description: Outputs total score of bowling game from text file. 
#  Student's Name: Evan Yacek
#  Student's UT EID: ety78
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 2/1/2016
#  Date Last Modified: 2/5/2016


def bowlScore(balls, frames=1, scores=0):              #This function ultimately calculates the total score of a bowling game, the input is a list
	if frames > 10 or not balls:
		print ("", scores ,end = "")                   #For each if statement I print out the total score, keeping track per frame
		return scores
	elif balls[0] == 10:
		balls = balls[1:]
		bonus = sum(balls[0:2]) if balls else 0        #Account for the bonus for strikes
		print ('',scores, end ="")
		return bowlScore(balls, frames + 1, scores + 10 + bonus) #recursive function adding to balls, frame, bonus, and score
	elif len(balls) == 1:
		print("",scores,end = "")
		return scores + balls[0]                       
	elif sum(balls[0:2]) == 10:
		balls = balls[2:]
		bonus = balls[0] if balls else 0               #Account for the bonus with spares
		print("", scores, end ="")
		return bowlScore(balls, frames + 1, scores + 10 + bonus)
	else:
		print(" ", scores,end ="")
		scores += sum(balls[0:2])
        
		return bowlScore(balls[2:], frames + 1, scores)


def main():

	
  
	in_file = open ("./scores.txt", "r")              # open file for reading
	num_lines = sum(1 for line in open('scores.txt')) #Count number of lines in file which I will be using for my range
  
  
	grid = []  #create a list I will be appending to
  

	for i in range (num_lines):  # read data line by line
		line = in_file.readline()
		newline = line.strip().replace("X","10").replace("/","43").replace("-","0") #Replace characters with integer values, "43" will be replaced later
	

    
		nums = newline.split()         #split each character in line into list
		nums = [int(i) for i in nums]  #convert to integers
		for n,i in enumerate(nums):
			if i == 43:
				nums[n]= 10 - nums[n-1]       #convert 43 to actual integer of number of pins knocked down on spare
	    
	
		grid.append (nums) #append each list to grid
	for entry in grid:
		print(  "  1     2   3   4   5   6   7    8   9   10")
		print("+----+----+---+---+---+---+---+---+---+-----+")
		print("|    |    |   |   |   |   |   |   |   |     |")
		print(entry)                                            #For some reason I could not print "line" without disrupting my output, so I chose to print the list, or each entry in my grid
		print(" ", bowlScore(entry))                            #I had trouble formating my output keeping my data within the frames, and printing the original inputs from the text file
		print("|    |    |   |   |   |   |   |   |   |     |")
		print("+----+----+---+---+---+---+---+---+---+-----+")
main()