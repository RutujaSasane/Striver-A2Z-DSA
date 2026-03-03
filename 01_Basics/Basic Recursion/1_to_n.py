# Print 1 to N using Recursion

class problem:
    def roots(self, count, N):
        if count > N:
            return
        print(count)
        
        self.roots(count+1, N)
        
        
if __name__ == "__main__":
    p = problem()
    N = 5
    
    p.roots(1, N)
    
