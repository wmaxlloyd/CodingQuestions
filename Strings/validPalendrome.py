# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome.
#

print "Using Hashmap"

s = "A man, a plan, a canal: Panama"

stripped = ""
for c in s:
	if c.isalpha():
		stripped += c.lower()

palindrome = True
for i in xrange(len(stripped)//2):
	if stripped[i] != stripped[-i - 1]:
		palindrome = False
		break

print palindrome