# Given a singly linked list of N nodes. The task is to find middle of the linked list. For example, if given linked list is 1->2->3->4->5 then output should be 3. 

# If there are even nodes, then there would be two middle nodes, we need to print second middle element. For example, if given linked list is 1->2->3->4->5->6 then output should be 4.

from linkedList import generateLinkedList

inputLL = generateLinkedList([1,2,3,7,8,4,9,0,3,9,3,45,3,453,4,3,5,5,3,4,4,53,45,345])

listIndex = 0
midpointNode = (inputLL, inputLL)
currentList = inputLL
listEmpty = False

while not listEmpty:
    if (listIndex % 2 == 1):
        midpointNode = (midpointNode[0], midpointNode[0].next)
    else:
        midpointNode = (midpointNode[1], None)
    print(midpointNode)
    if currentList.next:
        currentList = currentList.next
        listIndex += 1
    else:
        listEmpty = True


print(midpointNode[0].value)
if midpointNode[1]:
    print(midpointNode[1].value)