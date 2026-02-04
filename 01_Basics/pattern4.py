# Pattern - 4: Right-Angled Number Pyramid - II
class pattern4:
    def roots(self, n):
        for i in range(1, n+1):
            for j in range(1, i):
                print(i, end=" ")
            print()

if __name__ == "__main__":
    p = pattern4()
    n = 5
    p.roots(n)

# Time Complexity: O(N²)

# Space Complexity: O(1)
