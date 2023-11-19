def count_vowels(input_string):
    vowel_count = 0
    for char in input_string:
        if char.lower() in ["a", "e", "i", "o", "u"]:
            vowel_count +=1
    return vowel_count

def reverse_string(input_string):
    txt = input_string[::-1]
    return txt

# Main program
user_input = input("Enter a string: ")

# Use the count_vowels function
vowel_count = count_vowels(user_input)

# Use the reverse_string function
reversed_input = reverse_string(user_input)

# Print the results
print(f"Original String: {user_input}")
print(f"Vowel Count: {vowel_count}")
print(f"Reversed String: {reversed_input}")
