#Leet code 1768. Merge Strings Alternately
def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
        
    i = j = 0 
    result = ""
    while i < len(word1) and j < len(word2):
        result += word1[i]
        i += 1
        result += word2[j]
        j += 1

    if i < len(word1):
        result += word1[i:]
    
    if j < len(word2):
        result += word2[j:]

    return result


word1 = "ab"
word2 = "pqrs"

print(mergeAlternately(word1, word2))