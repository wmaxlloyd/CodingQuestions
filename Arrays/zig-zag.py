# Given an array A (distinct elements) of size N. Rearrange the elements of array in zig-zag fashion. The converted array should be in form a < b > c < d > e < f. The relative order of elements is same in the output i.e you have to iterate on the original array only.

# Input:
# The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains two lines of input. The first line contains a single integer N denoting the size of array.
# The second line contains N space-separated integers denoting the elements of the array.

# Output:
# For each testcase, print the array in Zig-Zag fashion.

inputArray = [2,4,7,3,5,3,2,5,7,9,7,0]

p1 = 0
p2 = 1
assending = True

while p2 < len(inputArray):
    item1 = inputArray[p1]
    item2 = inputArray[p2]
    switch = False
    if assending and (item1 > item2):
        switch = True
    if not assending and (item1 < item2):
        switch = True
    if switch:
        inputArray[p1] = item2
        inputArray[p2] = item1  
    p1+= 1 
    p2+= 1
    assending = not assending

print(inputArray)