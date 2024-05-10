import game, random
from GUI import *
#
portes = game.backgammonGame()
arxi = portes.startState()
#print 'start state:'
#print arxi
#test = portes.getRoll()
#print 'roll:'
#print test
#for die1 in range(1,7):
#    for die2 in range(die1,7):
#        if die1 == die2:
#            roll = [die1]*4
#        else:
#            roll = [die1, die2]
#        possib = portes.getSuccessorStates(arxi, roll, 0)
#        print roll
#print possib
end = False
player = 0
current = arxi
copy = portes.copyState(current)
print 'Current state: ', arxi
printGUI(copy)
while not end:
    
    roll = portes.getRoll()
    
    print 'Roll: ', roll
    if player == 0:
        # add end option
        for die in roll:
            move = input('How do you want to play die %d ? ' % die)
            point, new_point = move
            current = portes.move(current, point, new_point, player)
    else:
        current = random.choice(portes.getSuccessorStates(current, roll, player))
    print 'Current state: ', current
    copy = portes.copyState(current)
    printGUI(copy)
    player = 1 - player
    if portes.isEnd(current):
        end = True
    
## TERMINATION SUCCESSFUL!
            