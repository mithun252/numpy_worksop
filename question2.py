def is_palindrome(number):
  
    numstr = str(number)
    
    
    return numstr == numstr[::-1]


number = 12321
if ispalindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
