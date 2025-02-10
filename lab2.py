# with open('input_2.txt', 'r') as f:
#     data = f.read()

# reports = [list(map(int, line.split())) for line in data.strip().split('\n')]

# safe_count = 0

# for report in reports:
#     all_increasing = all(x < y for x, y in zip(report, report[1:]))
#     all_decreasing = all(x > y for x, y in zip(report, report[1:]))
    
#     if not (all_increasing or all_decreasing):
#         continue
#     valid_differences = all(1 <= abs(x - y) <= 3 for x, y in zip(report, report[1:]))
    
#     if valid_differences:
#         safe_count += 1

# print(safe_count)
# Result: 218

def is_safe(report):
    all_increasing = all(x < y for x, y in zip(report, report[1:]))
    all_decreasing = all(x > y for x, y in zip(report, report[1:]))
    
    if not (all_increasing or all_decreasing):
        return False

    valid_differences = all(1 <= abs(x - y) <= 3 for x, y in zip(report, report[1:]))
    
    return valid_differences

def is_safe_with_removal(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    
    return False

with open('input_2.txt', 'r') as f:
    data = f.read()

reports = [list(map(int, line.split())) for line in data.strip().split('\n')]

safe_count = 0

for report in reports:
    if is_safe_with_removal(report):
        safe_count += 1

print(safe_count)
#Result: 290