
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)

# Example 2:
# coins = [2], amount = 3
# return -1.

# Note:
# You may assume that you have an infinite number of each kind of coin.
#
coins = [1,2,5,8,7,9]
coins.sort()
coins = coins[::-1]
amount = 25

leastCoins = [-1] * (amount + 1)
for coin in coins:
	leastCoins[coin] = 1

for i in xrange(amount + 1):
	if leastCoins[i] != -1:
		continue
	for coin in coins:
		if coin < i:
			if leastCoins[i - coin] != -1:
				leastCoins[i] = leastCoins[i - coin] + 1
				break

print leastCoins[amount]

