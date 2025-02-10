# 1 task
# left = []
# right = []

# with open('input.txt', 'r') as file:
#     for line in file:
#         parts = line.strip().split()
#         if len(parts) == 2:
#             left_num = int(parts[0])
#             right_num = int(parts[1])
#             left.append(left_num)
#             right.append(right_num)

# left_sorted = sorted(left)
# right_sorted = sorted(right)

# total = 0
# for l, r in zip(left_sorted, right_sorted):
#     total += abs(l - r)

# print(total)
#Result: 1660292

# 2 task
from collections import Counter
with open('input.txt', 'r') as f:
    lines = f.readlines()

left_numbers = []
right_numbers = []

for line in lines:
    parts = line.strip().split()
    if len(parts) >= 2:
        left_numbers.append(int(parts[0]))
        right_numbers.append(int(parts[1]))

right_counter = Counter(right_numbers)

similarity_score = 0
for num in left_numbers:
    count = right_counter.get(num, 0)
    similarity_score += num * count

print(similarity_score)
#Result: 22776016