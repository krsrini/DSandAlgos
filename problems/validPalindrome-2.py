# 680. Valid Palindrome II
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

'''
Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
'''

def checkPalindromeSubset(s, i, j):
    while i < j :
        if s[i] != s[j]:
            return False
        i += 1
        j += 1
    return True

def validPalindrome(s):
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return checkPalindromeSubset(s, i+1, j) or  checkPalindromeSubset(s, i, j - 1)
        i += 1
        j -= 1
    return True

s = "abc"
print(validPalindrome(s))