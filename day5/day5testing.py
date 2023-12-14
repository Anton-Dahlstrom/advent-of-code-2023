import copy
with open("day5/day5input.txt", "r") as file:

    lines = file.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
        
    seeds = []
    temp = []
    for line in lines:
        if not line:
            break
        for number in line.split(" "):
            if number.isdigit():
                if temp:
                    temp.append(temp[0] + int(number)-1)
                    seeds.append([temp,temp])
                    temp = []
                else:
                    temp.append(int(number))
    seeds = sorted(seeds)
    print(seeds)

    ranges = []
    temp = []
    # Adding ranges for each stage. First array is destination range, second is source.
    for line in reversed(lines):
        if line:
            if line[0].isnumeric():
                nums =[int(line) for line in line.split(" ")]
                temp.append([[nums[0], nums[0] + nums[2]-1], [nums[1], nums[1] + nums[2]-1]])
                # temp[1].append()
            else:
                if temp:
                    ranges.append(temp)
                    temp = []

    # Sorts ranges and adding missing bottom and top ranges.
    for i in range(0, len(ranges)):
        ranges[i] = sorted(ranges[i])
        if ranges[i][0][0][0]:
            ranges[i].insert(0, [[0,ranges[i][0][0][0]-1], [0,ranges[i][0][0][0]-1]])
        if ranges[i][-1][0][1] < 100:
            ranges[i].append([[ranges[i][-1][0][1]+1, 100], [ranges[i][-1][0][1]+1, 100]])
    ranges.append(seeds)

    def overlappingRange(toFind, upperList):
        all = []
        for upRan in upperList:
            if upRan[0][0] > toFind[1]:
                break
            elif upRan[0][1] >= toFind[0]:
                overlap = [max(upRan[0][0], toFind[0]), min(upRan[0][1], toFind[1])]
                lowDiff = overlap[0] - upRan[0][0]
                upDiff = upRan[0][1] - overlap[1]
                all.append([upRan[1][0] + lowDiff, upRan[1][1] - upDiff])
        return all
    
    # should return [69, 69], [0, 54]
    checkAll = overlappingRange(ranges[0][0][1], ranges[1])

    def findSmallestSeed(ranges):
        for ran in ranges[0]:
            current = overlappingRange(ran[1], ranges[1])
            for i in range(2, len(ranges)):
                total = []
                for cur in current:
                    temp = overlappingRange(cur, ranges[i])
                    if temp:
                        for tem in temp:
                            total.append(tem)
                if total:
                    current = copy.deepcopy(total)
                else:
                    break
                if i == len(ranges)-1:
                    if total:
                        num = current[0]
                        print(current)
                        return num
                    
    seeds = findSmallestSeed(ranges)
    

    def test(ranges, seedNum):
        for row in ranges[-2::-1]:
            for array in row:
                if seedNum in range(array[1][0], array[1][1]):
                    difference = seedNum - array[1][0]
                    seedNum = array[0][0] + difference
                    break
        return seedNum
    smallest = None

    for i in range(seeds[0], seeds[0]+1):
        result = test(ranges, i)
        if not smallest:
            smallest = result
            print(smallest)
        if result < smallest:
            print(smallest)



    # 24092691 is too high



    # First we need to look for any numbers below the smallest dest/source range
    # Then we look in the ranges above to see if they can produce what we're looking for
    # Repeat until we reach the top
    # If it's not possible we restart the loop and check the next lowest range at the bottom
    # First step is to add the 0 to lowest ranges and top to 100 to each phase.
    # Then we pop the smallest range at the bottom and see if it goes all the way to the top 
    # go up with a range, if the other fits somehow take the larger of the two lower values
    # and the smaller of the upper values (10,20) and (5,15) becomes (10,15)
    # Take the smaller of the bottom part of the range + steps vs top of range when moving up
    # If the lowest point of the range we look up at is higher than the biggest part of our 
    # range we break the search. The search will look like a tree.

