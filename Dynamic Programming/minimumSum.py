# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1],
  [1,12,3]
]

gridWidth = len(grid[0])
gridHeight = len(grid)

minSumToPoint = [ [0] * gridWidth for i in range(gridHeight) ]


for heightIndex in range(gridHeight):
    for colIndex in range(gridWidth):
        value = grid[heightIndex][colIndex]
        if heightIndex == 0 and colIndex == 0:
            minSumToPoint[heightIndex][colIndex] = value
        elif heightIndex == 0:
             minSumToPoint[heightIndex][colIndex] = value + minSumToPoint[heightIndex][colIndex - 1]
        elif colIndex == 0:
            minSumToPoint[heightIndex][colIndex] = value + minSumToPoint[heightIndex - 1][colIndex]
        else:
            minSumToPoint[heightIndex][colIndex] = value + min(minSumToPoint[heightIndex - 1][colIndex], minSumToPoint[heightIndex][colIndex - 1])

print(minSumToPoint[-1][-1])