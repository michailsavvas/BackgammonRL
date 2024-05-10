from game import *
from GUI import *
####
portes = backgammonGame()
testState0 = portes.startState()
roll = [1, 4]
print portes.getSuccessorStates(testState0, roll, 0)
testState1 = {0: Counter({19: 14, 20: 1}), 1: Counter({})} #test for home
roll = [6, 5]
print portes.isAtHome(testState1, 0)
print portes.getSuccessorStates(testState1, roll, 0)
print '\n'
testState4 = {0: Counter({}), 1: Counter({6: 14, 5: 1})} #test for home
roll = [6, 5]
print portes.isAtHome(testState4, 1)
print portes.getSuccessorStates(testState4, roll, 1)
print '\n'
testState2 = {0: Counter({19: 14, 20: 1}), 1: Counter({100: 1})} #test for entry
roll = [6, 6, 6, 6]
print portes.getSuccessorStates(testState2, roll, 1)
print '\n'
testState3 = {0: Counter({19: 14, 20: 1}), 1: Counter({100: 2})} #test for entry
roll = [6, 5]
print portes.getSuccessorStates(testState3, roll, 1)
####
print 'new test got from game'
testState5 = {0: Counter({19: 4, 22: 4, 20: 3, 16: 2, 18: 2}), 1: Counter({13: 3, 21: 3, 2: 2, 8: 2, 23: 2, 1: 1, 4: 1, 6: 1})}
print portes.isAtHome(testState5, 1)
roll = [2, 4]
succ = portes.getSuccessorStates(testState5, roll, 1)
for el in succ:
    print el[1]
    if el[1][0] > 0:
        print el[1]
####
testState6 = portes.startState()
roll = [2, 2, 2, 2]
print portes.getSuccessorStates(testState6, roll, 0)
####
testState7 = portes.startState()
roll = [6, 6, 6, 6]
for state in portes.getSuccessorStates(testState6, roll, 0):
    printGUI(state)


## ALL SUCCESSFUL 29/11
