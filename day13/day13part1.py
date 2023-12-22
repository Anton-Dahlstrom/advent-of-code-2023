# Find a way to create one solution, then work with pointers to create the rest. Count how many you can create.
# Implement multiple loops over the same string to find all permutations. 
# Needs to start at the correct goal, change index that we turned broken into a working spring and keep going until it fails the first time.
# Then we look at the previous goal until there are no more.

def verticalSearch(arrays, index):
    converted = ""
    for array in arrays:
        converted += array[index]
    return converted

total = 0
count = 0
with open("day13/day13input.txt", "r") as file:
    lines = file.readlines()
    patterns = []
    temp = []
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
        if lines[i]:
            temp.append(lines[i])
            if i == len(lines) -1:
                patterns.append(temp)
        else:
            patterns.append(temp)
            temp = []

    failed = False
    for pnum, pattern in enumerate(patterns):   
        for i in range(1, len(pattern)):
            if pattern[i] == pattern[i-1]:
                l = i-1
                r = i
                while l >= 0 and r < len(pattern):
                    if pattern[l] == pattern[r]:
                        l -= 1
                        r += 1
                    else:
                        failed = True
                        break
                if not failed:
                    total += i*100
                    count += 1
                    break
                else:
                    failed = False

        previous = ""
        current = ""
        for j in range(0, len(pattern[0])):
            current = verticalSearch(pattern, j)
            if current == previous:
                l = j-1
                r = j
                while l >= 0 and r < len(pattern[0]):             
                    if verticalSearch(pattern, l) == verticalSearch(pattern, r):
                        l -= 1
                        r += 1
                    else:
                        failed = True
                        break
                if not failed:
                    total += j
                    count += 1
                    break
                else:
                    failed = False
            previous = current
            current = ""

print(total)
# 33381 too low