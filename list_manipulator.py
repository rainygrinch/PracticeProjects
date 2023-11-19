# Add 10 to the end of the list
# Remove the first occurrence of 5
# Double each element in the list

def modify_list(input_list):
    input_list.append(10)

    if 5 in input_list:
        input_list.remove(5)

    for i in range(len(input_list)):
        input_list[i] *=2


# Main program
initial_list = [2, 5, 8, 3, 5, 7]
print(f"Original List: {initial_list}")
# Use the modify_list function
modify_list(initial_list)

# Print the results
print(f"Updated List: {initial_list}")
