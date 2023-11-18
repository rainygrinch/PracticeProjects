# return the number of even ints in a given array

def count_evens(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(f"There are {count} even numbers in this list")


list_a = [1, 4, 5, 7, 8, 4, 5, 7, 23, 26, 23, 25, 24]

count_evens(list_a)