def productOfThree(x, y, z):
    return x * y * z

def favHolidays():

    return "Halloween", "Leap-Day"


# the variables inside the parantheses are called 'parameters'
# we can have multiple parameters, separated by a comma
def sum3(x):
    return x + 3

def main():

    print("Hello class")

    #both ways of accepting output can be printed
    print(sum3(2))
    result = sum3(8)
    print(result)

    print(favHolidays())

    print(productOfThree(5.5, 3, -9))

    favNum = input("Write your favorite number")
    print(2*favNum)
    



if __name__ == "__main__":
    main()
