grades = [5, 3, 4, 5, 2, 4, 5, 3, 4, 5]

good_grades = [] # 4 and 5
bad_grades = [] # 2 and 3

good_count = 0
bad_count = 0

for grade in grades:

    if 3 < grade < 6:
        good_grades.append(grade)
    else:

        bad_grades.append(grade)

for count in good_grades:
    good_count = good_count + 1

for count in bad_grades:
    bad_count = bad_count + 1

print(good_count)
print(bad_count)