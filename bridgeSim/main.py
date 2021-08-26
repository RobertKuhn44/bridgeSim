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
playerPoints = playerHand.calcPoints()
print(playerPoints)

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

passgPercent = (passg/totalSims)*100
partScorePercent = (partScore/totalSims)*100
gamePercent = (game/totalSims)*100
smallSlamPercent = (smallSlam/totalSims)*100
grandSlamPercent = (grandSlam/totalSims)*100


print('Total Sims = ' + str(totalSims))
print('Pass Percent = ' + str(passgPercent))
print('Part Score Percent = ' + str(partScorePercent))
print('Game Percent = ' + str(gamePercent))
print('Small Slam Percent = ' + str(smallSlamPercent))
print('Grand Slam Percent = ' + str(grandSlamPercent))


    






