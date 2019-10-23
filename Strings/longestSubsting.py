# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
# Assumptions:
# - All lowercase
# - No special characters (don't need to do character validation)
#
# Time Complexity: O(n^2)
# Space Complexity: O(1)

s = "asddsasaa"

print "O(n^2) Time"
p1=0
p2=1
maxLength = 0

while p2 < len(s) + 1:
	substring = s[p1:p2]
	if len(substring) == len(set(substring)):
		p2 += 1
		maxLength = max(maxLength, len(substring))
	else:
		p1 += 1
print maxLength

# Time Complexity: O(n) ???
#
print "O(n) time"
p1 = 0
p2 = 0
substringHash = {}
for c in set(s):
	substringHash[c] = 0
maxLength = 0
while p2 < len(s):
	if substringHash[s[p2]] > 0:
		substringHash[s[p1]] -= 1
		p1 += 1
	else:
		substringHash[s[p2]] += 1
		maxLength = max(maxLength, p2 - p1 + 1)
		p2 += 1
print maxLength

