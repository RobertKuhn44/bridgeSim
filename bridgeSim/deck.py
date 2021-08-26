from card import Card
import random

class Deck:
        #create card array
    cards = []

        #create Aces
    curDiamondCard = Card('Diamonds', 'Ace', 4, 'DA')
    curHeartCard = Card('Hearts', 'Ace', 4, 'HA')
    curClubCard = Card('Clubs', 'Ace', 4, 'CA')
    curSpadeCard = Card('Spades', 'Ace', 4, 'SA')
    cards.append(curClubCard)
    cards.append(curSpadeCard)
    cards.append(curDiamondCard)
    cards.append(curHeartCard)

        #create Kings
    curDiamondCard = Card('Diamonds', 'King', 3, 'DK')
    curHeartCard = Card('Hearts', 'King', 3, 'HK')
    curClubCard = Card('Clubs', 'King', 3, 'CK')
    curSpadeCard = Card('Spades', 'King', 3, 'SK')
    cards.append(curClubCard)
    cards.append(curSpadeCard)
    cards.append(curDiamondCard)
    cards.append(curHeartCard)

        #create Queens
    curDiamondCard = Card('Diamonds', 'Queen', 2, 'DQ')
    curHeartCard = Card('Hearts', 'Queen', 2, 'HQ')
    curClubCard = Card('Clubs', 'Queen', 2, 'CQ')
    curSpadeCard = Card('Spades', 'Queen', 2, 'SQ')
    cards.append(curClubCard)
    cards.append(curSpadeCard)
    cards.append(curDiamondCard)
    cards.append(curHeartCard)

        #create Jacks
    curDiamondCard = Card('Diamonds', 'Jack', 1, 'DJ')
    curHeartCard = Card('Hearts', 'Jack', 1, 'HJ')
    curClubCard = Card('Clubs', 'Jack', 1, 'CJ')
    curSpadeCard = Card('Spades', 'Jack', 1, 'SJ')
    cards.append(curClubCard)
    cards.append(curSpadeCard)
    cards.append(curDiamondCard)
    cards.append(curHeartCard)
    
    #make the cards for ranks 2-10  DONT FORGET YOU NEED TO UPDATE VALUES
    for x in range(2, 11):
        s ='S'
        d = 'D'
        h = 'H'
        c = 'C'
        s += str(x)
        d += str(x)
        h += str(x)
        c += str(x)
        curDiamondCard = Card('Diamonds', str(x), 0, d)
        curHeartCard = Card('Hearts', str(x), 0, h)
        curClubCard = Card('Clubs', str(x), 0, c)
        curSpadeCard = Card('Spades', str(x), 0, s)

        #add each suit of the current rank to cards
        cards.append(curClubCard)
        cards.append(curSpadeCard)
        cards.append(curDiamondCard)
        cards.append(curHeartCard)

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
    
    