// Implement an iterator class over a binary search tree (BST). 
// Your iterator will be initialized with the root node of a BST. 
// The iterator class must have a hasNext() and a next() method. 
// hasNext() returns a boolean 
// next() returns the next node in an in-order traversal of the BST.

class BstIterator {
    constructor(root) {
        this.root = root
        this.rightHandTree
        this.currentNode = root
        this.returnedCurrent = false
        while (this.currentNode.left) {
            const parent = this.currentNode
            this.currentNode = this.currentNode.left
            this.currentNode.parent = parent
        }
        this.createRightHandTree()
    }

    createRightHandTree() {
        if (this.currentNode.right) {
            this.rightHandTree = new BstIterator(this.currentNode.right)
        }
    }

    hasNext() {
        return (
            this.currentNode != this.root || 
            this.currentNode == this.root && !this.returnedCurrent ||
            this.rightHandTree?.hasNext()
        )
    }

    next() {
        if (!this.returnedCurrent) {
            this.returnedCurrent = true
            return this.currentNode.value
        }
        if (this.rightHandTree?.hasNext()) {
            return this.rightHandTree.next()
        }
        this.currentNode = this.currentNode.parent
        this.createRightHandTree()
        this.returnedCurrent = false
        return this.next()
    }
}