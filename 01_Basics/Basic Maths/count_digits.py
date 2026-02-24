# Count digits in a Number

class problem:
    def roots(self, n):
        count = 0
        while n > 0:
            count += 1
            n = n // 10
        
        print(f"No. of digits {m} has is {count} digits")

if __name__ == "__main__":
    p = problem()
    m = int(input("Enter a number: "))
    p.roots(m)
