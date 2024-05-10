from game import *
from learn import *
from util import *
from GUI import *
from collections import Counter
import random

#read weights first
w = Counter({})
f = open('test_weights0.txt', 'r')
next(f)
for line in f:
    info = line.split(': ')
    w[info[0]] = float(info[1])
#print w WORKS!
#

state = {0: Counter({19: 14, 20: 1}), 1: Counter({})} #test for home
print sigmoidLinearEvalFunction(state, w)
print sigmoidLinearGradient(state, w)

portes = backgammonGame()
#weights = learnWeights(portes, 10000)
#weights = learnWeights
#f = open('test_weights_10000_normalized.txt', 'w')
#f.truncate()
#for item in weights:
#    f.write('%s: %f \n' % (item, weights[item]))
#f.close()
  