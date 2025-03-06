import random

face_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
total_rolls = 1000

# Roll the die 1000 times
for _ in range(total_rolls):
    rand = random.random()

    if rand < 1/6:
        face_counts[1] += 1
    elif rand < 2/6:
        face_counts[2] += 1
    elif rand < 3/6:
        face_counts[3] += 1
    elif rand < 4/6:
        face_counts[4] += 1
    elif rand < 5/6:
        face_counts[5] += 1
    else:
        face_counts[6] += 1

total_frequency = 0

print("Face\tFrequency\tPercentage")
print("-" * 35)

# Print results for each face
for face in range(1, 7):
    frequency = face_counts[face]
    total_frequency += frequency

    percentage = (frequency / total_rolls) * 100
    print(f"{face}\t{frequency}\t\t{percentage:.1f}%")

print("-" * 35)
print(f"Total frequency: {total_frequency}")
