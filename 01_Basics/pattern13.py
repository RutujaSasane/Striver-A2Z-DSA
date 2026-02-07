# Pattern - 13: Increasing Number Triangle Pattern

class pattern13:
    def roots(self, n):
        current = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(current, end="")
                current += 1
            print()
            
if __name__ == "__main__":
    p = pattern13()
    n = 5
    p.roots(n)
        
# Time Complexity: O(N²)
# Space Complexity: O(1)