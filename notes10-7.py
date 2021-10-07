def main():

    #Strings can have their characters and substrings accessed by their indexes
    cFood = "strawberry"
    print(cFood[3])
    print(cFood[8])
    print(cFood[5])
    print(cFood[-4])

    #substring from index 3 to 7
    print(cFood[3:7])
    print(cFood[:5])
    print(cFood[2:])
    print(len(cFood))

    #for loop is a data structure for repeating a section of code
    # i is an iterator. It defaults starting at 0 and increasing by 1 each repetition
    for i in range(len(cFood)):
        if cFood[2*i] == "a":
            print("charles like fish")
        else:
            print(cFood[-1-i])


if __name__ == "__main__":
    main()
