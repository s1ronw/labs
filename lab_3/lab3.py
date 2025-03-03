# def extract_calibration_value(line):
#     digits = [char for char in line if char.isdigit()]
    

#     if not digits:
#         return 0
#     calibration_value = int(digits[0] + digits[-1])
#     return calibration_value

# def sum_calibration_values(file_path):
#     total_sum = 0
    
#     with open(file_path, 'r') as file:
#         for line in file:
#             line = line.strip()
#             calibration_value = extract_calibration_value(line)
#             total_sum += calibration_value
    
#     return total_sum

# file_path = 'input.txt'

# total_sum = sum_calibration_values(file_path)
# print(f"The sum of all calibration values is: {total_sum}")
# Result: 55538

import re

digit_words = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"

def extract_calibration_value(line):
    matches = re.findall(pattern, line)
    
    if not matches:
        return 0

    matches = [digit_words.get(match, match) for match in matches]

    calibration_value = int(matches[0] + matches[-1])
    return calibration_value

def sum_calibration_values(file_path):
    total_sum = 0
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            calibration_value = extract_calibration_value(line)
            total_sum += calibration_value
    
    return total_sum

file_path = 'input.txt'
total_sum = sum_calibration_values(file_path)
print(f"The sum of all calibration values is: {total_sum}")
# Result: 54875