numbers = [14, 7, 23, 5, 18, 42, 9, 31, 6, 12]

target = 42

found = False
index = -1

for number in range(len(numbers)):

    if numbers[number] == target:
        found = True
        index = number
        break

if found:
    print("Target found")
    print(f"Number: {target}")
    print(f"Index: {index}")
else:
    print("Target not found")