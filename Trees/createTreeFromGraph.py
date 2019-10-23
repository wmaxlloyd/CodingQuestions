# Turn a graph into a tree

graphRaw = [
    ("A","B"),
    ("A","C"),
    ("B","D"),
    ("D","E"),
    ("B","C"),
    ("E","B"),
    ("A","A")
]

# Make Consumable Tree
graph = {}
for edge in graphRaw:
    if edge[0] in graph:
        graph[edge[0]].add(edge[1])
    else:
        graph[edge[0]] = set(edge[1])
    if edge[1] in graph:
        graph[edge[1]].add(edge[0])
    else:
        graph[edge[1]] = set(edge[0])
print(graph)

def removeRecursiveEdges(parent, prevParents = []):
    recursiveEdges = []
    copiedChildren = graph[parent].copy()
    parents = prevParents + [parent]
    validChildren = copiedChildren.difference(prevParents[-1]) if len(prevParents) else copiedChildren
    for child in validChildren:
        if child not in graph[parent]:
            continue
        if child in parents:
            recursiveEdges.append((parent, child))
            graph[parent].remove(child)
            if child != parent:
                graph[child].remove(parent)
            continue
        if child in graph:
            recursiveEdges += removeRecursiveEdges(child, prevParents + [parent])
    return recursiveEdges

for node in graph:
    removeRecursiveEdges(node)

tree = graph
treeRaw = []

for parent in tree:
    for child in tree[parent]:
        if (child, parent) not in treeRaw:
            treeRaw.append((parent,child))

print(tree)
print(treeRaw)

    
        
            
