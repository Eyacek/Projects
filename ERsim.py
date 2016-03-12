#  File: ERsim.py
#  Description: Create seperate queues based on seriousness of condition, simulation for ER wating room
#  Student's Name: Evan Yacek
#  Student's UT EID: ety78
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 3/6/2016
#  Date Last Modified: 3/8/2016

class Queue:                        #Create class for Queue data type
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    def __str__(self):
	    return " ".join( [ str(name) for name in self.items ] )
    
		
def main():

	Critical = Queue()                   #Create three seperate queues for each condition
	Serious = Queue()
	Fair = Queue()
	
	with open("ERsim.txt") as f:         #Open file containing commnands
		for line in f:
		
			line = line.split()          #Split each line into its own list
			
			if line[0] == "add" and line[-1] == "Critical":                #Adds patient to critical queue
				Critical.enqueue(line[1])
				print("add patient", line[1],"to Cricitcal Queue" )
				print("Critical: [",Critical,"]")
				print("Serious: [",Serious,"]")
				print("Fair: [",Fair,"]")
				
			elif line[0] == "add" and line[-1] == "Serious":               #Adds patient to serious queue
				Serious.enqueue(line[1])
				print("add patient", line[1],"to Serious Queue" )
				print("Critical: [",Critical,"]")
				print("Serious: [",Serious,"]")
				print("Fair: [",Fair,"]")
				
				
			elif line[0] == "add" and line[-1] == "Fair":                  #Adds patients to fair queue
				Fair.enqueue(line[1])
				print("add patient", line[1],"to Fair Queue" )
				print("Critical: [",Critical,"]")
				print("Serious: [",Serious,"]")
				print("Fair: [",Fair,"]")
				
			elif line[0] == "treat" and line[-1] == "next":              #Treats each next patient starting with Critical
				if Critical.isEmpty() != True:        
					Critical.dequeue()
					print("Treating", line[1], "from Critical queue")
					print("Critical: [",Critical,"]")
					print("Serious: [",Serious,"]")
					print("Fair: [",Fair,"]")
					
				elif Critical.isEmpty() == True and Serious.isEmpty() == False:           #If critical queue is empty treat the serious queue
					Serious.dequeue()
					print("Treating", line[1], "from Serious queue")
					print("Critical: [",Critical,"]")
					print("Serious: [",Serious,"]")
					print("Fair: [",Fair,"]")
				elif Fair.isEmpty() != True and Serious.isEmpty() == True:               #If serious is empty treat the fair qeue
					Fair.dequeue()
					print("Treating", line[1], "from Fair queue")
					print("Critical: [",Critical,"]")
					print("Serious: [",Serious,"]")
					print("Fair: [",Fair,"]")
				else:
					print("All queues are empty")
				
			elif line[0] == "treat" and line[-1] == "Critical":                     #Treats critical patients
				Critical.dequeue()
				print("Treating", line[1], "for Cricitcal condition")
				print("Critical: [",Critical,"]")
				print("Serious: [",Serious,"]")
				print("Fair: [",Fair,"]")
			
			elif line[0] == "treat" and line[-1] == "Serious":                     #Treats serious patients
				Serious.dequeue()
				print("Treating", line[1], "for Serious condition")
				print("Critical: [",Critical,"]")
				print("Serious: [",Serious,"]")
				print("Fair: [",Fair,"]")
				
			elif line[0] == "treat" and line[-1] == "Fair":                       #Treats fair patients
				Fair.dequeue()
				print("Treating", line[1], "for Fair condition")
				print("Critical: [",Critical,"]")
				print("Serious: [",Serious,"]")
				print("Fair: [",Fair,"]")
				
			elif line[0] == "treat" and line[-1] == "all":                    #Treats all patients begining with critical,serious, then fair
				while Critical.isEmpty() == False:
					Critical.dequeue()
					print("Treating", line[1], "from Critical queue")
					print("Critical: [",Critical,"]")
					print("Serious: [",Serious,"]")
					print("Fair: [",Fair,"]")
				while Serious.isEmpty() == False:
					Serious.dequeue()
					print("Treating", line[1], "from Serious queue")
					print("Critical: [",Critical,"]")
					print("Serious: [",Serious,"]")
					print("Fair: [",Fair,"]")
				while Fair.isEmpty() == False:
					Fair.dequeue()
					print("Treating", line[1], "from Fair queue")
					print("Critical: [",Critical,"]")
					print("Serious: [",Serious,"]")
					print("Fair: [",Fair,"]")
					
				print("All queues are empty")
			
			elif line[0] == "exit":
				print("exit")
			
			
				
			
			
main()