# Check if a number is Armstrong Number or not

class problem:
    def roots(self, n):
        sum_num = 0
        length = len(str(n))
        # print(length)
        while n > 0:
            sum_num = sum_num + (n % 10)**length
            n = n // 10
        
        if sum_num == m:
            print("yes, it is Armstrong.")
        else:
            print("no, it is not.")
        
        
if __name__ == "__main__":
    p = problem()
    m = int(input("Enter a number to check if it is Armstrong or not: "))
    p.roots(m)