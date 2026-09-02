while True:

    number = float(input("Enter number: "))
    result = 1

    while number > 0:

        result *= number
        number -= 1

    print(int(result))