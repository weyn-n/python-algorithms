while True:

    number = int(input("Enter number: "))
    divisor = 2
    found_divisor = False

    if number < 2:
        print("Number is not prime")
    else:
        while divisor < number:

            if number % divisor == 0:
                found_divisor = True
                break

            divisor += 1

        if found_divisor:
            print("Number is not prime")
        else:
            print("Number is prime")
