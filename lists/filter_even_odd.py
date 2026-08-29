numbers = [12, 5, 8, 3, 15, 20, 7, 4, 10]

even_numbers = []
odd_numbers = []

for number in numbers:

    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(even_numbers)
print(odd_numbers)