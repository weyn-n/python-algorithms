numbers = [5, 2, 8, 5, 1, 5, 9, 2, 5, 7]

target = 5

count = 0
indexes = []

for i in range(len(numbers)):

    if numbers[i] == target:
        count += 1
        indexes.append(i)

print(f"Found: {count}")
print(f"Indexes: {indexes}")