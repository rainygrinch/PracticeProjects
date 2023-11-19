# Create and return a new list containing only the even numbers

def filter_odd_numbers(input_list):
    even_num = []
    for i in input_list:
        if i % 2 == 0:
            even_num.append(i)
    return even_num
# Main program
initial_list = [1, 5, 8, 3, 10, 7, 12]

print(f"Original List: {initial_list}")

# Use the filter_odd_numbers function
filtered_list = filter_odd_numbers(initial_list)

# Print the results

print(f"Filtered List (Even Numbers Only): {filtered_list}")
