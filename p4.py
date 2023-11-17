def reverse_string(s):
    # Base case: If the string is empty or has only one character, return the string itself
    if len(s) <= 1:
        return s
    
    # Recursive case: Reverse the substring excluding the first and last characters,
    # and concatenate the first character at the end
    return s[-1] + reverse_string(s[1:-1]) + s[0]

# Get input from the user
input_string = input("Enter a string: ")

# Call the reverse_string function and display the result
reversed_string = reverse_string(input_string)
#print("Original String:", input_string)
print("Reversed String:", reversed_string)

