def extract_calibration_value(line):
    # Extract the first digit
    first_digit = next((char for char in line if char.isdigit()), None)
    # Extract the last digit
    last_digit = next((char for char in reversed(line) if char.isdigit()), None)
    
    if first_digit is not None and last_digit is not None:
        return int(first_digit + last_digit)
    return 0

def calculate_total_calibration_value(lines):
    total_value = 0
    for line in lines:
        total_value += extract_calibration_value(line)
    return total_value

# Example input
lines = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]
with open('./examples/aoc/2023_1_1_input.txt', encoding='utf-8', mode='r') as f:
    lines = f.readlines()

print(calculate_total_calibration_value(lines=lines))



# def extract_calibration_values(lines):
#     calibration_values = []
#     for line in lines:
#         value = ''
#         for index, char in enumerate(line):
#             if index in (0, len(line) - 1):
#                 value += char
#         calibration_values.append(int(value))
#     return sum(calibration_values)

# lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
# print(extract_calibration_values(lines))


def find_calibration_values(input_string):
    total_sum = 0
    lines = input_string.split('\n')
    for line in lines:
        digits = [char for char in line if char.isdigit()]
        calibration_value = int(digits[0] + digits[-1])
        total_sum += calibration_value
    return total_sum

print(find_calibration_values(input_string='\n'.join([i.strip() for i in lines])))