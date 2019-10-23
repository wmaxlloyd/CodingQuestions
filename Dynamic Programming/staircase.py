# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.
#

n = 30

mem = [0] * (n+1)
mem[1] = 1
mem[2] = 2

# Unique options are nUnique[n-1] + nUnique[n-2]
#
for i in range(3, n+1):
	mem[i] = mem[i - 1] + mem[i -2]

print(mem[n])