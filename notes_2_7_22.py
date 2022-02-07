def main():


    #Get user input

    response = input("Type an amount of money")
    print(response)

    #define / create a dictionary
    d = {
        "hat" : 15,
        "gloves" : 25,
        "fruit" : 4,
        "cat" : 70,
        "bag" : True
        }

    print(d)
    print(d["hat"])

    print(d.get("cat"))
    print(d.pop("fruit"))

    print(d)

    d["car"] = 4000
    print(d)

    d.update({"pencil" : 0.50, "cat" : 100})
    print(d)




if __name__ == "__main__":
    main()
