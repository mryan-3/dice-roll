import random

face_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
total_rolls = 1000

# Roll the die 1000 times
for _ in range(total_rolls):
    rand = random.random()

    face = int(rand * 6) + 1

    face_counts[face] += 1

print("Face\tFrequency\tPercentage")
print("-" * 35)

# Print results for each face
for face in range(1, 7):
    frequency = face_counts[face]
    percentage = (frequency / total_rolls) * 100
    print(f"{face}\t{frequency}\t\t{percentage:.2f}%")
