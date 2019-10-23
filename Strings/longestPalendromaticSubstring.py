# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example:

# Input: "babad"

# Output: "bab"

# Note: "aba" is also a valid answer.
# Example:

# Input: "cbbd"

# Output: "bb"
#
s = "ababjabab"
print "brute force"
# Time complexity O(n^3)
# Space Complexity O(1)
# Assumptions
#  - all lowercase alpha characters

maxPal = ""
for i in xrange(len(s)):
	for j in xrange(i+1, len(s) + 1):
		substring = s[i:j]
		revsubstring = substring[::-1]
		if substring == revsubstring:
			if j-i > len(maxPal):
				maxPal = s[i:j]
print maxPal

print "Senaky"

revs = s[::-1]
longestStr = ""
for i in xrange(len(s)):
	ls = s[:-i-1]
	rs = s[i:]

	lsPal = ""
	for lsi in xrange(len(ls)):
		if ls[lsi] == ls[-lsi - 1]:
			lsPal += ls[lsi]
		else:
			lsPal = ""
		if len(longestStr) < len(lsPal):
			longestStr = lsPal
	rsPal = ""
	for rsi in xrange(len(rs)):
		if rs[rsi] == rs[-rsi - 1]:
			rsPal += rs[rsi]
		else:
			rsPal = ""
		if len(longestStr) < len(rsPal):
			longestStr = rsPal

print longestStr


