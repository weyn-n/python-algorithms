numbers = [4, 7, 2, 7, 4, 9, 2, 7, 5, 4]

counts = {}

for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

max_count = 0
most_common = 0

for number, count in counts.items():
    if count > max_count:
        max_count = count
        most_common = number

print(most_common)