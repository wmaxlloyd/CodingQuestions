# Clone a linked list with next and random pointer

from linkedList import generateRandomPointerLinkedList, Node
linkedList = generateRandomPointerLinkedList(["a","b","a","c","d","e"])

printList = linkedList
while printList.next:
    print(f"Current: {printList.value} | Next: {printList.next.value} | Random: {printList.random.value} | Random Id: {id(printList.random)}")
    printList = printList.next

linkedListToCopy = linkedList
nodeMap = {}
linkedListCopy = Node(linkedList.value)
currentLinkedListCopy = linkedListCopy

getNodeId = lambda node: str(id(node))
while linkedListToCopy.next:
    nodeId = getNodeId(linkedListToCopy)
    if nodeId not in nodeMap:
        nodeMap[nodeId] = currentLinkedListCopy
    
    nextNodeId = getNodeId(linkedListToCopy.next)
    if nextNodeId in nodeMap:
        currentLinkedListCopy.next = nodeMap[nextNodeId]
    else:
        newNode = Node(linkedListToCopy.next.value)
        currentLinkedListCopy.next = newNode
        nodeMap[nextNodeId] = newNode
    
    randomNodeId = getNodeId(linkedListToCopy.random)
    if randomNodeId in nodeMap:
        currentLinkedListCopy.random = nodeMap[randomNodeId]
    else:
        newNode = Node(linkedListToCopy.random.value)
        currentLinkedListCopy.random = newNode
        nodeMap[randomNodeId] = newNode

    linkedListToCopy = linkedListToCopy.next
    currentLinkedListCopy = currentLinkedListCopy.next


print("---------------")
printList = linkedListCopy
while printList.next:
    print(f"Current: {printList.value} | Next: {printList.next.value} | Random: {printList.random.value} | Random Id: {id(printList.random)}")
    printList = printList.next