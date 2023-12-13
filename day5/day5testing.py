
with open("day5/day5input.txt", "r") as file:
    seeds = []
    lines = file.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    temp = []
    for number in lines[0].split(" "):
        if number.isdigit():
            if temp:
                temp.append(temp[0] + int(number)-1)
                seeds.append([temp])
                temp = []
            else:
                temp.append(int(number))

    step = 0
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
            ranges[i].append([[ranges[i][-1][0][1]-1, 100], [ranges[i][-1][0][1], 100]])

    ranges.append(seeds)

    for x in ranges[0]:
        print(x)
        for y in ranges[1]:
            for z in ranges[2]:
        print(x)
    exit()
    # def searchUp(ranges, toSearch, index):
    #     values = []
    #     returning = False
    #     if index == len(ranges)-1:
    #         returning = True
    #     print("ranges index:", index, toSearch, ranges[index])
    #     for upRange in ranges[index]:
    #         if upRange[0][0] > toSearch[1]:
    #             break
    #         elif upRange[0][1] >= toSearch[0]:
    #             next = [max(upRange[0][0], toSearch[0])]
    #             next.append(min(upRange[0][1], toSearch[1]))
    #             if returning:
    #                 return next
    #                 print(next)
    #                 exit()
    #             value = searchUp(ranges, next, index+1)
    #             if value:
    #                 values.append(value)
    #                 return value
    #     return 
    

    def searchUp(ranges, toSearch, index):
        values = []
        returning = False
        if index == len(ranges)-1:
            returning = True
        # print("ranges index:", index, toSearch, ranges[index])
        for upRange in ranges[index]:
            if upRange[0][0] > toSearch[1]:
                break
            elif upRange[0][1] >= toSearch[0]:
                lowDiff = max(upRange[0][0], toSearch[0]) - min(upRange[0][0], toSearch[0])
                topDiff = max(upRange[0][1], toSearch[1]) - min(upRange[0][1], toSearch[1])
                # print(lowDiff, topDiff)
                next = [upRange[1][0] + lowDiff]
                next.append(upRange[1][1] - topDiff)
                values.append(next)
                # if index == 2 or index == 3:
                print("ranges index:", index, toSearch, next, ranges[index])
                # print("THESE:", toSearch, "NEXT:", next, upRange[0])
                if returning:
                    return next
        allRanges = []
        for value in values:
            recur = searchUp(ranges, value, index+1)
            if recur:
                allRanges.append(recur)
        if allRanges:
            return allRanges

        
        # need to keep looking
        return 
    # for start in ranges[0]:
    #     print("ASD", start[1])
    #     # print("START", start)
    #     asd = searchUp(ranges, start[1], 1)
    #     if asd:
    #         print("FINAL:", asd)
    #         break
    # final = asd[0]
    # print(final)
    print(searchUp(ranges, [46,46], 1))
    # for i in reversed(range(0, len(ranges)-1)):
    #     for rangelist in ranges[i]:
    #         # print(rangelist[1][0], rangelist[1][0])
    #         if final in range(rangelist[1][0], rangelist[1][1]):
    #             difference = final - rangelist[1][0]
    #             final = rangelist[0][0] + difference
    #             break

    # for a in ranges:
    #     print(a)
    exit()


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

