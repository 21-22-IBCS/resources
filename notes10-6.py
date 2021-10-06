def main():

    school = "Annie Wright"
    print(school)

    #individual characters can be indexed
    print(school[3])
    print(school[10])

    #substrings can be indexed as well
    '''print(school[3:8])
    print(school[:5])
    print(school[7:])
    print(school[-6])'''

    print("\n\n")

    #loop through a string to iterate through its characters
    for i in range(10):
        print(school[-i - 1])

    weather = "Rain"
    
    for i in range(len(weather)):
        print(2**i)

    if weather[0] == 'R':
        print("Oh no!")
    else:
        print("It is sunny, yay!")


if __name__ == "__main__":
    main()
