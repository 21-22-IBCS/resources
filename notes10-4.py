def sleepIn(weekday, vacation):

    if weekday:
        if vacation:
            return True
        return False
    return True

def div2(x):
    return x/2


# this is a newly defined method which takes in "x" as a parameter
def sum3(x):
    # this method outputs our "x" input added with 3
    y = x + 3
    return y

    print("Do we see this")


# this is our main method
def main():

    '''print("Hello from Main")

    numStudents = 3

    result = sum3(numStudents)
    print(result)

    res = div2(10)
    print(res)'''

    #print(sleepIn(True, False))

    #Input Examples

    answer = input("How many plants do you own?")
    print(answer)



    



if __name__ == "__main__":
    main()
