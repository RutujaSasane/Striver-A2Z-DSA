# Pattern - 16: Alpha-Ramp Pattern
class pattern16:
    def roots(self, n):
        for i in range(n):
            ch = chr(65 + i)

            for j in range(i+1):
                print(ch, end="")

            print()

if __name__ == "__main__":
    p = pattern16()
    n = 5
    p.roots(n)

# Time Complexity: O(N²)
# Space Complexity: O(1)