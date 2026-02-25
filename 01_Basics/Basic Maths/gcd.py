# GCD of two numbers

class problem:
    def roots(self, m1, m2):
        m1_divisors = []
        m2_divisors = []
        
        for i in range(1, m1+1):
            if m1%i == 0:
                m1_divisors.append(i)
            else:
                pass
        
        print(f"Divisors of {n1} are {m1_divisors}")
        
        for j in range(1, m2+1):
            if m2%j == 0:
                m2_divisors.append(j)
            else:
                pass
        print(f"Divisors of {n2} are {m2_divisors}")
        
        ##stuck further
        common_divisors = []
        
        for x in m1_divisors:
            if x in m2_divisors:
                common_divisors.append(x)
                
        print(f"Common Divisors: {common_divisors}")
        print(f"GCD of {n1} and {n2} is {max(common_divisors)}")
        
        
if __name__ == "__main__":
    p = problem()
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    p.roots(n1, n2)