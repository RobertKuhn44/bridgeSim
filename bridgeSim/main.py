from deck import Deck
from hand import Hand

keepRunning = True

def sim():
    #initialize sim variables
    totalSims = 100000
    passg = 0
    partScore = 0
    game = 0
    smallSlam = 0
    grandSlam = 0
    curScore = 0

    #creates deck obj
    gameDeck = Deck()

    #creates a deck of cards
    gameDeck.createDeck()
    #shuffle deck
    gameDeck.shuffleDeck()

    #deal the players hand
    playerHand = Hand(gameDeck.dealPlayerHand())
    print('Players Hand')
    #print the players hand
    playerHand.printHand()
    #calc the player points
    playerPoints = playerHand.calcPoints()
    print('Player Hand Points: ' + str(playerPoints))


    #report we are running sim
    print('Running Simmulation...')
    #run the partner hand simulation totalSims amount of times
    for idx in range(0, totalSims):
        #reset the score for each new hand
        curScore = 0

        #deal the partners hand
        partnerHand = Hand(gameDeck.simPartnerHand())
        #calc the partner points
        partnerPoints = partnerHand.calcPoints()

        #add the two scores up
        curScore += playerPoints
        curScore += partnerPoints

        #check curScore to see what type of game you simmed
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
            #if we are here im not sure how it happened
            print('WHOOPS')
    
    #calculate percentages
    passgPercent = (passg/totalSims)*100
    partScorePercent = (partScore/totalSims)*100
    gamePercent = (game/totalSims)*100
    smallSlamPercent = (smallSlam/totalSims)*100
    grandSlamPercent = (grandSlam/totalSims)*100
    #make sure we always run totalSims == 1000
    totalSimsSimmed = passg + partScore + game + smallSlam + grandSlam
    print('Total Sims = ' + str(totalSimsSimmed))
    #report percentages
    print('Pass Percent = ' + str(round(passgPercent, 2))+ '%')
    print('Part Score Percent = ' + str(round(partScorePercent, 2))+ '%')
    print('Game Percent = ' + str(round(gamePercent, 2))+ '%')
    print('Small Slam Percent = ' + str(round(smallSlamPercent, 2))+ '%')
    print('Grand Slam Percent = ' + str(round(grandSlamPercent, 2))+ '%')

sim()
while keepRunning:
    val = input('Run again? [Y|N]:')
    if val == 'N':
        keepRunning = False
    elif val == 'n':
        keepRunning = False
    elif val == 'Y':
        sim()
    elif val == 'y':
        sim()
    else:
        print('Please enter Y or N.')
