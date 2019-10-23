# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Write a function to determine if a number is strobogrammatic. The number is represented as a string.

# For example, the numbers "69", "88", and "818" are all strobogrammatic.

# Find all strobogrammatic of length n
#
# Assumptions:
# - n < 1000
# - n is integer
#
# Time complexity: O(4^(n//2))
# Space complexity: Same

n = 5

smap = {
	"6":"9",
	"9":"6",
	"8":"8",
	"0":"0"
}

if n % 2 == 1:
	sList = [num for num in smap]
else:
	sList = [num + smap[num] for num in smap]

def findSStrs(sList, i=1):
	newSList = []
	for num in smap:
		newSList += [num + string + smap[num] for string in sList]
	print newSList[0]
	if len(newSList[0]) >= n:
		return newSList
	else:
		i += 1
		return findSStrs(newSList, i)

print findSStrs(sList)