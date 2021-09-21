def main():

    #Line comments are always red
    ''' Triple quotation is
for multi-line or
block comments'''

    #some funny names

    student1 = "Alfred"
    student2 = "GRunto"
    
    print(student1)
    print(student2)
    
    #string concatenation (combines two strings together)
    print("Two students are " + student1 + " and " + student2)

    numPlants = 112

    print("I have " + str(numPlants) + " plants")

    numPlants = numPlants + 1

    print("I now have " + str(numPlants) + " plants")

    awFounded = "1884"
    curDate = 2021

    print("Years since Annie Wright was founded:")
    print(curDate - int(awFounded))

    #experiment with strings to integers
    #print(("a"))
    #print(str(curDate) - awFounded)

    print(type(curDate))

    date = "Tuesday"

    classToday = True
    if date == "Wednesday":
        classToday = False

    print(classToday)
    print(type(classToday))

    #float vs. integers

    x = 3.5
    print(int(x))
    y = -2
    z = 15.0
    print(z)
    z = 15.000000
    print(z)
    w = y * z
    
    print(type(x))
    print(type(y))
    print(type(z))
    print(type(w))

if __name__ == "__main__":
    main()
