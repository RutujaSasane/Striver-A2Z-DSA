# Reverse Digits of A Number

class problem:
    def roots(self, m):
        reversed = 0
        while m > 0:
            last_digits = m % 10
            reversed = reversed * 10 + last_digits
            m = m // 10
        
        print(f"The reverse of {n} is {reversed}")
        
        
if __name__ == "__main__":
    p = problem()
    n = int(input("Enter a number to reverse it: "))
    p.roots(n)