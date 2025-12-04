from day4.day4 import solve_puzzle, solve_puzzzle_part_two
from utils.utils import read_from_file_input


input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

answer, result = solve_puzzle(input)
print(result)
print(answer)

input_2 = read_from_file_input('day4/data')
answer, result = solve_puzzle(input_2)
print(result)
print(answer)

result = solve_puzzzle_part_two(input_2)
print(result)