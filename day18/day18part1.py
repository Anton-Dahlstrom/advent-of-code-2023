def addRight(arrays, length):
    for array in arrays:
        array += ["."]*length
    return arrays

def addLeft(arrays, length):
    for i in range(len(arrays)):
        arrays[i] = ["."]*length + arrays[i]
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
                difference = meter - x
                grid = addLeft(grid, difference)
                x += difference
            for i in range(meter):
                x -= 1
                grid[y][x] = "#"

        if dir == "U":
            if y - meter < 0:
                difference = meter - y
                grid = addUp(grid, difference)
                y += difference
            for i in range(meter):
                y -= 1
                grid[y][x] = "#"
        
        if dir == "D":
            if y + meter >= len(grid):
                difference = (y + meter + 1) - len(grid)
                grid = addDown(grid, difference)
            for i in range(meter):        
                y += 1
                grid[y][x] = "#"
    left = []
    right = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "#":
                left.append([i, j])
                break
        for k in reversed(range(len(grid))):
            if grid[i][k] == "#":
                right.append([i, k])
                break

    # 55055 too high
    # 44184 too high