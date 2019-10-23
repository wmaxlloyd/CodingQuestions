# Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details.

# Consider the following dictionary
# { i, like, sam, sung, samsung, mobile, ice,
#   cream, icecream, man, go, mango}

# Input:  ilike
# Output: Yes
# The string can be segmented as "i like".

# Input:  ilikesamsung
# Output: Yes
# The string can be segmented as "i like samsung" or "i like sam sung".

wordDict = ["i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"]

inputString = "ilikemangosamsungicecream"

def findSentenceInString(remainingInputString):
    print(remainingInputString)
    allSentences = []
    for word in wordDict:
        if remainingInputString.startswith(word):
            if remainingInputString == word:
                allSentences.append(word)
            else:
                allRemainingSentences = findSentenceInString(remainingInputString[len(word):])
                for sentence in allRemainingSentences:
                    allSentences.append(f"{word} {sentence}")
    return allSentences

print(findSentenceInString(inputString))