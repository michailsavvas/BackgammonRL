import operator
#minimax agent for the game

def minimaxValue(bg, state, roll, player, depth, evalFunction, weights, reward = 3):
    #returns minimax action
    if bg.isEnd(state):
        if state[0][0] >= 15:
            return reward
        else:
            return -reward
    elif depth == 0:
        return evalFunction(state, player, weights)
    elif player == 0:
        candidates = bg.getSuccessorStates(state, roll, player)
        expected = []
        for cand in candidates:
            total = 0
            for die1 in range(1, 7):
                for die2 in range(die1, 7):
                    if die1 == die2:
                        dice = [die1, die1, die1, die1]
                    else:
                        dice = [die1, die2]
                    temp = minimaxValue(bg, cand, dice, 1 - player, depth - 1,\
                                        evalFunction, weights, reward)
                    total += temp
            expected.append(total)
                    
        return max( expected)
        #return max(expected.iteritems(), key = operator.itemgetter(1))[0]
    elif player == 1: #this is exactly the same piece of code
        candidates = bg.getSuccessorStates(state, roll, player)
        expected = []
        for cand in candidates:
            total = 0
            for die1 in range(1, 7):
                for die2 in range(die1, 7):
                    if die1 == die2:
                        dice = [die1, die1, die1, die1]
                    else:
                        dice = [die1, die2]
                    temp = minimaxValue(bg, cand, dice, 1 - player, depth - 1,\
                                        evalFunction, weights, reward)
                    
                    total += temp
            expected.append(total)
        return min(expected)

def minimaxAction(bg, state, roll, player, depth, evalFunction, weights, reward = 3):    
    #returns minimaxAction
    candidates = bg.getSuccessorStates(state, roll, player)
    values = [0 for cand in candidates]
    for index, cand in enumerate(candidates):
        values[index] = 0
        for die1 in range(1, 7):
                for die2 in range(die1, 7):
                    if die1 == die2:
                        dice = [die1, die1, die1, die1]
                    else:
                        dice = [die1, die2]
                values[index] += minimaxValue(bg, cand, dice, 1 - player, depth - 1,\
                                             evalFunction, weights, reward)
                
        
    if player == 0:
        good = values.index(max(values))
        return candidates[good]
    else:
        good = values.index(min(values))
        return candidates[good]

  
    
                    
        
       
    
    