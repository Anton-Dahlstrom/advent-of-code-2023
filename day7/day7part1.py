with open("day7/day7input.txt", "r") as file:
    values = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

    def textToValues(text, values):
        temp = []
        for char in text:
            if char in values:
                temp.append(values[char])
            else:
                temp.append(int(char))
        return temp
    
    def compare(first, second, index, position):
        if first[index][position] == second[index][position]:
            return False
        elif first[index][position] > second[index][position]:
            return 1
        else:
            return 2
        
    lines = file.readlines()
    hands = []
    hmap = {}
    sortedHands = []
    for line in lines:
        hands.append(line.strip().split(" "))
    for hand in hands:
        cards = "".join(reversed(sorted(hand[0])))
        temp = []
        hmap = {}
        for card in cards:
            if card not in hmap:
                hmap[card] = 1
            else:
                hmap[card] += 1
        for key in hmap:
            if key in values:
                value = values[key]
            else:
                value = int(key)
            temp.append([hmap[key], value])
        temp.sort(reverse=True)
        cardsValues = textToValues(hand[0], values)

        sortedHands.append([temp, hand[1], cardsValues, hand[0]])

    finalHands = []
    while sortedHands:
        index = 0
        highest = [[[0]], 0, [0]]
        for i in range(len(sortedHands)):
            hand = sortedHands[i][0]
            betSize = sortedHands[i][1]
            text = sortedHands[i][2]
            stop = False
            for j in range(len(hand)):
                result = compare(hand, highest[0], j, 0)
                if result:
                    stop = True
                    if result == 1:
                        highest = [hand, betSize, text]
                        index = i
                    break
            if not stop:
                for k in range(len(text)):
                    if text[k] > highest[2][k]:
                        highest = [hand, betSize, text]
                        index = i
                        break
                    elif text[k] < highest[2][k]:
                        break
        finalHands.append(sortedHands.pop(index))

    answer = 0
    for i in reversed(range(len(finalHands))):
        print(i)
        print(finalHands[i])
        answer += (i+1) * int(finalHands[i][1])
    print(answer)
    # 254205094
    # 254205094 too high
    # 252997218 too high