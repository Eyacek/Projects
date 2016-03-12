
#  File: htmlChecker.py
#  Description: Checks html file to see if tags are matching
#  Student's Name: Evan Yacek
#  Student's UT EID: ety78
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 2/28/2016
#  Date Last Modified: 2/29/2016


import re            

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
	


def main():


	
	EXCEPTIONS =["br","/br","meta","!","hr"]
	VALIDTAGS = []
	
	with open('htmlfile.txt', 'r') as myfile:
		data = myfile.read().replace('\n', '')           #Open File as Long String

	tagList = re.findall(r'<(.*?)>',data)                 #Use regex to create list of tags between < >
	print("List of HTML Tags")
	print(tagList)
	stack = Stack()                                     #Create Stack
	print()
	for tag in tagList:
		if tag[0] != "/" and tag != "br" and tag[0] != "m" and tag[0] != "!" and tag != "hr":    #Push tags to Stack
			stack.push(tag)
			if tag not in VALIDTAGS:
				print(tag, "is not recognized but accepted")
				VALIDTAGS.append(tag)
			print("Tag is", tag , ": pushed: stack is now [",stack, "]" )
		
		elif tag[0] == "/" and tag != "/br":           #Check to see if tags are matching
			newTag = tag[1:]
			if newTag == stack.peek():
				stack.pop()
				print("Tag is", tag , ": matches: stack is now [", stack ,"]")
				
				
			else:
				print(tag, "Tag does not match top of stack [", stack, "]")
				print()
				print("Tag is", tag, "but it does not match top of stack,", stack.peek())
		
		elif tag or tag[0] or tag[0]+tag[1]+tag[2] +tag[3]  in EXCEPTIONS:                        #Check to see if tags are in exceptions
			
			print(tag, "Tag does not need match", "Stack still [",stack,"]")
		
		
	print()
	
	
	if stack.isEmpty() == True:                      #Final outputs based on size of stack
		print("Processing complete. No mismatches found")
		print()
	else:
		print("Processing complete. Stack remains [", stack,"]")
		print()
	
	print("VALID TAGS")
	print(VALIDTAGS)
	print()
	print("EXCEPTIONS")
	print(EXCEPTIONS)
	
	
main()	

		