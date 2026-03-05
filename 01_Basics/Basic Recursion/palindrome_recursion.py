# String is Palindrome or not using Recursion

class problem:
    def roots(self, string, left, right):
        if left >= right:
            return True
        
        if string[left] != string[right]:
            return False
            
        return self.roots(string, left+1, right-1)

if __name__ == "__main__":
    p = problem()
    string = input("Enter a string to check whether it is palindrome or not:")
    result = p.roots(string, 0, len(string) - 1)
    print(result)
    
# Time Complexity: O(N)
# Space Complexity: O(N)