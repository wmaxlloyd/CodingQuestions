# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

# Example 1:
# Input:

# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
#
#Assumptions:
# - String included unicode characters
# - special characters count as chars in palendrom (should not be ignored)
#
# Time complexity: O(n)
# Space complexity: O(1)
s = "lsdkjf098sdf098wjflksjf098;;;"

mem = [0,""] * len(s)
# mem element --> [longestPal, single letter]

charHash = {}
for char in s:
	char = char.lower()
	if char in charHash:
		charHash[char] += 1
	else:
		charHash[char] = 1

print charHash
longestPal = 0
extraChar = None

for char in charHash:
	if charHash[char] % 2 == 0:
		longestPal += charHash[char]
	else:
		if extraChar:
			if charHash[char] > charHash[extraChar]:
				longestPal += charHash[char] - charHash[extraChar]
		else:
			longestPal += charHash[char]
		extraChar = char
print longestPal
