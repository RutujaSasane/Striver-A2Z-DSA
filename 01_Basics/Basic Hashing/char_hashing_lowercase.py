# when the string contains only lowercase letters
s = "abcdabefc"

hash_arr = [0]*26   

# Pre-storing
for ch in s:
    index = ord(ch) - ord('a')
    hash_arr[index] += 1

queries = ['a', 'c', 'z']

# Fetching
for q in queries:
    index = ord(q) - ord('a')
    print(hash_arr[index])
