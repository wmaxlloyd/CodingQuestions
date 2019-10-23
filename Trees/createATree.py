class BiNode:
	def __init__(self,value):
		self.value = value
		self.right = None
		self.left = None

	def addNode(self, value, side):
		newNode = BiNode(value)
		if getattr(self,side) == None:
			setattr(self,side,newNode)
		else:
			setattr(NewNode,side, getattr(self,side))
			setattr(self,side,newNode)

	def addLeft(self,value):
		self.addNode(value,"left")

	def addRight(self,value):
		self.addNode(value,"right")

	def printTree(self):
		right = self.right.value if self.right != None else None
		left = self.left.value if self.left != None else None
		if right or left:
			print " " + str(self.value) + " "
			print "/ \\ "
			print left, right
			print "--------"

			if left != None:
				self.left.printTree()
			if right != None:
				self.right.printTree()

	def delete(self):
		self.value = None

	def createTree(self, arr):
		if len(arr)+1 & len(arr)+2 != 0:
			print "Not formatted correctly"
			print arr
			return None

		if self.left:
			self.left.delete()
		if self.right:
			self.right.delete()

		newLeft = arr[1:len(arr)//2]
		newRight = arr[len(arr)//2 + 1:]

		self.left = BiNode(arr[0])
		if len(newLeft) > 0:
			self.left.createTree(newLeft)

		self.right = BiNode(arr[len(arr)//2])
		if len(newRight) > 0:
			self.right.createTree(newRight)

if __name__ == "__main__":
	tree = BiNode(5)
	tree.createTree([None,None,None,1,2,3])
	tree.printTree()
