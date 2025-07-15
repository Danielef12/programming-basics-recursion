def add_value():
    value = input("Insert a number")

    if value == "":
        return 0.0
    else:
        try:
            number = float(value)
            return number + add_value()
        except ValueError:
            print("Not a number")
            return add_value()


total = add_value()
print("The total is", total)
