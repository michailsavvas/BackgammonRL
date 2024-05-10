import random, collections
from collections import Counter
from sets import Set

#define general search problem class here

####

#class defining a standard backgammon game, incorporate other variants later
class backgammonGame:
    #start state
    #0 = black, 1 = red, 100 = bar, 0: out for both red and black
    def startState(self):
        #the format of each state is a dictionary of two counters, which record the position of the 
        #checkers of the two players
        black = Counter( { 1: 2, 12: 5, 17: 3, 19: 5} )
        red = Counter( { 6: 5, 8: 3, 13: 5, 24: 2} )
        start = { 0: black, 1: red }
        return start
    
    #dice roll
    def getRoll(self):
        #return the rolls of two dice as a list
        die1 = random.choice( range(1,7) )
        die2 = random.choice( range(1,7) )
        if die1 > die2:
            return [die2, die1]
        elif die1 == die2:
            return [die1, die1, die1, die1]
        else:
            return [die1, die2]
    
    #players
    def players(self):
        return [0, 1]
    
    #points
    def points(self):
        return range(1, 25)
    
    #direction of the two players
    def direction(self, player):
        if player == 0:
            return +1
        else:
            return -1
        
    #check whether the game ended or not
    def isEnd(self, state):
        if state[0][0] >= 15 or state[1][0] >= 15:
            return True
        else:
            return False                
    
    #check for single
    def isSingle(self, state, point, player):
        return state[player][point] == 1
    
    #check function for anchor
    def isAnchor(self, state, point, player):
        return state[player][point] > 1
    
    #helper function to copy state
    def copyState(self, state):
        newState = {}
        newState[0] = Counter({})
        newState[1] = Counter({})
        for player in self.players():
            for point in state[player]:
                newState[player][point] = state[player][point]
        return newState    
    
    #function to modify state appropriately if checker is hit
    def isHit(self, state, point, player):
        newState = self.copyState(state)
        newState[player][point] -= 1
        if newState[player][point] == 0:
            del newState[player][point]
        newState[player][100] += 1
        return newState
    
    #function to check if all checkers of player are in home zone
    def isAtHome(self, state, player):
        check = True
        if state[player][100] == 0:
            for point in state[player]:
                if player == 0 and point < 19 and point != 0:
                    return False
                if player == 1 and point > 6 and point != 100:
                    return False
        return check
            
    
    #function to move player's checker from "point" to "new_point", also removes hit checkers
    #does not check legality of move
    def move(self, state, point, new_point, player):
        newState = self.copyState(state)
        newState[player][point] -= 1
        if newState[player][point] == 0:
            del newState[player][point]
        newState[player][new_point] += 1
        opponent = 1 - player
        if state[opponent][new_point] == 1 and new_point != 0 and new_point != 100:
            newState = self.isHit(newState, new_point, opponent)
        return newState         
    
    #modified count for entry from bar back to board (backwards)
    def convertRoll(self, die, player):
        if player == 0:
            return die
        else:
            return self.direction(player)*die % 25        
    
    #legal moves for player at a certain state after certain roll 
    def getSuccessorStates(self, state, roll, player):
        #for safety, treat black and red player separately
        succ = [] #pairs of successor states + number of dice left
        opponent = 1 - player
        stack = [ (state, roll) ] #intermediate stack of possible moves
        cache = [ (state, roll) ] #NEW LINE v. 1
        while stack:
            currentState, currentRoll = stack.pop()
            #print '0', currentState
            if len(currentRoll) == 0: #we have used up all the dice
                succ.append((currentState, 0))
                #succ.append((currentState, 0))
                #succ.add(currentState) #new possible state
            else:
                valid = False #have at least one valid move
                #check bar first
                if currentState[player][100] > 0:
                    enter = [self.convertRoll(die, player) for die in currentRoll]
                    #if checkers can't enter, do nothing, otherwise add elements to stack
                    for i in range(len(enter)):
                        if not self.isAnchor(currentState, enter[i], opponent): #can put checker in
                            valid = True
                            newRoll = [die for die in currentRoll]
                            del newRoll[i]
                            newState = self.move(currentState, 100, enter[i], player)
                            #print newState
                            if (newState, newRoll) not in cache:
                                cache.append( (newState, newRoll) ) #v. 1
                                stack.append( (newState, newRoll) ) #v. 1
                            #stack.append( (newState, newRoll) ) OLD LINE v. 0
                    if not valid: #no valid moves
                        succ.append((currentState, len(currentRoll)))
                else:
                    atHome = self.isAtHome(currentState, player) #check if at home
                    direction = self.direction(player) #adjust direction
                    for i in range(len(currentRoll)):
                        sign_die = direction * currentRoll[i]
                        newRoll = [die for die in currentRoll]
                        del newRoll[i]
                        for point in currentState[player]:
                            if point != 0:
                                new_point = point + sign_die
                                #print point, new_point
                                #if direction * (new_point - (new_point % 25)) > 0: #new_point out
                                if new_point > 24 or new_point < 1:
                                    if atHome: #check if this is allowed
                                        valid = True
                                        #print newRoll, point, new_point
                                        newState = self.move(currentState, point, 0, player)
                                        if (newState, newRoll) not in cache:
                                            cache.append( (newState, newRoll) ) #v. 1
                                            stack.append( (newState, newRoll) ) #v. 1
                                        #stack.append( (newState, newRoll) ) v. 0
                                else:
                                    if not self.isAnchor(currentState, new_point, opponent):
                                        valid = True
                                        newState = self.move(currentState, point, new_point, player)
                                        #print 'current', currentState
                                        #print newState
                                        if (newState, newRoll) not in cache:
                                            cache.append( (newState, newRoll) ) #v. 1
                                            stack.append( (newState, newRoll) ) #v. 1
                                        #stack.append( (newState, newRoll) ) v. 0
                        if not valid:
                            succ.append((currentState, len(currentRoll)))
        #SHOULD ENSURE USE MAX NUMBER OF DICE: DONE
        #eliminate duplicates
        succ1 = [new for i,new in enumerate(succ) if new not in succ[:i]]
        minimum = min( [new[1] for new in succ1] )
        succ2 = [new[0] for new in succ1 if new[1] == minimum]                      
        
        return succ2
                    
                    
                    
                
        
        
        