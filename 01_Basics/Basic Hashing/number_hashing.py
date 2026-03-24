arr = [1,2,1,3,2]

hash_arr = [0]*13

# Pre-storing
for num in arr:
    hash_arr[num] += 1

queries = [1,3,4,2,10]

# Fetching
for q in queries:
    print(hash_arr[q])