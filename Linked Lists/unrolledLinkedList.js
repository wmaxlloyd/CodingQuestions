// The idea is that the candidate "owns" a class whose clients think of it storing a zero-based array of integers. Inside this class, the integers are kept inside a linked list, where on each node of the linked list is a fixed-size buffer of ints. We can call the per-node buffers the "local" arrays, and the view of the list of integers that the class clients would have could be considered the "global" array. You can read about this data structure on wikipedia, "unrolled linked list". The advantage it has over a normal array is that you can insert and delete from the middle of the array without needing to take a O(n) cost, since all that needs to be "fixed" is the local array on the node being added or deleted to, rather than shifting nearly every element of the global array.

// const int MAX_SIZE = 4;

// struct Node {
//   int count;  // number of elements filled in buffer
//   int buffer[MAX_SIZE];
//   Node* next;
// };

// // assume this variable points to start of list.
// Node* HEAD;
// example: global array: [10, -1, 4, 0, 3, -6]

// stored as:

// node 1: [10, -1], count=2

// node 2: [4, 0, 3], count=3

// node 3: [-6], count=1

// (note that I try to avoid an example that has every node full)

// The warmup question is to code this function: int getAtIndex(int index), it is passed in an index to the "global" array, and should return the element found there.

// Example: input: 3, output 0 (since 0 is at zero-based global index 3)

const MAX_SIZE = 5
class Node {
    constructor(localArray = []) {
        if (!Array.isArray(localArray)) {
            throw new Error('incorrect type provided')
        }
        if (localArray.length > MAX_SIZE) {
            throw new Error('too big')
        }
        this.value = localArray
        this.next = undefined
    }
    add(value, index = undefined) {
        if (this.value.length + 1 > MAX_SIZE) {
            throw new Error('not enough room')
        }
        if (index == undefined) {
            this.value.push(value)
        } else {
            this.value.splice(index, 0, value)
        }
    }
    count() {
        return this.value.length
    }
    isFull() {
        return this.value.length >= MAX_SIZE
    }
}

class UnrolledList {
    constructor(...values) {
        this.startNode = new Node()
        let node = this.startNode
        while (values.length) {
            while (!node.isFull() && values.length) {
                node.add(values.shift())
            }
            if (values.length) {
                node.next = new Node()
                node = node.next
            }
        }
    }

    print() {
        let node = this.startNode
        while (node) {
            console.log(node.value)
            node = node.next
        }
    }

    // Is index always an int?
    // Is index always positive or 0?
    get(index) {
        let indexLeft = index
        let node = this.startNode
        while(indexLeft + 1 > node.count()) {
            if (!node.next) {
                throw new Error('index too large')
            }
            indexLeft -= node.count()
            node = node.next
        }
        return node.value[indexLeft]
    }

    insertAtIndex(value, index) {
        let indexLeft = index
        let node = this.startNode
        while(indexLeft + 1 > node.count()) {
            if (!node.next) {
                throw new Error('index too large')
            }
            indexLeft -= node.count()
            node = node.next
        }
        if (!node.isFull()) {
            node.add(value, indexLeft)
            return
        }
        this.cutNodeInHalf(node)
        if (indexLeft == 0) {
            node.add(value, 0)
            return
        }
        return this.insertAtIndex(value,index)
    }

    cutNodeInHalf(node) {
        const nodeArray = node.value
        const sliceIndex = Math.floor(nodeArray.length / 2)
        node.value = nodeArray.slice(0, sliceIndex)
        const intermediateNode = new Node(nodeArray.slice(sliceIndex))
        const nextNode = node.next
        node.next = intermediateNode
        intermediateNode.next = nextNode
        return node
    }
}

const unrolledList = new UnrolledList(1,2,3,4,5,6,7,8,9)
unrolledList.print()
unrolledList.insertAtIndex('test', 3)
unrolledList.print()
console.log(unrolledList.get(3))
