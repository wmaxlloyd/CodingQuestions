# Given a binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# For example:
# Given the below binary tree,

#        1
#       / \
#      2   3
# Return 6.
#
from createATree import BiNode

tree = BiNode(5)
tree.createTree([6,2,4,-1,2000,3])

def findPlugAndMax(tree):
	if tree.right != None:
		rightValues =  findPlugAndMax(tree.right)
		rightPlug = rightValues["plug"] if rightValues["plug"] > 0 else 0
		rightMaxSum = rightValues["maxSum"]
	else:
		rightPlug = 0
		rightMaxSum = 0
	if tree.left != None:
		leftValues =  findPlugAndMax(tree.left)
		leftPlug = leftValues["plug"] if leftValues["plug"] > 0 else 0
		leftMaxSum = leftValues["maxSum"]
	else:
		leftPlug = 0
		leftMaxSum = 0

	return {"plug":max([rightPlug, leftPlug]) + tree.value,"maxSum":max([leftMaxSum, rightMaxSum, leftPlug+tree.value+rightPlug])}

print findPlugAndMax(tree)["maxSum"]



