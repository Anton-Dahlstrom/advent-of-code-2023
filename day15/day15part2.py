import re

def hashAlgo(chars):
    value = 0
    for char in chars:
        value += ord(char)
        value *= 17
        value %= 256
    return value
with open("day15/day15input.txt", "r") as file:
    lines = file.readlines()
    labelArray = []
    for i in range(len(lines)):
        labelArray += lines[i].strip().split(",")
    boxes = {}
    for slot in labelArray:
        input = re.split("=|-", slot)
        label = input[0]
        boxIndex = hashAlgo(label)
        operator = slot[len(label)]
        if operator == "=":
            value = int(slot[-1])
            if boxIndex in boxes:
                found = False
                for i in range(len(boxes[boxIndex])):
                    if label == boxes[boxIndex][i][0]:
                        boxes[boxIndex][i][1] = value
                        found = True
                if not found:
                    boxes[boxIndex].append([label, value])
            else:
                boxes[boxIndex] = [[label, value]]
            continue
        if boxIndex in boxes:
            array = boxes[boxIndex]
            for i in range(len(array)):
                if label == boxes[boxIndex][i][0]:
                    boxes[boxIndex].pop(i)
                    break

    total = 0
    for key in boxes:
        if boxes[key]:
            for i in range(len(boxes[key])):
                temp = (key+1) * (i+1) * boxes[key][i][1]
                total += temp  
    print(total)
