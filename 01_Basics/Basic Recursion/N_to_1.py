# Print N to 1 using Recursion

class problem:
    def roots(self, current):
        if current < 1:
            return
        print(current)
        
        self.roots(current - 1)
        
        
if __name__ == "__main__":
    p = problem()
    N = 5
    
    p.roots(N)
    
# Time Complexity: O(N)
# Space Complexity: O(N)
