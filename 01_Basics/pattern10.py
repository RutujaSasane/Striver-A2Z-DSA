# Pattern - 10: Half Diamond Star Pattern

class pattern10:
    def roots(self, n):
        for i in range(1, 2*n):
            if i < n+1:
                for j in range(i):
                    print("*", end="")
                print()
            if i > n:
                for j in range(2*n-i):
                    print("*", end="")
                print()
                
            
if __name__ == "__main__":
    p = pattern10()
    n = 3
    p.roots(n)

# Time Complexity: O(N²)
# Space Complexity: O(1)