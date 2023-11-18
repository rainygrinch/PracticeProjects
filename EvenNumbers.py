# right a program that will print the even numbers between
# 1 and 10, and then print how many occurances of even numbers there are

def main():
    count = 0
    for n in range (1, 10):
        if n % 2 == 0:
            count +=1
            print(n)
    print(f"There are {count} even numbers")

main()