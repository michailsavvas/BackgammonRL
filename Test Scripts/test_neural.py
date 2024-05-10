from learn import *
from minimax import *
from game import *
from util import *

portes = backgammonGame()

startState = portes.startState()
w = Counter({})

#print neuralEvalFunction(startState, 0, w)
grad = neuralGradient(startState, 0, w)
print grad['layer 2 bias']
print grad['layer 2 1']
w = incrementSparseVector(w, -0.1, grad)
grad = neuralGradient(startState, 0, w)
print sigmoid(-0.025-5/16.0)
print w['layer 2 bias']
print w['layer 2 1']
print w['bias layer 1 1']
grad = neuralGradient(startState, 0, w)
w = incrementSparseVector(w, -0.1, grad)
print grad['bias layer 1 1']
print w['bias layer 1 1']
grad = neuralGradient(startState, 0, w)
w = incrementSparseVector(w, -0.1, grad)
grad = neuralGradient(startState, 0, w)
w = incrementSparseVector(w, -0.1, grad)


for item in grad:
    if item != 0:
        print item, grad[item]
        
print sigmoid(150)


