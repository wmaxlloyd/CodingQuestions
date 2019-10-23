# Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
#

nums = [2,3,5,7]
target = 100
#QUESTIONS--
#Do different sequences count as different combinations?
#Are there negitive numbers
#Can the target be negitive

#Assumptions --
#Non-negitive numbers
#Nums contains ints
#target is one number
#Not more than 2^31-1 bits

mem = [0] * (target+1)

for i in range(target + 1):
	if i in nums:
		mem[i] += 1
	for num in nums:
		if i > num:
			mem[i] += mem[i-num]

print (mem[target])

#If a negitive number in nums is allowed
# There needs to be a restriction that each number can only be used a certain number of times
# If you can use a number as many times as you want then there are alwats infinite possibliites