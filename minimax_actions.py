from game import *
from GUI import *
from minimax import *
from learn import *
from util import *

filename = raw_input('Please input location of weights: ')
eval_mode = input('Please input eval mode. 1 for sigmoid linear, 2 for neural: ')
player = input('Please select player. 0 for black, 1 for red: ')

if eval_mode == 1:
    evalFunction = sigmoidLinearEvalFunction
elif eval_mode == 2:
    evalFunction = neuralEvalFunction

w = Counter({})
f = open(filename, 'r')
next(f)
for line in f:
    info = line.split(': ')
    w[info[0]] = float(info[1])
f.close()
portes = backgammonGame()
start = portes.startState()
test_rolls = [ [5, 4], [1, 6], [2, 5], [3, 6], [4, 6], [1, 3], [1, 2] ]
print 'Weights: ', filename
for roll in test_rolls:
    print 'Roll: ', roll
    for depth in range(1, 3):
        print depth, minimaxAction(portes, start, roll, player, depth, evalFunction, w)