import random

#  File: Blackjack.py
#  Description: Command Line BlackJack Simulator
#  Evan Yacek
#  Date Created:  2/14/16
#  Date Last Modified: 2/18/16

 
class Card(object):
    #Define list of class attributes because list index = rank #
    suits = ("C","H","S","D")                            
    pips = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
 
    def __init__(self, pip,suit):
        self.pip=pip
        self.suit=suit
 
    def __str__(self):
	
        
        return "%s%s"%(self.pip,self.suit)
    
    
  
#Create class Deck that has a shuffle, and deal function 
class Deck(object):                               

    def __init__(self):
        self.deck = [Card(pip,suit) for suit in Card.suits for pip in Card.pips]
 
    def __str__(self):
        return "[%s]"%", ".join( (str(card) for card in self.deck))
 
    def shuffle(self):
        random.shuffle(self.deck)
 
    def deal(self):
        self.shuffle()  
        return self.deck.pop(0)

#Create a class Player, Players can hit, get blackjack, and I will keep track of the points here.
class Player (object):                                 

    def __init__ (self, cards):
        self.pcards = cards

    def hit (self, card):
        self.pcards.append(card)
    
    #Keeps the running total in the Hand
    def handTotal (self):                          
        total = 0
        for card in self.pcards:
            if card.pip > 9:
                total += 10
            elif card.pip == 1:
                total += 11
            else:
                total += card.pip

        #This is used to accomodate for when an Ace would bust the user, instead uses a 1
        for card in self.pcards:  
            if total <= 21:
                break
            elif card.pip == 1:
                total = total - 10
    
        return total

    #Function that looks at whether or not player has Blackjack
    def bj (self):  
        return len (self.pcards) == 2 and self.handTotal() == 21

  
    def __str__ (self):
    	#Prints cards and Handtotal
        return ("%s "*len(self.pcards)+"- %d points")%tuple(self.pcards+[self.handTotal()])        

#Created a dealer class that inherits from Player class
class Dealer (Player):                           


    def __init__ (self, cards):
        Player.__init__ (self, cards)
        self.dCards = True

    #Overloads hit in the Player class allowing cards <17 to be hit and shown
    def hit (self, deck):                     
        self.dCards = False
        while self.handTotal() < 17:
            self.pcards.append (deck.deal())

    #Returns one of the Dealers cards
    def __str__ (self):                          
        if self.dCards:
            return str(self.pcards[0])
        else:
            return Player.__str__(self)	
	  
class Blackjack (object):

    #Create game deck for use, shuffles, and deals
    def __init__ (self, numPlayers):
	
        self.gamedeck = Deck()                                                     
        self.gamedeck.shuffle()
        self.numPlayers = numPlayers
        self.Players = []
        self.Players.append (Player([self.gamedeck.deal(), self.gamedeck.deal()]))
        self.dealer = Dealer ([self.gamedeck.deal(), self.gamedeck.deal()])

    
  
  

    def play (self):
        
        print()
    
        #Print Players cards
        print ('Player 1 ' + str(self.Players[0])) 

        #Print dealers cards
        print ('Dealer: ' + str(self.dealer))      
        print()

    
        listP1Points = []
        for i in range (self.numPlayers):
            while True:
                entry = input ('Player 1 do you want to hit? [y / n]: ')
                if entry in ('y', 'Y'):
                    (self.Players[i]).hit (self.gamedeck.deal())
                    points = (self.Players[i]).handTotal()
                    print ('Player 1 ' + str(self.Players[i]))
                    if points >= 21:
                        print()
                        break
                else:
                    print()
                    break
        listP1Points.append ((self.Players[i]).handTotal())

        #Dealer needs to hit now if necessary
        self.dealer.hit (self.gamedeck)              
        dPoints = self.dealer.handTotal()
        print ('Dealer: ' + str(self.dealer))
        print()
    
        #Determines who wins or loses based on point totals
        if dPoints > 21:                                             
            print ('Player 1 wins!')
        elif dPoints > listP1Points[0]:
            print ('Player 1 loses!')
        elif dPoints < listP1Points[0] and listP1Points[0] <= 21:
            print ('Player 1 wins!')
        elif dPoints == listP1Points[0]:
            if self.Players[0].bj() and not self.dealer.bj():
                print ('Player 1 wins!')
            elif not self.Players[0].bj() and self.dealer.bj():
                print ('Player 1 loses!')
            else:
                print ('There is a tie!')
        else:
            print ('Player 1 loses!')
		
def main(): 
    #Create Deck
    cardDeck = Deck() 
    #Shuffle Deck
    cardDeck.shuffle()                           
    numPlayers = 1
    game = Blackjack (numPlayers) 
    print("(K=13,Q=12,J=11,A=1)")
    game.play()
	
    
    
main()
