def radix_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    max_arr = max(arr)
    place = 1
    while max_arr // place > 0:
        #counting_sort(arr, place)
        print(place)
        place *= 10

arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(arr))
