#import the game and minimax
from Game import *
from Game.minimax import *
from Robot373 import *
wheel=Motors("a")
tracks=Motors("b")


#Create the board
def initial_state():
    state = Board(5,5)
    return state


#define what a valid move is
def valid_moves(board,player):

    empty=[]
    for i in range(5):
        if board[i]==0:
            empty.append(i)

    return empty
    

#checks to see if there are 4 in a row
def check_four_in_a_row(row):

    if row[0]==1 and row[1]==1 and row[2]==1 and row[3]==1:
        return 1
    #elif row[1]==1 and row[2]==1 and row[3]==1 and row[4]==1:
     #   return 1
    elif row[0]==2 and row[1]==2 and row[2]==2 and row[3]==2:
        return 2
    #elif row[1]==2 and row[2]==2 and row[3]==2 and row[4]==2:
     #   return 2
    else:
        return 0
    
#defines what a win is 

def win_status(board,player):
    # in Connect4, after a move, that player can either win or stalemate
    # they can't lose after their own move
    
    if check_four_in_a_row( [board[0],board[1],board[2], board[3] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[1],board[2],board[3], board[4] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[5],board[6],board[7], board[8] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[6],board[7],board[8], board[9] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[10],board[11],board[12], board[13] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[11],board[12],board[13], board[14] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[15],board[16],board[17], board[18] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[16],board[17],board[18], board[19] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[0],board[5],board[10], board[15] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[1],board[6],board[11], board[16] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[2],board[7],board[12], board[17] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[3],board[8],board[13], board[18] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[4],board[9],board[14], board[19] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[3],board[7],board[11], board[15] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[4],board[8],board[12], board[16] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[0],board[6],board[12], board[18] ])==player:
        return 'win'
    
    if check_four_in_a_row( [board[1],board[7],board[13], board[19] ])==player:
        return 'win'
    #################################################
    if check_four_in_a_row( [board[5],board[10],board[15], board[20] ])==player:
        return 'win'
    if check_four_in_a_row( [board[6],board[11],board[16], board[21] ])==player:
        return 'win'
    if check_four_in_a_row( [board[7],board[12],board[17], board[22] ])==player:
        return 'win'
    if check_four_in_a_row( [board[8],board[13],board[18], board[23] ])==player:
        return 'win'
    if check_four_in_a_row( [board[9],board[14],board[19], board[24] ])==player:
        return 'win'
    if check_four_in_a_row( [board[20],board[21],board[22], board[23] ])==player:
        return 'win'
    if check_four_in_a_row( [board[21],board[22],board[23], board[24] ])==player:
        return 'win'
    if check_four_in_a_row( [board[20],board[16],board[12], board[8] ])==player:
        return 'win'
    if check_four_in_a_row( [board[21],board[17],board[13], board[19] ])==player:
        return 'win'
    if check_four_in_a_row( [board[6],board[11],board[17], board[23] ])==player:
        return 'win'
    if check_four_in_a_row( [board[6],board[12],board[18], board[24] ])==player:
        return 'win'
    
         # stalemate
    tie=True
    for i in range(5):
        if board[i]==0:
            tie=False

    if tie:
        return 'stalemate'



    return None

#updates the state
#NEED HELP
def update_state(state,player,move):
    new_state=state
    if state[4,move] ==0:
        new_state[4,move] = player
        trackmove(state)

    elif state[3,move] ==0:
        new_state[3,move] = player
        trackmove(state)

    elif state[2,move] ==0:
        new_state[2,move] = player
        trackmove(state)

    elif state[1,move] ==0:
        new_state[1,move] = player
        trackmove(state)

    elif state[0,move] ==0:
        new_state[0,move] = player
        return new_state
        trackmove(state)

    else:
        print("Ya cahnt get thaye fram heaya")
        
    return state

def trackmove(state):
    if state == 0:
            tracks.power=-25
            Wait(5)
            tracks.power=0
    if state == 1:
            tracks.power=-25
            Wait(5)
            tracks.power=0

    if state == 2:
            tracks.power=-25
            Wait(5)
            tracks.power=0

    if state == 3:
            tracks.power=-25
            Wait(5)
            tracks.power=0

    if state == 4:
            tracks.power=-25
            Wait(5)
            tracks.power=0



#defines how to print the board
def print_row(row):

    line=''
    if row[0]==0:
        line=line+'   '
    elif row[0]==1:
        line=line+' X '
    else:
        line=line+' O '

    line=line+'|'

    if row[1]==0:
        line=line+'   '
    elif row[1]==1:
        line=line+' X '
    else:
        line=line+' O '

    line=line+'|'

    if row[2]==0:
        line=line+'   '
    elif row[2]==1:
        line=line+' X '
    else:
        line=line+' O '

    line=line+'|'
    
    if row[3]==0:
        line=line+'   '
    elif row[3]==1:
        line=line+' X '
    else:
        line=line+' O '
    
    line=line+'|'
    
    if row[4]==0:
        line=line+'   '
    elif row[4]==1:
        line=line+' X '
    else:
        line=line+' O '
        

    
    print (line)


#actually prints the board
def show_state(board):

    print_row( [ board[0],board[1],board[2], board[3], board[4] ])
    print ("---+---+---+---+---")
    print_row( [ board[5],board[6],board[7], board[8], board[9] ])
    print ("---+---+---+---+---")
    print_row( [ board[10],board[11],board[12], board[13], board[14] ])
    print ("---+---+---+---+---")
    print_row( [ board[15],board[16],board[17], board[18], board[19] ])
    print ("---+---+---+---+---")
    print_row( [ board[20],board[21],board[22], board[23], board[24] ])
    
    print

#gets a random move
def random_move(state,player):

    moves=valid_moves(state,player)
    return random.choice(moves)

#gets a human move
def human_move(state,player):
    print ("Player ", player)
    valid_move=False
    while not valid_move:
        move=int(input('What is your move? '))
        print ("Choices:")
        print ("""
         0 | 1 | 2 | 3 | 4
        ---+---+---+---+---
         0 | 1 | 2 | 3 | 4
        ---+---+---+---+---
         0 | 1 | 2 | 3 | 4
        ---+---+---+---+---
         0 | 1 | 2 | 3 | 4
        ---+---+---+---+---
         0 | 1 | 2 | 3 | 4
        """)
        if move in valid_moves(state,player):
            valid_move=True
        else:
            print ("Illegal move.")

    return move


#gets player 2 move
def other_human_move(state,player):
    print ("Player ", player)
    valid_move=False
    while not valid_move:
        move=int(input('What is your move? '))

        if move in valid_moves(state,player):
            valid_move=True
        else:
            print ("Illegal move.")

    return move


#assignns agents to the move
human_agent=Agent(human_move)
random_agent=Agent(random_move)
other_human_agent=Agent(other_human_move)





#impletmeents the minimax agent function 
def minimax_move(state,player):
    values,moves=minimax_values(state,player, maxdepth=2)
    move = top_choice(moves,values)
    if move == 0:
        print("the move is zero")
        drive(move)
    if move == 1:
        print("the move is one")
        drive(move)
    if move ==2:
        print("the move is two")
        drive(move)
    if move == 3:
        print("the move is three")
        drive(move)
    if move == 4:
        print("the move is four")
        drive(move)
    print("Minimax moves", move)
    return move
    #return top_choice(moves,values)
minimax_agent=Agent(minimax_move)



def drive(move):
    if move==0:
        wheel.power=-10
        Wait(2.4)
        wheel.power=0
    if move==1:
        wheel.power=-10
        Wait(2.4)
        wheel.power=0
    if move==2:
        wheel.power=-10
        Wait(2.4)
        wheel.power=0
    if move==3:
        wheel.power=-10
        Wait(2.4)
        wheel.power=0
    if move==4:
        wheel.power=-10
        Wait(2.4)
        wheel.power=0
#runs the game
g=Game()
wins=g.run(human_agent, minimax_agent)

g.report()


