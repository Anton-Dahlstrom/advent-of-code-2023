# A function that searches through all paths from a starting node to a goal node.
# Need to see how many other paths each path kills
# If a path kills two other paths that would otherwise co-exist it can't be an optimal route
# How do I find the most paths without overlaps?

# When two paths are identical except one is longer the longer has to go.
# I can find which paths can co-exist and which can't by iterating.
# Visited should be a hmap.

# The recursive function that searches through all the nodes has to remember where it's already been and what the goal is.
def searchNode(node, goal, nodes, visited, paths):
    visited.append(node)
    for path in nodes[node]:
        if path == goal:
            paths.append(visited)
        else:
            if path not in visited:
                searchNode(path, goal, nodes, visited.copy(), paths)


with open("day25/day25input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    hmap = {}
    for line in lines:
        text = line.split(":")
        node = text[0]
        paths = text[1].strip().split(" ")
        if node not in hmap:
            hmap[node] = {}
        for path in paths:
            if path not in hmap[node]:
                hmap[node][path] = 1
            if path not in hmap:
                hmap[path] = {node: 1}   

    pathArray = []
    visited = []
    searchNode("jqt", "hfx", hmap, visited, pathArray)

# If an array is too short to keep comparing it's the winner so we can pop and save it while we throw out all 
# the other "living" arrays.

# Remove all the indexes of arrays that don't follow the same paths.
# When we find the shortest or only permutation of a path we pop to save it and pop all the other indexes.
test = [['jqt', 'rhn', 'xhk'], ['jqt', 'rhn', 'bvb', 'xhk'], ['jqt', 'rhn', 'bvb'], ['jqt', 'rhn'], ['jqt', 'xhk'], ['jqt', 'nvd', 'lhk', 'cmg', 'bvb', 'xhk'], ['jqt', 'nvd', 'lhk', 'cmg', 'bvb']]

asd = list(range(len(test)))
new = []
saving = []

# Indexes of all the lists
indexes = list(range(len(test)))

# Looks at each node in the path of index 0
while indexes:
    temp = [[k, value] for k, value in enumerate(indexes.copy())]
    # temp = indexes.copy()
    for i, value in enumerate(test[indexes[0]]):
        # Makes a copy of the indexes we have so we can remove paths that don't overlap with the one we're looking at
        # from the temp array and delete all the others that are left once we find the shortest one.
        found = False
        for j, index in enumerate(temp):
            # If the value of the array in this index doesn't match we remove it from temp.
            if test[index[1]][i] != value:
                temp.pop(j)
            # When we find the shortest array we pop all of them from indexes and break the search
            elif len(test[index[1]]) == i+1:
                found = True
                print(index, j)
                shortest = index[1]
                saving.append(shortest)
        if found:
            toPop = [duplicate for duplicate in temp[::-1]]
            for duplicate in toPop:
                indexes.pop(duplicate[0])
            break
        
print(saving)