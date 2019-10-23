# Implement int sqrt(int x).

# Compute and return the square root of x.

# x is guaranteed to be a non-negative integer.


# Example 1:

# Input: 4
# Output: 2
# Example 2:

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.
#

num = 123456789045678
ub = num
lb = 1

# while ub > lb+1:
# 	newMid = (lb+ub) // 2
# 	if newMid ** 2 > num:
# 		ub = newMid
# 	else:
# 		lb = newMid
# print lb

#With a square --> Large memory complexity
#

while ub > lb+1:
	newMid = (lb+ub) // 2
	if num // newMid < newMid:
		ub = newMid
	else:
		lb = newMid
print lb
