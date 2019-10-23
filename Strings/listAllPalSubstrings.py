# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
#

s = "abababababcc"

print ("Brute Force")
# Time complexity O(n^4)
# Space complexity O(1)
pals = []
for i in xrange(len(s)):
	for j in xrange(i+1, len(s) + 1):
		sub = s[i:j]
		if sub == sub[::-1]:
			pals.append(sub)
print (pals)

print ("Sneaky")

pals = []
for i in xrange(len(s)):
	c = s[i]
	pals.append(c)
	palLen = 1
	evenPal = ""
	oddPal = c

	while (oddPal or evenPal):
		try:
			if (oddPal) and s[i+palLen] == s[i-palLen]:
				oddPal = s[i+palLen] + oddPal + s[i-palLen]
				pals.append(oddPal)
			else:
				oddPal = False
		except:
			oddPal = False

		try:
			if (evenPal != False) and s[i + palLen] == s[i - palLen + 1]:
				evenPal = s[i + palLen] + evenPal + s[i - palLen + 1]
				pals.append(evenPal)
			else:
				evenPal = False
		except:
			evenPal = False
		palLen += 1


print (pals)

