# Pattern - 7: Star Pyramid

class pattern7:
    def roots(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end="")
            
            for j in range(2*i+1):
                print("*", end="")
            
            for j in range(n-i-1):
                print(" ", end="")
            print()
        
if __name__ == "__main__":
    p = pattern7()
    n = 5
    p.roots(n)

# Time Complexity: O(N²)
# Space Complexity: O(1)