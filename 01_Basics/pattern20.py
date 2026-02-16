# Pattern - 20: Symmetric-Butterfly Pattern
class pattern20:
    def roots(self, n):
        spaces = n * 2 - 2
        for i in range(1, n+1):
            print("*"*i, end="")
            print(" "*spaces, end="")
            print("*"*i, end="")
            spaces -= 2
            print()
        spaces = 2
        for i in range(n):
            print("*"*(n-i-1), end="")
            print(" "*spaces, end="")
            print("*"*(n-i-1), end="")
            spaces += 2
            print()
            
if __name__ == "__main__":
    p = pattern20()
    n = 5
    p.roots(n)
            
# Time Complexity: O(N²)
# Space Complexity: O(1)