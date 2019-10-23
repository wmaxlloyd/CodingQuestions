# Given a non negative integer number num. For every numbers i in the range 0 <= i <= num calculate the number of 1's in their binary representation and return them as an array.

# Example:
# For num = 5 you should return [0,1,1,2,1,2].

# Follow up:

# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

a = 20

print "brute force:"
# Space O(n)
# Time O(n*log(n))

def findOnes(a):
	count = 0
	while a > 0:
		if a&1 == 1:
			count += 1
		a >>= 1
	return count


returnArr = []
for i in xrange(a):
	count = 0
	returnArr.append(findOnes(i))

print returnArr
# Space O(n)
# Time O(n)
# Theory - If you want to know the number of 1s it is a repeating pattern that evolves exponentially where the second half of the sequence is the same as the first with 1 added.
#
# Assumptions:
# - Return array is organized assending
# - Input is always int
# - ints are dynamic length (no max int)

print "Sneaky Way"

returnArr = [0,1]
while len(returnArr) < a:
	stLen = len(returnArr)
	additionLength = stLen if (stLen*2 < a) else a-stLen
	newArr = []
	for i in xrange(additionLength):
		newArr.append(returnArr[i]+1)
	returnArr = returnArr + newArr

print returnArr



#Space goal O(n)

