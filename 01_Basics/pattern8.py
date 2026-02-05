# Pattern - 8: Inverted Star Pyramid

class pattern8:
    def roots(self, n):
        for i in range(n):
            for j in range(i):
                print(" ", end="")
            
            for j in range(2 * n - (2 * i + 1)):
                print("*", end="")
            
            for j in range(i):
                print(" ", end="")
            
            print()
        
if __name__ == "__main__":
    p = pattern8()
    n = 5
    p.roots(n)


# Time Complexity: O(N²)
# Space Complexity: O(1)