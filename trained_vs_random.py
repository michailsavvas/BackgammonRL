import game, random
from learn import *
from GUI import *
from util import *
from minimax import *
#read weights first
w = Counter({})
filename1 = raw_input('Please input location of weights: ')
f = open(filename1, 'r')
next(f)
for line in f:
    info = line.split(': ')
    w[info[0]] = float(info[1])
f.close()
eval_mode = input('Select eval mode: ')
depth = input('Select # of plies: ')
iterations = input('Select # of iterations: ')
mode = input('Select minimax player. 0 for black, 1 for red, 2 for random: ')
if eval_mode == 0:
    evalFunction = linearEvalFunction
    evalGradient = linearGradient
elif eval_mode == 1:
    evalFunction = sigmoidLinearEvalFunction
    evalGradient = sigmoidLinearGradient
elif eval_mode == 2:
    evalFunction = neuralEvalFunction
    evalGradient = neuralGradient
count = 0
percentage = 0 #debugger
for _ in range(iterations):
    portes = game.backgammonGame()
    currentState = portes.startState()
    player = random.choice( [0, 1] )
    if mode == 2:
        mini = random.choice( [0, 1] )
    elif mode == 1:
        mini = 1
    elif mode == 0:
        mini = 0
    while not portes.isEnd(currentState): #game not ended yet
        roll = portes.getRoll()
        #copy = portes.copyState(currentState)
        #printGUI(copy)
        if player == mini:
            newState = minimaxAction(portes, currentState, roll, player, depth,\
                                     evalFunction, w, reward = 3)
        elif player != mini:
            succ = portes.getSuccessorStates(currentState, roll, player)
            newState = random.choice(succ)
            
        if portes.isEnd(newState):                
            if player == mini:
                count += 1.0
            percentage = count / ( _ + 1 )
            print _ + 1, percentage
        currentState = newState    
        player = 1 - player

        filename2 = filename1 + str(depth) + 'plies_' + str(iterations) +'iter_' + str(mode) + 'minimax.txt'
        g = open(filename2, 'w')
        g.write('Percentage of minimax wins vs random in %d iterations: %f' % (_ + 1, percentage))
        g.close()
## TERMINATION SUCCESSFUL!
            