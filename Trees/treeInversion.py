# Invert a binary tree.
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1

from createATree import BiNode

tree = BiNode(5)
tree.createTree(range(2**3 - 2))

def invertTree(tree):
	invertedTree = BiNode(tree.value)
	if tree.left != None:
		invertedTree.right = invertTree(tree.left)
	if tree.right != None:
		invertedTree.left = invertTree(tree.right)
	return invertedTree

tree.printTree()
print "------------------------ NEW TREE ------------------------------"
invertTree(tree).printTree()