'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

Example 4:
    Input: s = "([])"
    Output: true

Time complexity : O(n)
Space complexity : O(n)
'''

def validParen(s):
    mapParen = {"(": ")", "[" : "]", "{" : "}"}
    stack = []
    if len(s) % 2 == 1:
        return False

    for char in s:
        if char in mapParen:
            #print(char, mapParen[char])
            stack.append(mapParen[char])
        else:
            if not stack:
                return False
            popped = stack.pop()
            if popped != char:
                return False
    return not stack
#s = "()[]{"
s = "(]"
print(validParen(s))