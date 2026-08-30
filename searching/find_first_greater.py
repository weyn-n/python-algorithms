numbers = [3, 7, 2, 9, 4, 12, 6, 15]

target = 10

found = []
index = -1
found_result = False

for number in range(len(numbers)):

    if numbers[number] > target:
        found = numbers[number]
        index = number
        found_result = True
        break

if found:    
    print(f"Found: {found}")  
    print(f"Index: {index}")
else:
    print("Number not found")