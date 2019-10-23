# Giving a dictionary and a string ‘str’, your task is to find the longest string in dictionary of size x which can be formed by deleting some characters of the given ‘str’.

# Examples:

# Input : dict = {"ale", "apple", "monkey", "plea"}   
#         str = "abpcplea"  
# Output : apple

# Input  : dict = {"pintu", "geeksfor", "geeksgeeks", 
#                                         " forgeek"} 
#          str = "geeksforgeeks"
# Output : geeksgeeks

wordDict = ["ale", "apple", "monkey", "plea"]
inputString = "abpmploenakesksjrlkysew"
longestWord = ""

def canBeMadeFrom(fullString, substring):
    for char in fullString:
        if char == substring[0]:
            substring = substring[1:]
            if not len(substring):
                return True
    return False

for word in wordDict:
    if len(word) > len(longestWord) and canBeMadeFrom(inputString, word):
        longestWord = word

print(longestWord)
