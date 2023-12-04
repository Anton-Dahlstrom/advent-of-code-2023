
with open("day3/day3input.txt", "r") as file:
    lineIndex = file.readlines()
    toAdd = []
    numbers = []
    for i, line in enumerate(lineIndex):
        for j, char in enumerate(line):
            if char.isnumeric():
                if not toAdd:
                    toAdd = [i,i,j,j]
                else:
                    toAdd[3] = j                
            else:
                if toAdd:
                    toSearch = list(toAdd)
                    ylen = len(lineIndex)
                    strippedLine = line.strip()
                    xlen = len(strippedLine)
                    if toAdd[0] > 0:
                        toSearch[0] = toAdd[0]-1
                    if toAdd[1] < ylen:
                        toSearch[1] = toAdd[1]+1
                    if toAdd[2] > 0:
                        toSearch[2] = toAdd[2]-1
                    if toAdd[3] < xlen:
                        toSearch[3] = toAdd[3]+1
                    stopSearch = False
                    for y in range(toSearch[0], toSearch[1]+1):
                        if y >= ylen:
                            break
                        elif stopSearch:
                            break
                        for x in range(toSearch[2], toSearch[3]+1):
                            strippedLine = lineIndex[y].strip()
                            xlen = len(strippedLine)
                            if x >= xlen:
                                break
                          
                            elif strippedLine[x] != ".":
                                if not strippedLine[x].isnumeric():
                                    stopSearch = True
                                    break
                    if stopSearch:                    
                        word = ""
                        for k in range(toAdd[2], toAdd[3]+1):
                            word += lineIndex[toAdd[1]][k]
                        numbers.append(word)
                    toAdd = []

    total = 0
    for number in numbers:
        total += int(number)
    print(total)
