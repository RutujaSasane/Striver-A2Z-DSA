# Pattern - 17: Alpha-Hill Pattern
class pattern17:
    def roots(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end="")

            ch = ord('A')
            breakpoint = (2 * i + 1) // 2

            for j in range(1, 2 * i + 2):
                print(chr(ch), end="")
                if j <= breakpoint:
                    ch += 1
                else:
                    ch -= 1
            
            print()

if __name__ == "__main__":
    p = pattern17()
    n = 5
    p.roots(n)

# Time Complexity: O(N²)
# Space Complexity: O(1)