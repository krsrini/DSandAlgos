def k_most_frequent(k, words):
    """
    Args:
     k(int32)
     words(list_str)
    Returns:
     list_str
    """
    # Write your code here.
    if not words:
        return []
        
    word_count = {}

    for word in words:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += 1

    sort_by_freq = sorted(word_count.items(), key= lambda item:(-item[1], item[0]) )
    print(sort_by_freq)
    return ([pair[0] for pair in sort_by_freq[:k]])


words = ["car", "bus", "taxi", "car", "driver", "candy", "race", "car", "driver", "fare", "taxi"]
k = 4

print(k_most_frequent(k, words))
