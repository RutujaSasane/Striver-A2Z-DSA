# recursion approach
class problem:
    def reverse(self, arr, left, right):
        if left >= right:
            return
    
        arr[left], arr[right] = arr[right], arr[left]
        self.reverse(arr, left + 1, right - 1)
    
if __name__ == "__main__":
    p = problem()
    arr = list(map(int, input("Enter elements:").split()))
    p.reverse(arr, 0, len(arr)-1)
    print(*arr)

# Time Complexity: O(N)
# Space Complexity: O(N)