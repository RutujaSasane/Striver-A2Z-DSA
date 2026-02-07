# Pattern - 12: Number Crown Pattern

class pattern12:
    def roots(self, n):
        spaces = 2 * (n-1)
        
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end="")
            for j in range(1, spaces+1):
                print(" ", end="")
            for j in range(i, 0, -1):
                print(j, end="")
            print()
            spaces -= 2
            
if __name__ == "__main__":
    p = pattern12()
    n = 5
    p.roots(n)

# Time Complexity: O(N²)
# Space Complexity: O(1)