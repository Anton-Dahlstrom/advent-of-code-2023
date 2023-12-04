with open("day3/day3input.txt", "r") as file:
    lineIndex = file.readlines()
    toAdd = []
    numbers = []
    hmap = {}
    stars = {}
    nums = {}
    multiplied = 0
    for i, line in enumerate(lineIndex):
        if i > 2:
            if (i-2) in stars:
                for star in stars[i-2]:
                    for row in range(i-3,i):
                        if row in hmap:                            
                            for col in range(star-1, star+2):
                                if col in hmap[row]:
                                    nums[hmap[row][col]] = 1
                    temp = []
                    if len(nums) == 2:
                        for key in nums:
                            temp.append(key)
                        multiplied += (temp[0] * temp[1])
                    nums = {}      
                del stars[i-2]       
        for j, char in enumerate(line):
            if char == "*":
                if i in stars:
                    stars[i].append(j)
                else:
                    stars[i] = [j]
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
                        numberString = ""
                        for k in range(toAdd[2], toAdd[3]+1):
                            numberString += lineIndex[toAdd[1]][k]
                        numbers.append(numberString)
                        if i not in hmap:
                            hmap[i] = {}
                        if len(hmap) > 3:
                            hmap.pop(min(hmap))
                        for h in range(toAdd[2], toAdd[3]+1):
                            hmap[i][h] = int(numberString)
                    toAdd = []
    for lastLine in range(len(lineIndex)-3,len(lineIndex)):
        if lastLine in stars:
            for star in stars[lastLine]:
                for row in range(lastLine-1,lastLine+2):
                    if row in hmap:                            
                        for col in range(star-1, star+2):
                            if col in hmap[row]:
                                nums[hmap[row][col]] = 1
                temp = []
                if len(nums) == 2:
                    for key in nums:
                        temp.append(key)
                    multiplied += (temp[0] * temp[1])
                nums = {}
print("ANSWER: ", multiplied)