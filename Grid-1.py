#  File: Grid.py

#  Description: finds the max product of four adjacent numbers(Horizontal,Vertical,Diagonals) in a grid

#  Student Name: Evan Yacek

#  Student UT EID: ety78

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created:10/27/2015

#  Date Last Modified: 10/28/2015

def main():
  
  in_file = open ("./grid.txt", "r") #Open file to read

  
  dim = in_file.readline()  #Read Dimension
  dim = dim.strip()
  dim = int (dim)

  
  grid = []                    # create a 2-D list
   
  for i in range (dim):       # read data line by line
    line = in_file.readline()
    line = line.strip()

    
    nums = line.split()      # split the line

    
    for j in range (dim):      # convert into integers
      nums[j] = int (nums[j])

    
    grid.append (nums)            # append nums to the 2-D list
	
  
 
  maxProduct = 0                 #Create intial Variables
  rows = len(grid)                  
  cols = len(grid[0])
  step = 4                       #We want products of 4 adjacent numbers
  


  for i in range(rows):        #For loop through the number of rows
  
    for j in range(cols - step + 1):       #For loop for each iteration calculation Horizontal and Vertical Products
	
      horizontalProduct = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
      vericalProduct = grid[j][i]* grid[j+1][i] * grid[j+2][i] * grid[j+3][i]
	  
      if i <= rows - 4:                      #If Check to calculate diagonal products
	  
        diagonalProduct1 = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
        diagonalProduct2 = grid[i][j+3] * grid[i+1][j+2] * grid[i+2][j+1] * grid[i+3][j]
		
      maxProduct = max(horizontalProduct, vericalProduct, diagonalProduct1,diagonalProduct2,maxProduct) #Create max product
	  
  print("The greatest product is {0:0}.".format(maxProduct)) #Print and Format
main()

