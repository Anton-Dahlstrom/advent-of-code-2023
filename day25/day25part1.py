# A function that searches through all paths from a starting node to a goal node.
# Need to see how many other paths each path kills
# If a path kills two other paths that would otherwise co-exist it can't be an optimal route
# How do I find the most paths without overlaps?

# The recursive function that searches through all the nodes has to remember where it's already been and what the goal is.

def searchNode(node, goal, visited):
    pass


with open("day25/day25input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    hmap = {}
    for line in lines:
        text = line.split(":")
        node = text[0]
        paths = text[1].strip().split(" ")
        print(paths)
        if node not in hmap:
            hmap[node] = {}
        for path in paths:
            if path not in hmap[node]:
                hmap[node][path] = 1
            if path not in hmap:
                hmap[path] = {node: 1}   
    print(hmap)
    
    for node in hmap:
        traveled = {}
        for endpoint in hmap:
            if node == endpoint:
                continue

asd = ["j", "b", "c"]
if "a" in asd:
    print("hi")