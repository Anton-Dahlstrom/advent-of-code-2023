def addRight(arrays, length):
    for array in arrays:
        array += ["."]*length
    return arrays

def addLeft(arrays, length):
    for i in range(len(arrays)):
        arrays[0] = ["."]*length + arrays[0]
    return arrays

def addUp(arrays, length):
    arrayLen = len(arrays[0])
    for i in range(length):
        arrays.insert(0, ["."]*arrayLen)
    return arrays

def addDown(arrays, length):
    arrayLen = len(arrays[0])
    for i in range(length):
        arrays.append(["."]*arrayLen)
    return arrays

with open("day18/day18input.txt", "r") as file:
    lines = file.readlines()
    directions = []
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(" ")
        directions.append([lines[i][0], lines[i][1]])
    position = [0,0]
    grid = [["#"]]
    y = position[0]
    x = position[1]
    for direction in directions:
        dir = direction[0]
        meter = int(direction[1])
        
        if dir == "R":
            if x + meter > len(grid[0]):
                difference = (x + 1 + meter) - len(grid[0])
                grid = addRight(grid, difference)
            for i in range(meter):
                x += 1
                grid[y][x] = "#"
            
        if dir == "L":
            if x - meter < 0:
                difference = meter - x + 1
                grid = addLeft(grid, difference)
                x += difference - 1
            for i in range(meter):
                x -= 1
                grid[y][x] = "#"

        if dir == "U":
            if y - meter < 0:
                difference = 0 + (y - meter)
                grid = addUp(grid, difference)
                y += difference
            print(y)
            for i in range(meter):
                y -= 1
                grid[y][x] = "#"
        
        if dir == "D":
            if y + meter > len(grid):
                difference = (y + 1 + meter) - len(grid)
                grid = addDown(grid, difference)
            for i in range(meter):        
                y += 1
                grid[y][x] = "#"

    total = 0
    for g in grid:
        l = 0
        r = len(g)-1
        while g[l] != "#":
            l +=1
        while g[r] != "#":
            r -=1
        total += (r-l)+1
    print(total)
