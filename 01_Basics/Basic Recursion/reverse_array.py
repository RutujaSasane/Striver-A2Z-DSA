# Reverse a given Array

class problem:
    def roots(self, arr):
        p1 = 0
        p2 = len(arr)-1
        
        while p1 < p2:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1 += 1
            p2 -= 1
        
if __name__ == "__main__":
    p = problem()
    arr = list(map(int, input("Enter elements:").split()))
    p.roots(arr)
    print(" ".join(map(str, arr)))
    
# Time Complexity: O(N)
# Space Complexity: O(1)