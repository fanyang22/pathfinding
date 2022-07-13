def makegrid():
    width = 10
    height = 10
    grid = []
    for i in range (height):
        for j in range (width):
            grid.append((i, j))
    return grid
    #print(grid)
        

obstacles = [[9,7],[8,7],[6,7],[6,8]]
startPoint = [0,0]
deliveryPoint = [9,9]

def down(i, j):
    i += 1
    return [i, j]

def right(i, j):
    j += 1
    return [i, j]

def adj(i, j):
    i += 1
    j += 1
    return [i, j]

def up(i, j):
    i -= 1
    return [i, j]

def left(i, j):
    j -= 1
    return [i, j]

def move():
    grid = makegrid()
    nextPosition = startPoint
    i = 0
    j = 0
    path = []
    while nextPosition != deliveryPoint:
        #nextPosition  = #grid.index[location]
        if adj(nextPosition[0],nextPosition[1]) not in obstacles and (down(nextPosition[0],nextPosition[1]) not in obstacles or right(nextPosition[0],nextPosition[1]) not in obstacles) :
            nextPosition = adj(nextPosition[0],nextPosition[1])
        elif down(nextPosition[0],nextPosition[1]) not in obstacles:
            nextPosition = down(nextPosition[0],nextPosition[1])
        elif right(nextPosition[0],nextPosition[1]) not in obstacles:
            nextPosition = right(nextPosition[0],nextPosition[1])
        elif left(nextPosition[0],nextPosition[1]) not in obstacles:
            nextPosition = left(nextPosition[0],nextPosition[1])   
        elif up(nextPosition[0],nextPosition[1]) not in obstacles:
            nextPosition = up(nextPosition[0],nextPosition[1])
        path.append(nextPosition)
    print(path)
    print("Arrived at the destination!")
