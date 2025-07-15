def decimal_to_binary(number):

    if number == 0:
        return "0"
    elif number == 1:
        return "1"
    else:
        return decimal_to_binary(number // 2) + str(number % 2)


def main():
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            raise ValueError("Number cannot be negative")
        else:
            binary = decimal_to_binary(number)
            print(binary)
    except ValueError:
        print("Invalid input")

main()




