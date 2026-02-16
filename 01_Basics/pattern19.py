# Pattern-19: Symmetric-Void Pattern

class pattern19:
    def roots(self, n):
        spaces = 0
        for i in range(n):
            print("*"*(n-i), end="")
            print(" "*spaces, end="")
            print("*"*(n-i), end="")
            spaces += 2
            print()
        
        spaces = 2 * n - 2
        for i in range(1,n+1):
            print("*"*i, end="")
            print(" "*spaces, end="")
            print("*"*i, end="")
            spaces -= 2
            print()

if __name__ == "__main__":
    p = pattern19()
    n = 5
    p.roots(n)

# Time Complexity: O(N²)
# Space Complexity: O(1)
        
    
