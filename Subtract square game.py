import math 
totalCoins = 50
print('Total Coins : 50')
def playerTurn(playerNum):
    global totalCoins
    print('player '+str(playerNum))
    player = int(input())
    while player > totalCoins or player < 1 or math.sqrt(player).is_integer()==False:
        print('player '+str(playerNum)+' : Play Again')
        player = int(input())
    totalCoins -= player
    print('Remaining coins : '+str(totalCoins))
def round():
    global totalCoins
    playerTurn(1)
    if totalCoins == 0:
        print('player 1 won')
    else:
        playerTurn(2)
        if totalCoins == 0:
            print('player 2 won')
        if totalCoins > 0:
            round()
round()
