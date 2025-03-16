"""
Asymptotic complexity in terms of input integer `n`:
* Time: O(n).
* Auxiliary space: O(1).
* Total space: O(1).
"""

def find_fibonacci(n):
    if n == 0:
        return 0
    
    superPrevious = 0
    previous = 1

    for i in range(2, n+1):
        current = superPrevious + previous
        superPrevious = previous
        previous = current
    
    return previous

n = 10
print(find_fibonacci(n))