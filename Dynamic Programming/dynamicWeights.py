# Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
# In other words, given two integer arrays val[0...n-1] and wt[0...n-1] which represent values and weights associated with n items respectively.
# Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.
# You cannot break an item
#
vals = [46, 8, 44, 73, 73, 64, 28, 31, 76, 9, 9, 64, 52, 5, 53, 94, 16, 43, 51, 14, 49, 18, 81, 52, 6, 6, 78, 71, 8, 86, 18, 62, 43, 55, 2, 90, 42, 47, 19, 25, 7, 2, 65, 78, 49, 62, 55, 63, 99, 71, 98, 74, 58, 35, 34, 92, 95, 90, 36, 57, 65, 76, 100, 100, 76, 64, 65, 60, 96, 15, 16, 29, 22, 62, 20, 52, 22, 6, 3, 97, 6, 12, 95, 42, 47, 79, 28, 20, 16, 97, 40, 48, 28, 54, 79, 81, 64, 47, 85, 97]
wts = [87, 8, 54, 62, 36, 43, 52, 51, 86, 31, 18, 15, 49, 76, 31, 34, 49, 4, 73, 4, 86, 53, 95, 25, 88, 89, 29, 93, 74, 87, 61, 11, 94, 32, 53, 26, 7, 21, 76, 12, 46, 3, 71, 16, 31, 70, 64, 73, 65, 75, 79, 89, 82, 70, 27, 19, 12, 54, 52, 75, 35, 77, 21, 84, 59, 31, 94, 28, 18, 56, 49, 79, 83, 82, 76, 34, 4, 53, 42, 4, 20, 50, 89, 88, 85, 29, 31, 82, 20, 98, 56, 19, 99, 2, 30, 56, 1, 15, 66, 34]

W = 500

bpVal = 0
bpWt = 0
mem = [[0,0]] * len(vals)
# def generateInputs(ln):
# 	from random import randint
# 	wtSeed = [0] * ln
# 	valsSeed = wtSeed[:]

# 	for i in xrange(ln):
# 		wtSeed[i] = randint(1,100)
# 		valsSeed[i] = randint(1,100)
# 	print wtSeed
# 	print valsSeed

# Initializing hash of weight value pairs organized by valPerWeight and extraWeight
valPerWtHash = {}
for i in xrange(len(vals)):
	hashKey1 = vals[i] // wts[i]
	hashKey2 = vals[i] % wts[i]

	if hashKey1 not in valPerWtHash:
		valPerWtHash[hashKey1] = {}

	if hashKey2 not in valPerWtHash[hashKey1]:
		valPerWtHash[hashKey1][hashKey2] = []

	valPerWtHash[hashKey1][hashKey2].append([vals[i], wts[i]])

#Sorting hash so we start with most efficient weights
valPerWtSort = sorted(valPerWtHash.keys())[::-1]


#Functions that digs through memory for latest backpack that can fit weight
def findLatestPack(wt, counter):
	while counter >= 0:
		if wt + mem[counter][1] <= W:
			return mem[counter]
		counter -= 1
	return [0,0]

#DP loop
counter = 0
for valRate in valPerWtSort:
	hashSort = sorted(valPerWtHash[valRate].keys())[::-1]
	for valExtra in valPerWtHash[valRate]:
		for wtValPair in valPerWtHash[valRate][valExtra]:
			val = wtValPair[0]
			wt = wtValPair[1]  # DP Logic Starts here

			removeUntilAdd = findLatestPack(wt, counter - 1) # Finds latest backpack version from mem where this weight can be added
			ruaVal = removeUntilAdd[0]
			ruaWt = removeUntilAdd[1]

			if ruaVal + val > bpVal:
				bpWt = ruaWt + wt
				bpVal = ruaVal + val


			mem[counter] = [bpVal, bpWt]
			counter += 1

print "Value: {0} | Weight: {1}".format(bpVal,bpWt)


#memory has 2 dimensions-- total val, total weight


# 18886244410 - Statefarm
