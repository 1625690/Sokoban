from search import DFS,BFS,IDFS

#Board of the game
board = {}
#Boxes' positions
boxesPos = []
#Player position
player = []
#Goals positions
goalsPos = {}

def read_level(lvl):

    #Goals counter
    numGoals = 0
    #Flag for box
    boxFlg = False

    gameBoard = open(lvl)
    #lines
    i = 0
    for x in gameBoard:
        #columns
        j = 0
        #If line have at least one wall 
        if "W" in x:
            #Take each character in line
            while j < len(x):
                #Not the end of the txt
                if x[j] is not "\n":
                    #Fill the board map
                    if x[j] == "X":
                        board[(i, j)] = x[j]
                        goalsPos[(i, j)] = x[j]
                        numGoals += 1
                        j += 1
                    else:
                        board[(i, j)] = x[j]
                        j += 1
                    #Next character    
                else:
                    j += 1
        #Not the end of the txt
        else:
            if x is not "\n" and boxFlg == False:
                player.append(int(x[0]))
                player.append(int(x[2]))
                boxFlg = True
            elif x is not "\n" and boxFlg == True:
                boxesPos.append([int(x[0]), int(x[2])])
        #next line
        i += 1

read_level("nivel1.txt")

print(IDFS(board,player,goalsPos,boxesPos))