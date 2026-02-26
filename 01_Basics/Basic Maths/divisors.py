# Print all Divisors of a given Number

class problem:
    def roots(self, n):
        divisors = []
        
        for i in range (1, n+1):
            if n%i == 0:
                divisors.append(i)
            else:
                pass
        
        print(f"The divisors of {n} are {divisors}")
        
if __name__ == "__main__":
    p = problem()
    m = int(input("Enter a number to print all its divisors:"))
    p.roots(m)