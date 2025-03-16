"""
Asymptotic complexity in terms of `n`:
* Time: O(log(n)).
* Auxiliary space: O(1).
* Total space: O(1).
"""

def count_all_subsets(n):
    subsetCount = 1
    multiplier = 2

    while n > 0:

        if n % 2 == 1:
            subsetCount *= multiplier

        n //=2
        multiplier *= multiplier

    return subsetCount

print(count_all_subsets(n))