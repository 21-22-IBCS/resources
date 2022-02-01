def main():

    #String methods
    word = "Fergie"
    other = str(20)
    print(word)
    print(other)

    #concatenate strings push them together
    combine = word + other
    print(combine)
    print(combine*5)
    print(combine.upper())
    print(word.upper())

    #split() string method which separates your string into multiple strings
    #based on a 'separator' substring as input. The result is a list. Removes separator

    sof = "I hate brussel sprouts"
    words = sof.split("br")
    print(words)

    #strip() string method removes specific characters from the beginning and ending
    #of a string

    nad = "The tree is tall."
    print(nad)
    fixed = nad.replace("e","")
    print(fixed)
    #justIce = nad.strip("")
    #print(justIce)

    #using files in python
    f = open("odyssey.txt", "r")
    
    #read() returns the string of the entire file
    wholeText = f.read()

    #readline() returns one line at a time
    '''for i in range(40):
        print(f.readline())'''

    listOdyssey = wholeText.split(" ")
    ind = listOdyssey.index("and\nmost")
    print(ind)
    print(listOdyssey[21])
    newList = []
    for i in range(50):
        tempList = listOdyssey[i].split("\n")
        for e in tempList:
            newList.append(e)

    print(newList)    
        



    

if __name__ == "__main__":
    main()
