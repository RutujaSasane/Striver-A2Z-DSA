# Pattern - 22: The Number Pattern
class pattern22:
    def roots(self, n):
        for i in range(2*n - 1):
            for j in range(2*n - 1):
                top = i
                left = j
                bottom = (2*n - 2) - i
                right = (2*n - 2) - j
                
                minDist = min(top, left, bottom, right)
                
                print(n-minDist, end="")
            print()
            
if __name__ == "__main__":
    p = pattern22()
    n = 5
    p.roots(n)
    
# Time Complexity: O(N²)
# Space Complexity: O(1)