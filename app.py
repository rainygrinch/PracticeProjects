print("Hello, welcome to this program that doesn't fucking work")

# Value to increase by
diff = 1
#value to reduce by
reduction = 15
global x
x = 1

# function to change the value by increasing by diff variable, or if it reaches 10, to subtract reduction variable
def valueChange():

    while x < 10:
        print ("The Value of X is currently: " + str(x))
        x += diff
    else:
        print ("The Value of X is above 10, specifically it is: " + str(x))
        x -= reduction
        print("X has been reduced by: " + str(reduction) + ", The Value of X is currently: " + str(x))


# function to ask user to continue loop, stop loop, or provide error
def decide():
    cont = (input("Do you wish to run the loop again, type Y or N: "))
    if cont == "Y" or "y":
        (valueChange())
    elif cont == "N" or "n":
        print("You have stopped the process")
    else:
        print("Invalid Response, please input again")
        decide()

valueChange()
decide()