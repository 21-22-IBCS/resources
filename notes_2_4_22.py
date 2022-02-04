def main():

    #Creating and using a dictionary
    #a data structure

    #starbucks
    d = {
        "iced coffee" : 5.50,
        "croissant" : 3.75,
        "strawberry aqua" : 15.25,
        "iced coffee" : 4.00
        }

    print(d)
    #get value
    print(d["iced coffee"])
    price = d.get("iced coffee")
    print(price)
    print(d.keys())
    print(d.values())


if __name__ == "__main__":
    main()
