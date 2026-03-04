# Sum of first N Natural Numbers

class problem:
    def roots(self, N):
        if N == 1:
            return 1
        return N + self.roots(N - 1)
        
if __name__ == "__main__":
    p = problem()
    N = int(input("Enter an integer:"))
    print(f"The sum of {N} natural numbers is {p.roots(N)}")
    
# Time Complexity: O(N)
# Space Complexity: O(N)