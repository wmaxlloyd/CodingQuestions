# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.
#
# Assumptions:
# - Any array is a subset of itself
# - Empty array is subset of all possible sets
# - Sets are given as arrays
# - For recursion: There are less than 1000 elements in input nums (Stack limit)
# - Implementation of For loop will get around stack limit
# - Sub list is an array of values where each value is in the origional list
# - input array contains no repeating values

inputNums = [2,2,2,4,5,6]

#Time complexity O(n * 2^n)
#Space complexity O(2^(n-1))

#recursion
def findSubsets(nums, subsetList=[[]], iterator=0):
	newList = []
	for subset in subsetList:
		newList.append(subset + [nums[iterator]]) #Most time complexity
	iterator += 1
	if iterator < len(nums):
		return findSubsets(nums, subsetList + newList, iterator)
	else:
		return subsetList + newList

print "Recursion:"
print findSubsets(inputNums)

#while loop
# Time complexity O(n * 2^n)
print "For Loop:"
subsetList = [[]]

for i in xrange(len(inputNums)):
	newList = []
	for subset in subsetList:
		newList.append(subset + [inputNums[i]])
	subsetList += newList
print subsetList

#What if there are duplicate values?
#
print "Recursion (Dups):"

# Time complexity: O(2^(n-D)) D = number of duplicates
# Space complexity: O(2^(n-1))
# Assumptions:
# - Less than 1000 unique values
# - All elements can be dictionary definitions: All elements are strings, ints or dictionaries

listHash = {}
for num in inputNums:
	if num not in listHash:
		listHash[num] = 1
	else:
		listHash[num] += 1

uniqueVals = listHash.keys()

def findSubsetsDup(nums, subsetList=[[]], iterator=0):
	value = uniqueVals[iterator]
	occurances = listHash[value]
	newSubsets = [ subset + [value] for subset in subsetList ]
	for i in xrange(1, occurances):
		newSubsets += [ subset + [value] for subset in newSubsets ]

	iterator += 1
	if iterator < len(uniqueVals):
		return findSubsetsDup(nums, subsetList + newSubsets, iterator)
	else:
		return subsetList

print list(findSubsetsDup(inputNums))


