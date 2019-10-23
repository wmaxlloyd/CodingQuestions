# Given two strings s and t, write a function to determine if t is an anagram of s.

# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.

# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
#

s = "anagram"
t = "nagrama"

print "sorting"

print True if sorted(s) == sorted(t) else False

print "Using a hash map"

sHash = {}
tHash = {}
anagram = True if len(s) == len(t) else False
if anagram:
	for i in xrange(len(s)):
		if s[i] not in sHash:
			sHash[s[i]] = 1
		else:
			sHash[s[i]] += 1

		if t[i] not in tHash:
			tHash[t[i]] = 1
		else:
			tHash[t[i]] += 1

for key in sHash:
	try:
		if sHash[key] != tHash[key]:
			anagram = False
			break
	except:
		anagram = False
		break
print anagram

print "For all Unicode"
anagram = True if len(s) == len(t) else False

sHash = {}
tHash = {}
print sHash, tHash
if anagram:
	for i in xrange(len(s)):
		sUniKey = ord(s[i])
		tUniKey = ord(t[i])
		if sUniKey in sHash:
			sHash[sUniKey] += 1
		else:
			sHash[sUniKey] = 1
		if tUniKey in tHash:
			tHash[tUniKey] += 1
		else:
			tHash[tUniKey] = 1
	print sHash, tHash
	for key in sHash:
		try:
			if sHash[key] != tHash[key]:
				anagram = False
				break
		except:
			anagram = False
			break
print anagram

