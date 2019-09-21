def isBox(boxesPos, coords):
    for boxcoord in boxesPos:
        if boxcoord[0] == coords[0] and boxcoord[1] == coords[1]:
            return True
    return False

def isMoveValid(board, goalsPos, coords, direction, nodeBoxPos):

    if board.get(coords[0], coords[1]) == 'W':
        return False
    if direction == 'U':
        if isBox(nodeBoxPos, coords):
            if isBox(nodeBoxPos, (coords[0] - 1, coords[1])):
                return False
            if board.get(coords[0]-1, coords[1]) == 'W': 
                return False
            if (board.get(coords[0]-2, coords[1]) == 'W' and board.get(coords[0]-1, coords[1]-1)) == 'W':
                if (coords[0] - 1, coords[1]) not in goalsPos:
                    return False
            if (board.get(coords[0]-2, coords[1]) == 'W' and board.get(coords[0]-1, coords[1]+1)) == 'W':    
                if (coords[0] - 1, coords[1]) not in goalsPos:
                    return False
        return True
    
    if direction == 'D':
        if isBox(nodeBoxPos, coords):
            if isBox(nodeBoxPos, (coords[0] + 1, coords[1])):
                return False
            if board.get(coords[0]+1, coords[1]) == 'W': 
                return False
            if (board.get(coords[0]+2, coords[1]) == 'W' and board.get(coords[0]+1, coords[1]-1)) == 'W':
                if (coords[0] + 1, coords[1]) not in goalsPos:
                    return False
            if (board.get(coords[0]+2, coords[1]) == 'W' and board.get(coords[0]+1, coords[1]+1)) == 'W':
                if (coords[0] + 1, coords[1]) not in goalsPos:        
                    return False
        return True

    if direction == 'L':
        if isBox(nodeBoxPos, coords):
            if isBox(nodeBoxPos, (coords[0], coords[1]-1)):
                return False
            if board.get(coords[0], coords[1]-1) == 'W': 
                return False
            if (board.get(coords[0], coords[1]-2) == 'W' and board.get(coords[0]+1, coords[1]-1)) == 'W':
                if (coords[0], coords[1]-1) not in goalsPos:
                    return False
            if (board.get(coords[0], coords[1]-2) == 'W' and board.get(coords[0]-1, coords[1]-1)) == 'W':
                if (coords[0], coords[1]-1) not in goalsPos:                  
                    return False
        return True

    if direction == 'R':
        if isBox(nodeBoxPos, coords):
            if isBox(nodeBoxPos, (coords[0], coords[1]+1)):
                return False
            if board.get(coords[0], coords[1]+1) == 'W': 
                return False
            if (board.get(coords[0], coords[1]+2) == 'W' and board.get(coords[0]+1, coords[1]+1)) == 'W':
                if (coords[0], coords[1]+1) not in goalsPos:
                    return False
            if (board.get(coords[0], coords[1]+2) == 'W' and board.get(coords[0]-1, coords[1]+1)) == 'W':
                if (coords[0], coords[1]+1) not in goalsPos:        
                    return False
        return True
            
def moveBox(direction, coords, nodeBoxPos):
    if not isBox(nodeBoxPos, coords):
        return nodeBoxPos
    
    for box in nodeBoxPos:
        if box[0] == coords[0] and box[1] == coords[1] and direction == 'U':
            nodeBoxPos.remove(box)
            nodeBoxPos.append([coords[0]-1,coords[1]])
            return nodeBoxPos

        if box[0] == coords[0] and box[1] == coords[1] and direction == 'D':
            nodeBoxPos.remove(box)
            nodeBoxPos.append([coords[0]+1,coords[1]])
            return nodeBoxPos

        if box[0] == coords[0] and box[1] == coords[1] and direction == 'L':
            nodeBoxPos.remove(box)
            nodeBoxPos.append([coords[0],coords[1]-1])
            return nodeBoxPos

        if box[0] == coords[0] and box[1] == coords[1] and direction == 'R':
            nodeBoxPos.remove(box)
            nodeBoxPos.append([coords[0],coords[1]+1])
            return nodeBoxPos


def alreadyVisited(node, queue):
    for visitedNode in queue:
        if visitedNode[0] == node[0] and visitedNode[1] == node[1]:
            return True
    return False

def isLevelCompleted(goalsPos, boxesPos):
    for goal in goalsPos:
        if not boxesPos.__contains__(goal):
            return False
    return True