import random

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    
def generateLinkedList(inputList):
    linkedList = Node(inputList[0])
    currentLink = linkedList
    for item in inputList[1:]:
        nextLink = Node(item)
        currentLink.next = nextLink
        currentLink = nextLink
    return linkedList

def generateRandomPointerLinkedList(inputList):
    nodes = [Node(value) for value in inputList]
    for node in nodes:
        node.random = nodes[random.randint(0,len(inputList) - 1)]
    for (index, node) in enumerate(nodes[:-1]):
        node.next = nodes[index + 1]
    return nodes[0]