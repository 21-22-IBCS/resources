def main():

    '''
    #LISTS
    aList = ["fruits", "vegetables", "butter"]
    print(aList)
    #add things to lists
    aList.append("bread")
    aList.append(5.5)
    print(aList)
    #lists can be made up of other lists
    aList.append(["candy", "cereal", "fish"])
    print(aList)
    #create a list with the list function'''
    bList = list(("Lady Gaga", "Adam Sandler", "Fergie"))
    print(bList)
    #remove items from a list
    bList.remove("Fergie")
    print(bList)
    
    cList = list(("Obama", 10, -3.12, True))
    print(cList)

    #indexing items in a list.
    bList.append("Steph Curry")
    bList.append("Ms. Corrigan")
    bList.append("Woody")
    bList.append("Grunto")
    print(bList)
    #the 2 index is the third element in the list
    print(bList[2])
    #the -1 index is the last element in the list
    print(bList[-1])
    #sublists are created with an index : index to see the start and stop
    print(bList[1:3])
    print(bList[:5])
    print(bList[4:])

    #use lists in loops
    for celeb in bList:
        print(celeb)

    for i in range(len(bList)):
        print(bList[i])

    #set items in a list to another value
    bList[1] = "Sofiia"
    print(bList)







if __name__ == "__main__":
    main()
