map = {}
solution = []
boxes = 0

def search():
    read_level()
    stack = []
    moves = []
    box = []
    stack.append(list(map[0]))

    for n in range(5):
        if len(stack) == 0:
            return "Fallo"
        n = stack.pop()
        if box == solution:
            return moves


def read_level():
    file = open("nivel1.txt")
    i = 0
    global boxes
    for x in file:
        j = 0
        if "W" in x:
            while j < len(x):
                if x[j] is not "\n":
                    map[(i, j)] = x[j]
                    j += 1
                else:
                    j += 1
        elif x is not "\n":
            map[boxes] = (int(x[0]), int(x[2]))
            boxes += 1
        i += 1
    for x in map:
        if map[x] == "X":
            solution.append(list(x))


read_level()
