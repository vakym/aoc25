import numpy as np


def to_array(instruction: str):
    array = None
    for line in instruction.split('\n'):
        if not line:
            continue
        int_line = convert_line(line)
        if array is None:
            array = np.array(int_line)
        else:
            array = np.vstack([array, int_line])
    return array

def convert_line(line: str) -> list[int]:
    array = []
    for char in line:
        if char == '@':
            array.append(1)
        else:
            array.append(0)
    return array
            
def count_rolls(array, x_1, y_1, x, y) -> int:
    rolls = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            y_2 = y_1 + i
            x_2 = x_1 + j
            if not in_borders(x_2, y_2, x, y):
                continue
            rolls += array[x_2,y_2]
    return rolls
            
            
def in_borders(x,y, widht, heigth) -> bool:
    return (x >= 0 and x <widht) and (y >= 0 and y < heigth)


def solve_puzzle(instruction: str) -> int:
    array = to_array(instruction)
    y, x = array.shape
    can_move_rolls_cnt = 0
    answer = np.zeros((x,y))
    for x_1 in range(x):
        for y_1 in range(y):
            answer[x_1, y_1] = array[x_1, y_1]
            if array[x_1, y_1] != 1:
                continue
            if count_rolls(array, x_1, y_1, x, y) < 4:
                can_move_rolls_cnt +=1
                answer[x_1, y_1] = 2
    return answer, can_move_rolls_cnt

def solve_puzzzle_part_two(instruction: str) -> int:
    array = to_array(instruction)
    total_removed = 0
    while True:
        new_array, removed_cnt = find_removeable_rolls(array)
        total_removed += removed_cnt
        array = new_array
        if removed_cnt == 0:
            break
    return total_removed
    
    
def find_removeable_rolls(array):
    y, x = array.shape
    answer = np.zeros((x,y))
    removed = 0
    for x_1 in range(x):
        for y_1 in range(y):
            answer[x_1, y_1] = array[x_1, y_1]
            if array[x_1, y_1] != 1:
                continue
            if count_rolls(array, x_1, y_1, x, y) < 4:
                removed +=1
                answer[x_1, y_1] = 0
    return answer, removed
            