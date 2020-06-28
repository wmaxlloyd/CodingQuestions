// Given a 2-dimensional canvas implement the algorithm that performs the MS Paint bucket functionality.

// Your available arguments are:
// canvas: A 2 dimensional array of Color Objects.
// newColor: The color you are changing target to.
// x: Starting points x coordinate
// y: Starting points y coordinate

// Examples
// Before
//     x x x x x x x x x
//     x x x x x x x x x
//     x x o o o o o x x
//     x x o x x x o x x
//     x x o x x x o x x
//     x x o x x x o x x
//     x x o o o o o x x
//     x x x x x x x x x
//     x x x x x x x x x
 
// After
//     x x x x x x x x x
//     x x x x x x x x x
//     x x o o o o o x x
//     x x o o o o o x x
//     x x o o o o o x x
//     x x o o o o o x x
//     x x o o o o o x x
//     x x x x x x x x x
//     x x x x x x x x x


// Questions about inputs:
// 1. What does `canvas` look like?
// 2. Will x and y always be in bounds?
// 3. What will newColor look like? Should I always expect a certain type?
// 4. Are x and y always going to be ints?

export const bucketFill = (canvas, newColor, x, y) => {
    const oldColor = canvas[y][x]
    if (oldColor == newColor) {
        return
    }
    canvas[y][x] =  newColor
    if (y + 1 < canvas.length && canvas[y + 1][x] == oldColor) {
        bucketFill(canvas, newColor, x, y + 1)
    }
    if (y - 1 >= 0 && canvas[y-1][x] == oldColor) {
        bucketFill(canvas, newColor, x, y - 1)
    }
    if (x + 1 < canvas[y].length && canvas[y][x + 1] == oldColor) {
        bucketFill(canvas, newColor, x + 1, y)
    }
    if (x - 1 >= 0 && canvas[x - 1][y] == oldColor) {
        bucketFill(canvas, newColor, x - 1, y)
    }
    return canvas
}