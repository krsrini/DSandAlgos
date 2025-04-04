'''
20. Valid Parentheses
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