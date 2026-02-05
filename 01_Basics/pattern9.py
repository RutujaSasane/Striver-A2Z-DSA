# Pattern - 9: Diamond Star Pattern

class pattern9:
    def roots(self, n):
        for i in range(n):         # erect pyramid - pattern7
            for j in range(n-i-1):
                print(" ", end="")
            for j in range(2*i+1):
                print("*", end="")
            for j in range(n-i-1):
                print(" ", end="")
            print()
        for i in range(n):         # inverted pyramid - pattern8
            for j in range(i):
                print(" ", end="")
            for j in range(2*n-(2*i+1)):
                print("*", end="")
            for j in range(n):
                print(" ", end="")
            print()
            
if __name__ == "__main__":
    p = pattern9()
    n = 20
    p.roots(n)


# Time Complexity: O(N²)
# Space Complexity: O(1)