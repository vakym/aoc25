from utils.utils import read_from_file_input
import day3.day3 as day3

test_input = """987654321111111
811111111111119
234234234234278
818181911112111"""
test_result = day3.find_joltage(test_input)
print(test_result)


data = read_from_file_input('day3/data')
result = day3.find_joltage(data)
print(result)