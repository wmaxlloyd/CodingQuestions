# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

arr = [3,0,1,2,4,5,6,7,9,10]

print "Non-bitwise"
arrLen = len(arr)

print (arrLen**2 + arrLen)//2 - sum(arr) #space complexity O(1), time complexity O(n)

print "Bitwise"
#Assumptions:
# - No repeating numbers
# - Always a number
# - What size?
# - length is n where n is the max number in the array
# - Target space / time complexity -- > O(n), O(1)
# - Bitwise operation eliminates danger of overflow

x1 = 0
x2 = 0

for num in xrange(len(arr) + 1):
	if num < len(arr):
		x1 ^= arr[num]
	x2 ^= num
print x1 ^ x2

#Explaination:
# - a "1" in the binary expression of x1 means that the kth bit is represented an odd number of times in the array
# - a "1" in the binary expression of x2 means that the kth bit is represented an odd number of times in the sequence from 1 to n
#  Findng the XOR between both x1 and x2 shows us all bits that are missing between our array and the sequence from 1 to n
