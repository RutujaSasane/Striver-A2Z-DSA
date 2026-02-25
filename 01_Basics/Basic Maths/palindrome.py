# Check if a number is Palindrome or Not

class problem:
    def roots(self, m):
        reversed = 0
        while m > 0:
            last_digits = m % 10
            reversed = reversed * 10 + last_digits
            m = m // 10
        
        if n == reversed:
            print(f"The reverse of {n} is {reversed} and therefore it is a palindrome.")
        else:
            print("No, it is not a palindrome.")
        
        
if __name__ == "__main__":
    p = problem()
    n = int(input("Enter a number: "))
    p.roots(n)