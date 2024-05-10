import game, random
from learn import *
from GUI import *
from util import *
#read weights first
w = Counter({})
f = open('test_weights_150_linear_normalized.txt', 'r')
for line in f:
    info = line.split(': ')
    w[info[0]] = float(info[1])
#print w WORKS!
#
portes = game.backgammonGame()
arxi = portes.startState()
#
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
        succ = portes.getSuccessorStates(current, roll, player)
        value = min([linearEvalFunction(state, 1 - player, w) for state in succ])
        candidates = [state for state in succ if linearEvalFunction(state, 1 - player, w) == value]
        current = random.choice(candidates)
        

    print 'Current state: ', current
    copy = portes.copyState(current)
    printGUI(copy)
    player = 1 - player
    if portes.isEnd(current):
        end = True
    
## TERMINATION SUCCESSFUL!
            