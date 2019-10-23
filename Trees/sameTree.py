# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
from createATree import BiNode

tree = BiNode(5)
tree.createTree(range(2**6 - 2))

tree2 = BiNode(5)
tree2.createTree(range(2**6 - 2))
tree2.right.value = None

def compareTrees(tree1, tree2):
	if tree1 == None or tree2 == None:
		if tree1 == tree2:
			return True
		else:
			return False

	if tree1.value == tree2.value:
		return compareTrees(tree1.right,tree2.right) and compareTrees(tree1.left,tree2.left)
	else:
		return False

print compareTrees(tree,tree2)