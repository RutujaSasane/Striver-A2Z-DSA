# Pattern-14: Increasing Letter Triangle Pattern

class pattern14:
    def roots(self, n):
        for i in range(n):
            for j in range(i+1):
                print(chr(65 + j), end="")
            print()
            
if __name__ == "__main__":
    p = pattern14()
    n = 5
    p.roots(n)

# Time Complexity: O(N²)
# Space Complexity: O(1)