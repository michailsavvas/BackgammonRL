from util import *
from game import *
from GUI import *
from collections import Counter
import random
import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def dumbFeatureVector(state, player): 
    #
    feature = Counter({})
    ran = range(0, 25)
    ran.append(100)
    for point in ran:
        for plr in range(2):
            if state[plr][point] > 0:
                no = float(state[plr][point])
                stop = min(5, state[plr][point] + 1)
                for i in range(1, stop):
                    if i < 4:
                        feature['%d has at least %d pieces at point %d' % (plr, i, point)] = 1
                    else:
                        feature['%d has at least 4 pieces at point %d' % (plr, point)] = (no - 3) / 2
                        
    return feature

def betterFeatureVector(state, player):
    #
    feature = Counter({})
    ran = range(1, 25)
    for point in ran:
        for plr in range(2):
            if state[plr][point] > 0:
                no = float(state[plr][point])
                stop = min(5, state[plr][point] + 1)
                for i in range(1, stop):
                    if i < 4:
                        feature['%d has at least %d pieces at point %d' % (plr, i, point)] = 1
                    else:
                        feature['%d has at least 4 pieces at point %d' % (plr, point)] = (no - 3) / 2
    ran.append(0)
    for plr in range(2):
        feature['%d has these many pieces out' % plr] = state[plr][0] / 15.0
    ran.append(100)
    for plr in range(2):
        feature['%d has these many pieces on bar' % plr] = state[plr][100] / 2.0
    return feature

def bestFeatureVector(state, player):
    #
    feature = Counter({})
    ran = range(1, 25)
    for point in ran:
        for plr in range(2):
            if state[plr][point] > 0:
                no = float(state[plr][point])
                stop = min(5, state[plr][point] + 1)
                for i in range(1, stop):
                    if i < 4:
                        feature['%d has at least %d pieces at point %d' % (plr, i, point)] = 1
                    else:
                        feature['%d has at least 4 pieces at point %d' % (plr, point)] = (no - 3) / 2
    ran.append(0)
    for plr in range(2):
        feature['%d has these many pieces out' % plr] = state[plr][0] / 15.0
    ran.append(100)
    for plr in range(2):
        feature['%d has these many pieces on bar' % plr] = state[plr][100] / 2.0
    feature['it is player %d turn' % player] = 1
    return feature

def neuralFeatureVector(state, player):
    return bestFeatureVector(state, player)

def featureVector(state, player):
    return bestFeatureVector(state, player)
    
def linearEvalFunction(state, player, w):
    #linear evaluation function given current weights w
    return sparseVectorDotProduct(w, featureVector(state, player))

def linearGradient(state, player, w):
    #
    return featureVector(state, player)

def sigmoidLinearEvalFunction(state, player, w):
    #
    dot = sparseVectorDotProduct(w, featureVector(state, player))
    return sigmoid(dot)

def sigmoidLinearGradient(state, player, w):
    #
    sigma = sigmoidLinearEvalFunction(state, player, w)
    factor = sigma * (1 - sigma)
    return incrementSparseVector(Counter({}), factor, featureVector(state, player))

def neuralEvalFunction(state, player, w): #computes evaluation function that uses neural net
    featVec = featureVector(state, player)
    alpha = Counter({})
    for feat in featVec: #layer 0 - 
        temp = w[feat] * featVec[feat]
        alpha[feat] = sigmoid(temp)
    beta = Counter({})
    for i in range(50): #layer 1 - 50 hidden nodes
        temp = w[ 'bias layer 1 %d' % i ] * 1
        for feat in featVec:
            temp += w[ feat + ' layer 1 %d' % i ] * alpha[feat]
        beta[i] = sigmoid(temp)
    delta = w[ 'layer 2 bias' ] * 1
    for i in range(50): #layer 2 - output
        delta += w[ 'layer 2 % d' % i ] * beta[i]
    delta = sigmoid( delta ) #this is the value of the evaluation function
    
    return delta

def neuralGradient(state, player, w): #computes gradient via backpropagation
    featVec = featureVector(state, player)
    alpha = Counter({})
    for feat in featVec: #layer 0 - 
        temp = w[feat] * featVec[feat]
        alpha[feat] = sigmoid(temp)
    beta = Counter({})
    for i in range(50): #layer 1 - 50 hidden nodes
        temp = w[ 'bias layer 1 %d' % i ] * 1
        for feat in featVec:
            temp += w[ feat + ' layer 1 %d' % i ] * alpha[feat]
        beta[i] = sigmoid(temp)
    delta = w[ 'layer 2 bias' ] * 1
    for i in range(50): #layer 2 - output
        delta += w[ 'layer 2 %d' % i ] * beta[i]
    delta = sigmoid( delta ) #this is the value of the evaluation function
    
    #now compute gradient
    gradient = Counter({})
    gradient[ 'layer 2 bias' ] = delta * ( 1 - delta )
    for i in range(50):
        gradient[ 'layer 2 %d' % i ] = gradient[ 'layer 2 bias' ] * beta[i]
        gradient[ 'bias layer 1 %d' % i ] = gradient[ 'layer 2 %d' % i ] *\
        ( 1 - beta[i] ) * w[ 'layer 2 %d' % i ]
        for feat in featVec:
            gradient[ feat + ' layer 1 %d' % i ] = gradient[ 'bias layer 1 %d' % i ] * alpha[feat]
    for feat in featVec:
        gradient[ feat ] = 0
        for i in range(50):
            gradient[ feat ] += gradient[ feat + ' layer 1 %d' % i ]
        gradient[ feat ] = gradient[ feat ] * ( 1 - alpha[feat] ) * w[feat]
        
    return gradient      

def learnWeights(bg, filename, initial_weights, iterations, eval_mode, step_mode, norm_step = 100, reward = 20,\
                 update = 500, eta = 0.1, gamma = 1):
    #function that learns the weights by simulating the game and running TD-Learning
    #initialize weights at 0
    w = initial_weights
    if eval_mode == 0:
        evalFunction = linearEvalFunction
        evalGradient = linearGradient
    elif eval_mode == 1:
        evalFunction = sigmoidLinearEvalFunction
        evalGradient = sigmoidLinearGradient
    elif eval_mode == 2:
        evalFunction = neuralEvalFunction
        evalGradient = neuralGradient
     
    percentage = 0 #debugging parameter
    for _ in range(iterations):
        currentState = bg.startState()
        player = random.choice( [0, 1] )
        while not bg.isEnd(currentState): #game not ended yet
            roll = bg.getRoll()
            
            succ = bg.getSuccessorStates(currentState, roll, player)
            if player == 0:
                value = max([evalFunction(state, 1 - player, w) for state in succ])
            elif player == 1:
                value = min([evalFunction(state, 1 - player, w) for state in succ])
            candidates = [state for state in succ if evalFunction(state, 1 - player, w) == value]
            
            newState = random.choice(candidates)
            
            if bg.isEnd(newState):                
                r = (0.5 - player) * reward
                percentage += float(player)
                print percentage / (_ + 1) 
            else:
                r = 0
            
            if step_mode == 0:
                epsilon = eta
            elif step_mode == 1:
                epsilon = 1.0 / (1 + _)
            elif step_mode == 2:
                epsilon = 0.1 / (1 + (_ / update))
                
            scale = epsilon * (evalFunction(currentState, player, w) - r\
                               - gamma * evalFunction(newState, 1 - player, w))
            
            w = incrementSparseVector(w, -scale, evalGradient(currentState, player, w))
            
            currentState = newState
            player = 1 - player #player change
        print 'Game %d' % (_+ 1)
          
        if (_ + 1) % norm_step == 0 and eval_mode != 2: #10 or 1000
            w = normalizeWeights(w)
        
        if (_ + 1) % norm_step == 0:
            f = open(filename, 'w')
            f.truncate()
            f.write('After %d games \n' % (_ + 1))
            for item in w:
                if w[item] != 0:
                    f.write('%s: %f \n' % (item, w[item]))
            f.close()
    return w        
        