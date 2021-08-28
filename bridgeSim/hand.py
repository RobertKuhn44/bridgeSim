#from card import Card

class Hand:
    def __init__(self, cards):
        self.cards = cards
        self.points = 0
        self.clubs = 0
        self.spades = 0
        self.hearts = 0
        self.diamonds = 0

    def calcPoints(self):
        for idx in range(0, len(self.cards)):
            #each card has a value.  Add it to the hands point value
            self.points += self.cards[idx].value
            
            #calculate number of each suit in hand for distribution score
            if self.cards[idx].suit == 'C':
                self.clubs += 1
            elif self.cards[idx].suit == 'H':
                self.hearts += 1    
            elif self.cards[idx].suit == 'D':
                self.diamonds += 1
            elif self.cards[idx].suit == 'S':
                self.spades += 1
            else:
                print('ERROR: Card was not assigned a suit.')
        
        #calculate number of heart points for distribution score
        if self.hearts == 0:
            self.points += 5
        elif self.hearts == 1:
            self.points += 2
        elif self.hearts == 2:
            self.points += 1

        #calculate number of club points for distribution
        if self.clubs == 0:
            self.points += 5
        elif self.clubs == 1:
            self.points += 2
        elif self.clubs == 2:
            self.points += 1

        #calculate number of spade points for distribution
        if self.spades == 0:
            self.points += 5
        elif self.spades == 1:
            self.points += 2
        elif self.spades == 2:
            self.points += 1

        #calculate number of diamond points for distribution
        if self.diamonds == 0:
            self.points += 5
        elif self.diamonds == 1:
            self.points += 2
        elif self.diamonds == 2:
            self.points += 1
        
        return self.points
    
    #uhh yeah this prints the cards out to terminal
    def printHand(self):
        cardsString = str(self.cards[0].acro)
        for idx in range(1, len(self.cards)):
                cardsString += ', ' + str(self.cards[idx].acro)
        print(cardsString)