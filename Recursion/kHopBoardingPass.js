// This is a graph-traversal problem with the "tricky" part being that you can have multiple edges between 2 nodes, and that when one is used in a path, that path cannot re-use it.

// Let a boarding pass have a source and destination.

// struct BoardingPass {
//     string src;
//     string dest;
// };
// So an example boarding pass could be:

// src: 'SEA'
// dest: 'SLC'
// I usually draw out an example of a simple graph you might get from some boarding passes. Let the passes be

// [ {src:'SEA',dest:'SLC'},{src:'SLC',dest:'LAX'},{src:'SEA',dest:'SLC'},{src:'SLC',dest:'SEA'}]
// I can't really draw a graph on the wiki, but 2 edges from SEA to SLC, one edge from SLC to SEA, one edge from SLC to LAX

// The question is to determine if there is a k-hop path from A to B, for a given A, B, and k (and set of passes) The way I ask the question, I am looking for exactly k as the only valid answer. Some people ask this question with an int return type instead of boolean, where they want to know the number of k-hop paths. Other more complicated variants add a timestamp to the passes and the path must respect time-order. On the above example data:

// hasKHopPath with src=SEA, dest=SLC, k=3 returns true: SEA->SLC->SEA->SLC

// hasKHopPath with src=SEA, dest=SLC, k=2 returns false.

// hasKHopPath with src=SEA, dest=LAX, k=4 returns true: SEA->SLC->SEA->SLC->LAX

const edges = [ {src:'SEA',dest:'SLC'},{src:'SLC',dest:'LAX'},{src:'SEA',dest:'SLC'},{src:'SLC',dest:'SEA'}]

const edgesToMap = (edges) => {
    const srcDestMap = {}
    edges.forEach(edge => {
        if (!srcDestMap[edge.src]) {
            srcDestMap[edge.src] = {}
        }
        if (!srcDestMap[edge.src][edge.dest]) {
            srcDestMap[edge.src][edge.dest] = 0
        }
        srcDestMap[edge.src][edge.dest] += 1
    })
    return srcDestMap
}

const srcDestMap = edgesToMap(edges)
console.log(srcDestMap)

const hasKHopPath = (srcDestMap, k, src, dest) => {
    if (!srcDestMap[src]) {
        return false
    }
    if (k === 1) {
        return srcDestMap[src][dest] && srcDestMap[src][dest] > 0
    }
    const foundPath = Object.keys(srcDestMap[src]).find(midDest => {
        mapCopy = JSON.parse(JSON.stringify(srcDestMap))
        mapCopy[src][midDest] -= 1
        return hasKHopPath(mapCopy, k - 1, midDest, dest)
    })
    return !!foundPath
}

console.log(hasKHopPath(srcDestMap, 2, 'SEA', 'LAX'))