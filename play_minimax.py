import game, random
from learn import *
from GUI import *
from util import *
from minimax import *
#
filename = raw_input('Please input location of weights: ')
eval_mode = input('Please input eval mode. 1 for sigmoid linear, 2 for neural: ')
#
if eval_mode == 1:
    evalFunction = sigmoidLinearEvalFunction
elif eval_mode == 2:
    evalFunction = neuralEvalFunction
#
w = Counter({})
f = open(filename, 'r')
next(f)
for line in f:
    info = line.split(': ')
    w[info[0]] = float(info[1])
f.close()
portes = game.backgammonGame()
arxi = portes.startState()
#
end = False
player = 0
current = arxi
copy = portes.copyState(current)
depth = input('Please enter # of plies: ')
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
        current = minimaxAction(portes, current, roll, player, depth, evalFunction, w)
        

    print 'Current state: ', current
    copy = portes.copyState(current)
    printGUI(copy)
    player = 1 - player
    if portes.isEnd(current):
        end = True
    
## TERMINATION SUCCESSFUL!
            