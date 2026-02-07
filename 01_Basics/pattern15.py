# Pattern-15: Reverse Letter Triangle Pattern

class pattern15:
    def roots(self, n):
        for i in range(n, 0, -1):
            for j in range(i):
                print(chr(65+j), end="")
            print()

if __name__ == "__main__":
    p = pattern15()
    n = 5
    p.roots(n)
            
# Time Complexity: O(N²)
# Space Complexity: O(1)