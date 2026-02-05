# Pattern - 11: Binary Number Triangle Pattern

class pattern11:
    def roots(self, n):
        for i in range(n):
            if i%2 == 0:
                start = 1
            else:
                start = 0
                
            for j in range(i+1):
                print(start, end="")
                start = 1 - start
            print()    
            
if __name__ == "__main__":
    p = pattern11()
    n = 5
    p.roots(n)          
                
# Time Complexity: O(N²)
# Space Complexity: O(1)