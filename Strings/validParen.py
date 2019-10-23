# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

#Assumptions:
# - s is only made up of "(", "[", "{"
# Time Complexity: O(n)
# Space Complexity: O(1)

s = "([{}()]{[]})"


closedParenMap = {
	")":"(",
	"]":"[",
	"}":"{"
}

openParen = s[0]
valid = True if openParen not in closedParenMap else False
if valid:
	for c in s:
		try:
			if closedParenMap[c] == openParen[-1]:
				openParen = openParen[:-1]
			else:
				valid = False
				break

		except:
			openParen += c


print (valid if not openParen else False)