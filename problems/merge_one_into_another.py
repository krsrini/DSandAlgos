def merge_one_into_another(first, second):
    i = len(first)- 1
    j = len(second) - len(first) - 1 
    k = len(second) - 1 
    while i >= 0 and j >= 0:
        if first[i] >  second[j]:
            second[k] = first[i]
            i -= 1
        else:
            second[k] = second[j]
            j -= 1
        k -= 1

    while i >= 0:
        second[k] = first[i]
        i -= 1
        j -= 1

    return second

#first = [1, 3, 5]
#second = [2, 4, 6, 0, 0, 0]

first =  [2]
second =  [1, 0]

print(merge_one_into_another(first,second))