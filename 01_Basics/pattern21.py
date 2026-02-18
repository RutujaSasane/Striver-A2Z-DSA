# Pattern - 21: Hollow Rectangle Pattern
class pattern21:
    def roots(self, n):
        for i in range(n):
            for j in range(n):
                if i == 0 or j == 0 or i == n - 1 or j == n - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

if __name__ == "__main__":
    p = pattern21()
    n = 4
    p.roots(n)

# Time Complexity: O(N²)
# Space Complexity: O(1)