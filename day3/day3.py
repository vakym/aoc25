def find_joltage(instruction: str) -> int:
    total_joltage = 0
    for line in instruction.split('\n'):
        total_joltage += find_line_joltage(line)
    return total_joltage
        
        
#987654321111111
def find_line_joltage(line: str) -> int:
    values = []
    current_max_value = 0
    current_max_minux_one = 0
    for value in line:
        number = int(value)
        if current_max_value < number:
            values.append(current_max_value * 10 + number)
            current_max_value = number
            current_max_minux_one = 0
        else:
            if current_max_minux_one < number:
                current_max_minux_one = number
                values.append(current_max_value * 10 + current_max_minux_one)
    return  max(values)
            