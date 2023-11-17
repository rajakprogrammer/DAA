#Write a short recursive Python function that determines if a string s is a palindrome. For example, racecar and gohangasalamiimalasagnahog are palindromes

def is_palindrome(s):
    # Base case: If the string is empty or has only one character, it's a palindrome
    if len(s) <= 1:
        return True
    
    # Check if the first and last characters are the same
    if s[0] == s[-1]:
        # If they are the same, check the substring without the first and last characters
        return is_palindrome(s[1:-1])
    else:
        # If the first and last characters are different, it's not a palindrome
        return False

# Get input from the user
input_string = input("Enter a string: ")

# Call the is_palindrome function and display the result
if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
