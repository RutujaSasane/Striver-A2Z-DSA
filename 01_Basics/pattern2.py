# Pattern-2: Right-Angled Triangle Pattern

class pattern2:
    def roots(self, n):
        for i in range(1, n+1):
            print("*" * i)

if __name__ == "__main__":
    p = pattern2()
    n = 3
    p.roots(n)

# Time Complexity: O(N²)
# Space Complexity: O(N)