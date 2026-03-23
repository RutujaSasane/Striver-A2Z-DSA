class problem:
    def fibonacci(self, n):
        if n <= 1:
            return n

        last = self.fibonacci(n - 1)
        second_last = self.fibonacci(n - 2)

        return last + second_last
    
if __name__ == "__main__":
    p = problem()
    n = int(input("Enter the number of terms in Fibonacci sequence: "))
    for i in range(n):
        print(p.fibonacci(i), end=" ")

# Time Complexity: O(2^N)
# Space Complexity: O(N) 