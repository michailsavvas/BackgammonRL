from game import *
from learn import *
from util import *
from GUI import *
from collections import Counter
import random

portes = backgammonGame()
eval_mode = input('Select eval mode. 0 for linear classifier, 1 for sigmoid linear and 2 for neural net: ')
step_mode = input('Select step_mode: ')
iterations = input('Select # of iterations: ')
reward = input('Select reward: ')
initial = input('Would you like random initial weights? Enter 2 if you wish to initialize weights from file. ')
if initial == 2:
    filename = raw_input('Please enter location of weights: ')
#filename = 'FINAL_iter40000_eval2_step2_norm50000_reward3_update2000.txt'
update = input('Select update rate: ')
norm_step = input('Select normalization step: ')
output = raw_input('Please enter name of output file: ')

#initialize weights
if initial == 1 and eval_mode == 1:
    initialw = Counter({})
    ran = range(1, 25)
    for point in ran:
        for player in range(2):
            for i in range(1, 5):
                if i < 4:
                    initialw['%d has at least %d pieces at point %d' % (player, i, point)] =\
                    random.uniform(-1, 1)
                else:
                    initialw['%d has at least 4 pieces at point %d' % (player, point)] =\
                    random.uniform(-1, 1)
    ran.append(0)
    for player in range(2):
        initialw['%d has these many pieces out' % player] = random.uniform(-1, 1)
    ran.append(100)
    for player in range(2):
        initialw['%d has these many pieces on bar' % player] = random.uniform(-1, 1)
elif initial == 1 and eval_mode == 2:
    w = Counter({})
    f = open('init_labels_neural.txt', 'r')
    next(f)
    for line in f:
        info = line.split(': ')
        w[info[0]] = random.uniform(-1, 1)
    f.close()
    initialw = w
elif initial == 0:
    initialw = Counter({})
else:
    w = Counter({})
    f = open(filename, 'r')
    next(f)
    for line in f:
        info = line.split(': ')
        w[info[0]] = float(info[1])
    f.close()
    initialw = w

weights = learnWeights(portes, output, initialw, iterations, eval_mode, step_mode, norm_step, reward, update)

  