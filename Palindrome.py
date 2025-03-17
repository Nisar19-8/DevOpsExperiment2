#Palindrome Number
def is_palindrome(num):
    # Convert the number to string to easily reverse it
    str_num = str(num)
    
    # Check if the number is the same forwards and backwards
    if str_num == str_num[::-1]:
        return True
    else:
        return False

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(num):
    print("{num} is a palindrome number.")
else:
    print("{num} is not a palindrome number.")

