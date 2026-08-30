def analyze_number(number):

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

    if number > 10:
        print("Greater than 10")
    else:
        print("Not greater than 10")

while True:
    number = int(input("Write the number: "))
    analyze_number(number)