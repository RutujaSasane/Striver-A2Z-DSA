# Pattern-5: Inverted Right Pyramid
class pattern5:
    def roots(self, n):
        while n > 0:
            print("*" * n)
            n -= 1
        print()
        
if __name__ == "__main__":
    p = pattern5()
    n = 5
    p.roots(n)

# Time Complexity: O(N²)
# Space Complexity: O(1)