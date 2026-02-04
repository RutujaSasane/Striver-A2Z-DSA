# Pattern - 3: Right-Angled Number Pyramid

class pattern3:
    def roots(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end= " ")
            print()
        
if __name__ == "__main__":
    p = pattern3()
    n = 5
    p.roots(n)

# Time Complexity: O(N²)
# Space Complexity: O(1)