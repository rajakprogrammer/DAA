#Write a recursive function to convert the entered string of digits into the integer it represents. For example, 13531 represents the integer 13,531.

def string_to_integer(input_string):
    # Base case: If the string is empty, return 0
    if len(input_string) == 0:
        return 0
    
    # Convert the first character to an integer
    first_digit = int(input_string[0])
    
    # Recursive case: Convert the rest of the string and add the first digit
    remaining_string = input_string[1:]
    result = first_digit * (10 ** len(remaining_string)) + string_to_integer(remaining_string)
    
    return result

# Get input from the user
input_string = input("Enter a string of digits: ")

# Check if the input is valid (contains only digits)
if input_string.isdigit():
    result = string_to_integer(input_string)
    formatted_result = f"{result:,}"  # Format the result with commas
    print(f"The integer representation of '{input_string}' is: {formatted_result}")
else:
    print("Invalid input. Please enter a string of digits.")


