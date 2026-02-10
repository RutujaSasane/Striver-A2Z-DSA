# Pattern-18: Alpha-Triangle Pattern

class pattern18:
    def roots(self, n):
        for i in range(n):

            start = ord('A') + n - 1 - i
            end = ord('A') + n 

            for ch in range(start, end):
                print(chr(ch), end="")

            print()

if __name__ == "__main__":
    p = pattern18()
    n = 5
    p.roots(n)

# Time Complexity: O(N²)
# Space Complexity: O(1)