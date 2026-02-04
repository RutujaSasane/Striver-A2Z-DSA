# Pattern - 6: Inverted Numbered Right Pyramid
class pattern6:
    def roots(self, n):
        for i in range(n+1, 0, -1):
            for j in range(1, i):
                print(j, end = " ")
            print()
        
if __name__ == "__main__":
    p = pattern6()
    n = 5
    p.roots(n)

# Time Complexity: O(N²)
# Space Complexity: O(1)