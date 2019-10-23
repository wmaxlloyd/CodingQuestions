# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.
# Time complexity: O(n * m * log(m))

s = ["eat", "tea", "tan", "ate", "nat", "bat"]

print "Sorting"

returnHash = {}
for element in s:
	sortEle = "".join(sorted(element))
	if sortEle in returnHash:
		returnHash[sortEle].append(element)
	else:
		returnHash[sortEle] = [element]

for key in returnHash:
	print returnHash[key]

print "Hash"

returnHash2 = {}
for element in s:
	elementHash = {}
	for c in element:
		if c in elementHash:
			elementHash[c] += 1
		else:
			elementHash[c] = 1
	key = ""
	for alpha in sorted(elementHash.keys()):
		key += alpha + str(elementHash[alpha])

	if key in returnHash2:
		returnHash2[key].append(element)
	else:
		returnHash2[key] = [element]
for key in returnHash2:
	print key, returnHash2[key]
