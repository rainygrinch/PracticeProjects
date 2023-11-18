# given a string, return a string where every char in the original
# string is doubled

def double_char(str):
    to_return = ""
    for char in str:
        to_return += char*2

    print(to_return)

double_char("ABC")
