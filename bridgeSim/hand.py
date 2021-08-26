#from card import Card

class Hand:
    def __init__(self, cards, points, clubs, spades, hearts, diamonds):
        self.cards = cards
        self.points = points
        self.clubs = clubs
        self.spades = spades
        self.hearts = hearts
        self.diamonds = diamonds

    def calcPoints(self):
        for idx in range(0, len(self.cards)):
            self.points += self.cards[idx].value
            
            if self.cards[idx].suit == 'Clubs':
                self.clubs += 1

            if self.cards[idx].suit == 'Hearts':
                self.hearts += 1    

            if self.cards[idx].suit == 'Diamonds':
                self.diamonds += 1

            if self.cards[idx].suit == 'Spades':
                self.spades += 1
        
        if self.hearts == 0:
            self.points += 5
        elif self.hearts == 1:
            self.points += 2
        elif self.hearts == 2:
            self.points += 1

        if self.clubs == 0:
            self.points += 5
        elif self.clubs == 1:
            self.points += 2
        elif self.clubs == 2:
            self.points += 1

        if self.spades == 0:
            self.points += 5
        elif self.spades == 1:
            self.points += 2
        elif self.spades == 2:
            self.points += 1

        if self.diamonds == 0:
            self.points += 5
        elif self.diamonds == 1:
            self.points += 2
        elif self.diamonds == 2:
            self.points += 1
        
        return self.points