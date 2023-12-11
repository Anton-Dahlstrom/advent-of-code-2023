import copy

directions = {"|": [[1, -1], [0, 0]], "-": [[0, 0], [1, -1]],
               "L": [[0, -1], [1, 0]], "J": [[0, -1], [0, -1]],
              "7": [[1, 0], [0, -1]], "F": [[1, 0],[1, 0]]}

with open("day10/day10input.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "S":
                ycoord, xcoord = j, j
                start = [i, j]

    def solution(start):
        y = 0
        x = 1
        counter = 0
        for i in range(0, 2):
            axis = i
            for j in range(-1,2,2):
                step = j
                position = start.copy()
                char = ""
                while char != "S" or char != ".":
                    position[axis] += step
                    counter += 1
                    char = lines[position[y]][position[x]]
                    if char in directions:  
                        if step * -1 in directions[char][axis]:
                            directionCopy = copy.deepcopy(directions[char])
                            toPop = directionCopy[axis].index(step * -1)
                            directionCopy[axis].pop(toPop)
                            for axi in range(0, len(directionCopy)):
                                for num in directionCopy[axi]:
                                    if num:
                                        axis = axi
                                        step = num
                        else:
                            break         
                    else:
                        break
                if char == "S":
                    return counter//2
print(solution(start))