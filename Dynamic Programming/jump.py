# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# For example:
# A = [2,3,1,1,4], return true.

# A = [3,2,1,0,4], return false.
#

A = [3,2,1,0,4]

truthArr = [False] * len(A)

for i in xrange(len(A)-1,-1,-1):
	for j in xrange(1, A[i] + 1):
		try:
			if truthArr[i + j]:
				truthArr[i] = True

		except:
			truthArr[i] = True #Jump off end of array

print truthArr[0]