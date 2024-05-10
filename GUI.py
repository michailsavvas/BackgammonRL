#import game

def symbol(player):
    #returns X or O according to player being red or black
    if player == 0:
        return 'X'
    elif player == 1:
        return 'O'

def printGUI(state):
    #function that outputs the current image of the board
    #first row
    top_row = ['12', '11', '10', ' 9', ' 8', ' 7', '|', '|', ' 6', ' 5', ' 4', ' 3', ' 2', ' 1', '|', 'black_bar', 'black_out']
    #last row
    bottom_row = ['13', '14', '15', '16', '17', '18', '|', '|', '19', '20', '21', '22', '23', '24', '|', 'red_bar', 'red_out']
    print ' '.join(str(_) for _ in top_row)
    #    
    for _ in range(7): #let's do 7 + 1 + 7 rows inbetween
        intermediate_row = ['  ', '  ', '  ', '  ', '  ', '  ', '|', '|',\
                            '  ', '  ', '  ', '  ', '  ', '  ', '|', '  ', '  ']
        for point in range(1,13):
            if state[0][point] > 0:
                if point < 7:
                    intermediate_row[14-point] = ' X'
                else:
                    intermediate_row[12-point] = ' X'
                state[0][point] -= 1
            elif state[1][point] > 0:
                if point < 7:
                    intermediate_row[14-point] = ' O'
                else:
                    intermediate_row[12-point] = ' O'
                state[1][point] -= 1
        print ' '.join(str(__) for __ in intermediate_row)
    
    intermediate_row = ['  ', '  ', '  ', '  ', '  ', '  ', '|', '|',\
                            '  ', '  ', '  ', '  ', '  ', '  ', '|', '  ', '  ']
    print ' '.join(str(__) for __ in intermediate_row)
    #
    for _ in range(7):
        intermediate_row = ['  ', '  ', '  ', '  ', '  ', '  ', '|', '|',\
                            '  ', '  ', '  ', '  ', '  ', '  ', '|', '  ', '  ']
        for point in range(13,25):
            if state[0][point] > 0:
                if point < 19:
                    intermediate_row[point-13] = ' X'
                else:
                    intermediate_row[point-11] = ' X'
                state[0][point] -= 1
            elif state[1][point] > 0:
                if point < 19:
                    intermediate_row[point-13] = ' O'
                else:
                    intermediate_row[point-11] = ' O'
                state[1][point] -= 1
        print ' '.join(str(__) for __ in intermediate_row)   
    
    print ' '.join(str(_) for _ in bottom_row)
    return
    
