numbers = [12, 7, 3, 18, 5, 20, 9, 4, 15, 2]

even = []
odd = []

even_sum = 0
odd_sum = 0

for number in numbers:

    if number % 2 == 0:
        even.append(number)
        even_sum += number
    else:
        odd.append(number)
        odd_sum += number


print(even)
print(odd)
print(even_sum)
print(odd_sum)