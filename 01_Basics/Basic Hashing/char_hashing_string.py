# when the string contains uppercase and lowercase letters
s = "HelloWorld"

# create hash array for ASCII characters
hash_arr = [0] * 256

# pre-storing
for ch in s:
    hash_arr[ord(ch)] += 1

# queries
queries = ['H', 'l', 'o', 'W', 'z']

# fetching
for q in queries:
    print(q, "appears", hash_arr[ord(q)], "times in the string.")