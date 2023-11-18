# given an array of ints,return true if 6 appears as either the first
# or last numbers

list_a = [3, 6, 4, 7, 6]
list_b = [6, 6, 4, 7, 0]
list_c = [3, 6, 4, 7, 4]
list_d = [3, 6, 4, 7, 2]

def first_last(list):
    for num in list:
        if list[0] == 6 or list[-1] == 6:
            return True
        else:
            return False

first_last(list_a)
first_last(list_b)
first_last(list_c)
first_last(list_d)

