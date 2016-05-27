#  File: ExpressionTree.py
#  Description: Computes the value of expression and expresses it in postfix and prefix form 
#  Student's Name: Evan Yacek
#  Student's UT EID: ety78
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created:  4/27/16
#  Date Last Modified: 4/29/16

expressionList = ['+', '-', '*', '/']             


class Stack:                                      #implementation of stack data type
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
     def __str__(self):                                         #Prints the Stack
         return " ".join( [ str(tag) for tag in self.items ] )




class Node(object):                  #Create Node Class that has left and right child 

	def __init__ (self, data):         
		self.data = data
		self.leftChild = None
		self.rightChild = None



class BinaryTree(object):

	def __init__ (self):
		self.root = Node(None)    

	#Must call create tree before evaluate or else error 
	def createTree (self, expression):
		charList = expression.split()
		pNodes = Stack()	# Creates a stack of the parent nodes 
		cur = self.root
    
    # If the token is not a parenthesis or space it should become a node 
		for token in charList:
		  # Ignore ( and move down expression tree 
			if token == '(':
				pNodes.push(cur)
				cur.leftChild = Node(None)
				cur = cur.leftChild
			
		  
			elif token in expressionList:
				cur.data = token
				pNodes.push(cur)
				cur.rightChild = Node(None)
				cur = cur.rightChild
        
			elif token.isdigit() or '.' in token:
				cur.data = token
				cur = pNodes.pop()
        
			elif token == ')':
				if not pNodes.isEmpty():
					cur = pNodes.pop()
				else:
					break                  #Breaks if list is empty 

   
	def evaluate (self, curNode):  # Evaluate the equations using recursive evaluate function
		
            
		if curNode.data not in expressionList:
			return float(curNode.data)
			#Calculates using correct operator 
		else:
			if curNode.data == '+':
				return self.evaluate(curNode.leftChild) + self.evaluate(curNode.rightChild)
			elif curNode.data == '-':
				return self.evaluate(curNode.leftChild) - self.evaluate(curNode.rightChild)
			elif curNode.data == '*':
				return self.evaluate(curNode.leftChild) * self.evaluate(curNode.rightChild)
			elif curNode.data == '/':
				return self.evaluate(curNode.leftChild) / self.evaluate(curNode.rightChild)
			
  
  

	def preOrder (self, curNode):        #PreOrder Traversal 
		if (curNode != None):
		  print(curNode.data, end = ' ')
		  self.preOrder (curNode.leftChild)
		  self.preOrder (curNode.rightChild)

  
	def postOrder (self, curNode):          #Post order Traversal
		if (curNode != None):
		  self.postOrder (curNode.leftChild)
		  self.postOrder (curNode.rightChild)
		  print(curNode.data, end = ' ')
    


	
def main():
	expression = ''
	with open("expression.txt") as f:  
		for line in f:                      #Will iterate through each line in file
			expression = line 
			expressTree = BinaryTree()
			expressTree.createTree(expression)
			print()
			# Prints the  solution
			print(expression, '=', expressTree.evaluate(expressTree.root))
			# Outputs postfix and prefix expressions 
			print("Prefix expression:", end = ' ') 
			expressTree.preOrder(expressTree.root)
			print()
			print("Postfix expression:", end = ' ')
			expressTree.postOrder(expressTree.root)
			print()
      



main()