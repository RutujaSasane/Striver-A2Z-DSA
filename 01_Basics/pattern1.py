#pattern1: The task is to print a square pattern of stars.
class pattern1:
    def roots(self, n):
        for i in range(0, n):
            for j in range(0, n):
                print("*", end= " ")
            print(" ")
        
if __name__ == "__main__":
    p = pattern1()
    n = 10
    p.roots(n)

# Time Complexity: O(N²)
# Space Complexity: O(1)