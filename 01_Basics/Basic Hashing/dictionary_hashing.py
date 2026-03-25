# Dictionary uses less memory than array hashing as it 
# only stores the unique elements and their frequencies, 
# while array hashing may require a large array to accommodate all possible values, 
# leading to wasted space if the range of values is large and sparse.

arr = [1,2,3,1,3,2,12]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) +1

print(freq)

print("Handling Queries")

queries = [1,2,12,5]

for q in queries:
    print(q, "appears", freq.get(q, 0), "times")