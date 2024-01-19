from random import randrange


def display_board(board):
    for j in range(3):
        print(("+" + 7 * "-")*3,end="")
        print("+")
        print(("|" + " " * 7) * 3, end="")
        print("|")
        for k in range(3):
            print(("|" + " " * 3), end="")
            print(board[j][k], end="")
            print((" " * 3), end="")
        print("|")
        print(("|" + " " * 7) * 3, end="")
        print("|")
    print(("+" + 7 * "-")*3,end="")
    print("+")
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    avbl=()
    #for i in range 3:    
    avail = make_list_of_free_fields(board)
    #display_board(board)
    print("                   IT'S YOUR TURN                     ")
    choice = int(input("              FROM THE AVAILABLE BOARD NUMBERS, ENTER THE NUMBER WHERE YOU WANT TO PUT THE O:"))
    while choice not in avail:
        choice = int(input("        SORRY, THIS IS NOT AVAILABLE! SEE THE BOARD AND TRY AGAIN: "))
    #else:
     #   break
    for i in range(3):
        for j in range(3):
            if board[i][j] == choice:
                board[i][j] = 'O'
    print("           THIS IS THE UPDATED BOARD WITH YOUR CHOICE            ")
    display_board(board)
    return(board)
    
    

def make_list_of_free_fields(board):
    avbl=[]
    for i in range(3):
        for j in range(3):
            if board[i][j] != ('O','X'):
                avbl.append(board[i][j])
    return(avbl)
            
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
        

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    countof3 = 0
    result = False
    for i in range(3):
        for j in range(3):
            if (board[i][j] == sign):
                countof3 += 1
        if (countof3 == 3):
            result = True
  #          print("3 values in 1 row are the same", result)
            break
        else:
            #result = "not yet"
            countof3 = 0
            
    for i in range(3):
        # find out if the left to right diagonal has 3 consecutive signs
        countof3 = 0 
        if (board[i][i] == sign):
            countof3 += 1
    if (countof3 == 3):
        result = True
 #       print("left to right diagonal has same 3 values", result)
    else:
        countof3 = 0
        #result = "not yet"
    #find if the right to left diagonal has 3 consecutive signs
    countof3 = 0
    i = 0
    j = 2
    while (i<3):
        if (board[i][j] == sign):
            countof3 += 1
        i += 1
        j -= 1
    if (countof3 == 3):
        result = True
#        print("right to left diagonal has same 3 values", result)
    else:
        countof3=0
        #result = "not yet"
    #find out if any columns have 3 consecutive signs
    for i in range(3):
        for j in range(3):
            if (board[j][i] == sign):
                countof3 += 1
        if (countof3 == 3):
            result = True
   #         print("3 values in one column are the same", result)
            break
        else:
            countof3 = 0
            #result = "not yet"
    #print(result)
    return(result)
                        


def draw_move(board):
    # The function draws the computer's move and updates the board.
    howmanyleft=make_list_of_free_fields(board)
    r1 = 0
    while (r1 not in howmanyleft):
        r1 = randrange(1,10)
    for i in range(3):
        for j in range(3):
            if board[i][j] == r1:
                board[i][j] = 'X'
    print("                  THE COMPUTER HAS MADE A MOVE. THIS IS THE UPDATED BOARD             ")
    display_board(board)
    return(board)
    
    
    
    
board = [[0 for i in range(3)] for j in range(3)]
numb=0

for i in range(3):
    for j in range(3):
        board[i][j] = numb + 1
   #     print(i,j,board[i][j])
        numb += 1

        
#display_board(board)

board[1][1]='X'

print("                   WELCOME TO THE GAME OF TIC-TAC-TOE                ")
print("                 COMPUTER HAS ENTERED X IN POSITION 5                        ")
display_board(board)

result = False

for count in range(4):
    enter_move(board)
    result = victory_for(board, "O" )
    if result == True:
    #if (victory_for(board, "O")):
        print ("CONGRATULATIONS!! YOU HAVE WON!!")
        break
    draw_move(board)
    result = victory_for(board, "X" )
    if result == True:
    #if (victory_for(board, "X")):
        print ("THE COMPUTER HAS WON! BETTER LUCK NEXT TIME")
        break

if result != True:
    print("ITS A DRAW! WELL PLAYED!!")


