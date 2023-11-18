def reverse_and_capitalise(input_string):
    txt = input_string[::-1]
    output = txt.upper()
    return output


# Main program
user_input = input("Enter a string: ")

# Use the reverse_and_capitalise function
result = reverse_and_capitalise(user_input)

# Print the results
print(f"Original String: {user_input}")
print(f"Reversed String: {result}")
