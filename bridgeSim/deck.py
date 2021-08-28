from card import Card
import random

class Deck:
        #create card array
    def __init__(self):
        self.cards = []
    

    def createDeck(self):
        self.cards = []

        for suit in "SCDH":
            for rank in "AKQJT98765432":
                value = 0
                if rank == 'A':
                    value = 4
                elif rank == 'K':
                    value = 3
                elif rank == 'Q':
                    value = 2
                elif rank == 'J':
                    value = 1
            
                acro = str(suit) + str(rank)
                nextCard = Card(suit, rank, value, acro)
                self.cards.append(nextCard)

    def shuffleDeck(self):
        random.shuffle(self.cards)
    
    def dealPlayerHand(self):
        hand = []

        for idx in range(0, 13):
            hand.append(self.cards.pop())

        return hand

    def simPartnerHand(self):
        hand = []

        for idx in range(0, 13):
            hand.append(self.cards.pop())

        #add them back so we can sim another hand
        for idx in range(0, 13):
            self.cards.append(hand[idx])

        #get ready for the next sim
        self.shuffleDeck()
        
        return hand
    
    