# Check if a number is prime or not

class problem:
    def roots(self, n):
        factors = 0
        
        for i in range(1, n+1):
            if n%i == 0:
                factors += 1
            else:
                pass
    
        if factors == 2:
            print("It is a prime number.")
        else:
            print("It is a composite number.")
        
if __name__ == "__main__":
    p = problem()
    m = int(input("Check if a number is prime or not:"))
    p.roots(m)