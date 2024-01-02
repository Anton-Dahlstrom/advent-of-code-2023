with open("day7/day7input.txt", "r") as file:
    values = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

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
        sortedHands.append([temp, hand[1]])

    finalHands = []
    while sortedHands:
        index = 0
        highest = [[0]]
        found = False
        for i in range(len(sortedHands)):
            hand = sortedHands[i][0]
            for j in range(len(hand)-1):
                if hand[j][0] == highest[j][0]:
                    continue
                elif hand[j][0] > highest[j][0]:
                    highest = hand
                    index = i
                    found = True
                    break
                else:
                    found = True
                    break
            if not found:
                for k in range(len(hand)):
                    if hand[k][1] > highest[k][1]:
                        highest = hand
                        index = i
                    elif hand[k][1] == highest[k][1]:
                        continue
                    else:
                        break
        finalHands.append(sortedHands.pop(index))
        print(finalHands[-1])

    answer = 0
    for i in range(len(finalHands)):
        answer += (i+1) * int(finalHands[i][1])
        # print(answer)
    print(answer)

    # 252997218 too high