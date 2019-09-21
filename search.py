from movement import isLevelCompleted, isMoveValid, moveBox, alreadyVisited

def DFS(board, playerPos, goalsPos, boxesPos):
    root = [[playerPos[0]], [i[:] for i in boxesPos], '']
    nextNode = []
    queue = []
    queue.append(root)
    visited = []

    while(len(queue)>0):
        visited.insert((len(visited)), queue[0])
        node = queue.pop(0)
        playerCoords = [node[0]]
        boxesPos = [i[:] for i in node[1]]
        movements = node[2]

        playerCoordsUp = [playerCoords[0][0]-1,playerCoords[0][1]]
        if isMoveValid(board, goalsPos, playerCoordsUp,'D',boxesPos):
            moveBox(playerCoordsUp, 'U', boxesPos)
            movements += 'U'
            nextNode = [[playerCoordsUp], [i[:] for i in boxesPos], movements]
            if not alreadyVisited(nextNode, queue) and not alreadyVisited(nextNode, visited):
                queue.insert(0, nextNode)
            movements = movements[:len(movements) - 1]
            boxesPos = [i[:] for i in node[1]]

        playerCoordsDown = [playerCoords[0][0]+1,playerCoords[0][1]]
        if isMoveValid(board, goalsPos, playerCoordsDown,'D',boxesPos):
            moveBox(playerCoordsDown, 'D', boxesPos)
            movements += 'D'
            nextNode = [playerCoordsDown, [i[:] for i in boxesPos], movements]
            if not alreadyVisited(nextNode, queue) and not alreadyVisited(nextNode, visited):
                queue.insert(0, nextNode)
            movements = movements[:len(movements) - 1]
            boxesPos = [i[:] for i in node[1]]

        playerCoordsLeft = [playerCoords[0][0],playerCoords[0][1]-1]
        if isMoveValid(board, goalsPos, playerCoordsLeft, 'L', boxesPos):
            moveBox(playerCoordsLeft, 'L', boxesPos)
            movements += 'L'
            nextNode = [playerCoordsLeft, [i[:] for i in boxesPos], movements]
            if not alreadyVisited(nextNode, queue) and not alreadyVisited(nextNode, visited):
                queue.insert(0,nextNode)
            movements = movements[:len(movements) - 1]
            boxesPos = [i[:] for i in node[1]]

        playerCoordsRight = [playerCoords[0][0],playerCoords[0][1]+1]
        if isMoveValid(board, goalsPos, playerCoordsRight,'R', boxesPos):
            moveBox(playerCoordsRight, 'R', boxesPos)
            movements += 'R'
            nextNode = [playerCoordsRight, [i[:] for i in boxesPos], movements]           
            if not alreadyVisited(nextNode, queue) and not alreadyVisited(nextNode, visited):
                queue.insert(0,nextNode)
            movements = movements[:len(movements) - 1]
            boxesPos = [i[:] for i in node[1]]
        
        if isLevelCompleted(goalsPos, boxesPos):
            return movements
    return "No hay solución"