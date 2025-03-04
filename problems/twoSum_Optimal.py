def twoSumHashing(num_arr, pair_sum):
    sum=[]
    hashmap = {}
    for i in range(len(num_arr)):
        hashmap[num_arr[i]] = 1
    for i in range(len(num_arr)):
        compliment = pair_sum - num_arr[i]
        if (compliment in hashmap):
            return [i, hashmap[compliment]]

# Driver Code
num_arr = [4, 5, 1, 8]
pair_sum = 9
  
# Calling function
print(twoSumHashing(num_arr, pair_sum))