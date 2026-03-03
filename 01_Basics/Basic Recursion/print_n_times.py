# Print Name N times using Recursion

class problem:
    def roots(self, name, count, N):
        if count == N:
            return
        print(name)
        
        self.roots(name, count+1, N)
        
        
if __name__ == "__main__":
    p = problem()
    N = 5
    name = "Rutuja"
    
    p.roots(name, 0, N)

# Time Complexity: O(N)
# Space Complexity: O(N)