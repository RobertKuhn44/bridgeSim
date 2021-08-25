from card import Card

class Deck:
        #create card array
    cards = []

        #create Aces
    curDiamondCard = Card('Diamonds', 'Ace', int(13), 'DA')
    curHeartCard = Card('Hearts', 'Ace', int(13), 'HA')
    curClubCard = Card('Clubs', 'Ace', int(13), 'CA')
    curSpadeCard = Card('Spades', 'Ace', int(13), 'SA')
    cards.append(curClubCard)
    cards.append(curSpadeCard)
    cards.append(curDiamondCard)
    cards.append(curHeartCard)

        #create Kings
    curDiamondCard = Card('Diamonds', 'King', int(13), 'DK')
    curHeartCard = Card('Hearts', 'King', int(13), 'HK')
    curClubCard = Card('Clubs', 'King', int(13), 'CK')
    curSpadeCard = Card('Spades', 'King', int(13), 'SK')
    cards.append(curClubCard)
    cards.append(curSpadeCard)
    cards.append(curDiamondCard)
    cards.append(curHeartCard)

        #create Queens
    curDiamondCard = Card('Diamonds', 'Queen', int(13), 'DQ')
    curHeartCard = Card('Hearts', 'Queen', int(13), 'HQ')
    curClubCard = Card('Clubs', 'Queen', int(13), 'CQ')
    curSpadeCard = Card('Spades', 'Queen', int(13), 'SQ')
    cards.append(curClubCard)
    cards.append(curSpadeCard)
    cards.append(curDiamondCard)
    cards.append(curHeartCard)

        #create Jacks
    curDiamondCard = Card('Diamonds', 'Jack', int(13), 'DJ')
    curHeartCard = Card('Hearts', 'Jack', int(13), 'HJ')
    curClubCard = Card('Clubs', 'Jack', int(13), 'CJ')
    curSpadeCard = Card('Spades', 'Jack', int(13), 'SJ')
    cards.append(curClubCard)
    cards.append(curSpadeCard)
    cards.append(curDiamondCard)
    cards.append(curHeartCard)
    
    #make the cards for ranks 2-10  DONT FORGET YOU NEED TO UPDATE VALUES
    for x in range(2, 11):
        s ='s'
        d = 'd'
        h = 'h'
        c = 'c'
        s += str(x)
        d += str(x)
        h += str(x)
        c += str(x)
        curDiamondCard = Card('Diamonds', str(x), int(13), d)
        curHeartCard = Card('Hearts', str(x), int(13), h)
        curClubCard = Card('Clubs', str(x), int(13), c)
        curSpadeCard = Card('Spades', str(x), int(13), s)

        #add each suit of the current rank to cards
        cards.append(curClubCard)
        cards.append(curSpadeCard)
        cards.append(curDiamondCard)
        cards.append(curHeartCard)

    