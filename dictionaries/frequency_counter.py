numbers = [1, 2, 2, 3, 1, 2, 4, 3, 2]

counts = {}

for number in numbers:
    
    if number in counts:
        counts[number] += 1

    else:
        counts[number] = 1

print(counts)