attempts = [10, 0, 7, -1, 15, 3, 0, 8, -1, 20, 5]

total_attempts = 0
total_score = 0

successful = 0 # >= 10
failed = 0 # < 10

successful_scores = []
failed_scores = []

best_score = 0

for score in attempts:

    if score == -1:
        continue

    total_attempts += 1
    total_score += score

    if score >= 10:
        successful += 1
        successful_scores.append(score)
    else: 
        failed += 1
        failed_scores.append(score)

    if score > best_score:
        best_score = score


print(f"Total attempts: {total_attempts}")
print(f"Total score: {total_score}")
print(f"Successful: {successful}")
print(f"Failed: {failed}")
print(f"Successful scores: {successful_scores}")
print(f"Failed scores: {failed_scores}")
print(f"Best score: {best_score}")