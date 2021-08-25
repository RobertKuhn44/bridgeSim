from deck import Deck

gameDeck = Deck()

s = str(gameDeck.cards[1].rank)
s += ' of '
s += str(gameDeck.cards[1].suit)

print(s)