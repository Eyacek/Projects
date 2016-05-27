#  File: numberPath.py
#  Description: finds a path of numbers in grid that equal a target value  
#  Student's Name: Evan Yacek
#  Student's UT EID: ety78
#  Course Name: CS 313E 
#  Unique Number: 50940
#  Date Created: 4/12/2016
#  Date Last Modified: 4/14/2016


class Problem():

	def __init__(self,startRow, startCol, grid, sum, pathHistory):         #Create instance variables
		self.grid = grid
		self.pathHistory = pathHistory
		self.startRow = startRow
		self.startCol = startCol
		self.sum = sum
		self.startData = self.grid[self.startRow][self.startCol]
	
	def __str__(self):                              #Method to print Grid 
		string = ""
		for i in range(len(self.grid)):
			for j in range(len(self.grid[i])):
				string += str(self.grid[i][j]).center(10)
			if(i != len(self.grid)-1):
				string = string + "\n"
		return string
	
	
	def initialValue(self):              #Returns the starting point of the data
		return self.startData
	
	
	def showPath(self):                  #Gets the path when called upon 
		
		list = []
		for i in range(len(self.pathHistory)):
			list.append(self.pathHistory[i])
		return list
		
	
		
		
	def promblemInitializer(self):       #Keeps track of the path, sum, and replaces grid values with none
		
		self.pathHistory = self.showPath()
		self.pathHistory.append(self.grid[self.startRow][self.startCol])
		self.sum = self.sum + self.initialValue()
		self.grid[self.startRow][self.startCol] = None
		print("Current Value: " +str(self.initialValue()))
		print("New Sum: " +str(self.sum))
		print(self)
		
	
	def copyGrid(self):                   #Creates a copy of a Grid 
		d = []
		for i in range (len(self.grid)):
			g = []
			for j in range (len (self.grid[i])):
			  g.append (self.grid[i][j])
			d.append (g)
		return d 
	

    
	
		
def display(problem):                     #Displays debugging information 
    
	starter = problem.initialValue()
	print("Initial coords: [" + str(problem.startRow) + "," + str(problem.startCol) + "]")
	print("Initial Value: " +str(starter))
	print("History: " +str(problem.pathHistory))
	print("Grid:")
	
def solve(problem):
	
	
	
	if problem.sum == targetValue: #Solution complete once sum equals the target value 
		print("Solution Found!")
		return problem.pathHistory

	elif(problem.sum > targetValue):
		print("Target exceeded:  abandoning path")
		return None
	
	else:
		
		start = problem.initialValue()
		gridCopy = problem.copyGrid()
		newSum = problem.sum
		pathCopy = problem.showPath()

		#First see if we can move right 
		
		if(problem.startCol < gridCols - 1):
			if(problem.grid[problem.startRow][problem.startCol + 1] != None):
				
				print("Moving to the right")
				print("Previous sum " +str(newSum))
				problemInstance = Problem( problem.startRow, problem.startCol + 1,gridCopy, newSum, pathCopy) #Create New Problem Instance
				problemInstance.promblemInitializer()
				pathStep = solve(problemInstance)
				if pathStep != None:
					return pathStep
		else:
			print("Can not move right")

		#If we cant move right then we will move up
		
		if(problem.startRow - 1 >= 0):              #Each of the if blocks will return a different possible step in the path
			if(problem.grid[problem.startRow - 1][problem.startCol] != None):
				
				print("Moving up")
				print("Previous sum " +str(newSum))
				problemInstance = Problem( problem.startRow - 1, problem.startCol,gridCopy, newSum, pathCopy)
				problemInstance.promblemInitializer()
				pathStep = solve(problemInstance)
				if pathStep != None:
					return pathStep
		else:
			print("Can not move up")

		#If we cant move right or up move down 
		if(problem.startRow < gridRows - 1):
			if(problem.grid[problem.startRow + 1][problem.startCol] != None):
				
				print("Moving down")
				print("Previous sum " +str(newSum))
				problemInstance = Problem( problem.startRow + 1, problem.startCol,gridCopy, newSum, pathCopy)
				problemInstance.promblemInitializer()
				pathStep = solve(problemInstance)
				if pathStep != None:
					return pathStep
		else:
			print("Can not move down")

		#If we cant move in the other three directions move left 
		if(problem.startCol- 1 >= 0):
			if(problem.grid[problem.startRow][problem.startCol - 1] != None):
				
				print("Moving to the left")
				print("Previous sum " +str(newSum))

				problemInstance = Problem( problem.startRow, problem.startCol - 1,gridCopy, newSum, pathCopy)
				problemInstance.promblemInitializer()
				pathStep = solve(problemInstance)
				if pathStep != None:
					return pathStep
		else:
			print("Can not move left")

		print("Couldn't move in any direction.  Backtracking." +str(problem.pathHistory))
		return None
		
			
	
		


def main():


	global targetValue                                   #Initialize global variables I can use in functions 
	global gridRows
	global gridCols
	
	list1 = []
	pathHistory = []
	for line in open("pathdata.txt"):                   #Read File 
		x = line.split()
		list1.append(x)
    
	
	firstRow = list1[0]                                  #Get Data from the first line
	targetValue = int(firstRow[0])
	gridRows = int(firstRow[1])
	gridCols = int(firstRow[2])
	startRow = int(firstRow[3])
	startCol = int(firstRow[4])
	endRow = int(firstRow[5])
	endCol = int(firstRow[6])
	sum = 0
	list1.pop(0)
	grid = []
	for i in range(len(list1)):                             #Create Grid of integers 
		grid2 = []
		for j in range(len(list1[i])):
			if(list1[i][j] != None):
				grid2.append((int)(list1[i][j]))
			else:
				grid2.append(None)
		grid.append(grid2)
	
	problem = Problem(startRow,startCol, grid, sum, pathHistory)           #Create first Instace of my problem 
	print("Grid")
	print(problem)
	
	problem.promblemInitializer()
	
	print("Target Value: " +str(targetValue))
	display(problem)
	print(problem)

	
	pathStep = solve(problem)                  #Run the recursive function 

	
	print("Solution is: " +str(pathStep))         #Show Solution 
	
	
	
		
	
	
main()