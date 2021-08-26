from deck import Deck
from hand import Hand

totalSims = 1000
passg = 0
partScore = 0
game = 0
smallSlam = 0
grandSlam = 0
curScore = 0

gameDeck = Deck()

gameDeck.shuffleDeck()

playerHand = Hand(gameDeck.dealPlayerHand(), 0, 0, 0, 0, 0)
print('Players Hand')
playerHand.printHand()
playerPoints = playerHand.calcPoints()
print('Player Hand Points: ' + str(playerPoints))

for idx in range(0, totalSims):
    curScore = 0

    partnerHand = Hand(gameDeck.simPartnerHand(), 0, 0, 0, 0, 0)
    partnerPoints = partnerHand.calcPoints()
    curScore += playerPoints
    curScore += partnerPoints

    if curScore < 20:
        passg += 1
    elif curScore >= 20 and curScore <= 25:
        partScore += 1
    elif curScore >= 26 and curScore <= 31:
        game += 1
    elif curScore >= 32 and curScore <= 35:
        smallSlam += 1
    elif curScore > 35:
        grandSlam += 1
    else:
        print('WHOOPS')

passgPercent = (passg/totalSims)*100
partScorePercent = (partScore/totalSims)*100
gamePercent = (game/totalSims)*100
smallSlamPercent = (smallSlam/totalSims)*100
grandSlamPercent = (grandSlam/totalSims)*100

print('Passes: ' + str(passg))
print('Part Scores: ' + str(partScore))
print('Games: ' + str(game))
print('Small Slams: ' + str(smallSlam))
print('Grand Slams: ' + str(grandSlam))

print('Total Sims = ' + str(totalSims))
print('Pass Percent = ' + str(round(passgPercent, 2))+ '%')
print('Part Score Percent = ' + str(round(partScorePercent, 2))+ '%')
print('Game Percent = ' + str(round(gamePercent, 2))+ '%')
print('Small Slam Percent = ' + str(round(smallSlamPercent, 2))+ '%')
print('Grand Slam Percent = ' + str(round(grandSlamPercent, 2))+ '%')


    






