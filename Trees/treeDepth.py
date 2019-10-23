from createATree import BiNode

tree = BiNode(5)
tree.createTree(range(2**6 - 2))

def findDepth(tree, depth=1):
	if tree.left:
		leftDepth = findDepth(tree.left, depth + 1)
	else:
		leftDepth = depth

	if tree.right:
		rightDepth = findDepth(tree.right, depth + 1)
	else:
		rightDepth = depth
	return max([leftDepth, rightDepth])

print findDepth(tree)

