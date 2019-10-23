# Given an array,find the maximum j – i such that arr[j] > arr[i]

inputArray = [100,200,8,4,6,3,6,9,8,3,5,3,6,3,5,7,8,5,0]

pointerDifference = len(inputArray) - 1
answer = None

while pointerDifference > 0:
    p1 = 0
    p2 = p1 + pointerDifference
    while p2 < len(inputArray):
        if inputArray[p2] > inputArray[p1]:
            answer = (p1,p2)
            break
        p1 += 1
        p2 += 1
    if answer:
        break
    pointerDifference -= 1

print(answer)
