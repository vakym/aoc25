
import math


def zero_cnt(str_pos: int, instruction: str) -> int:
    zero_count = 0
    position = str_pos
    for line in instruction.split('\n'):
        if not line:
            continue
        line = line.strip()
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'L':
            position = (position - distance) % 100
        else:
            position = (position + distance) % 100
        
        if position == 0:
            zero_count += 1
    return zero_count

def zero_cnt_with_rotation(start_pos: int, instructions: str) -> int:
    zero_count, pos = 0, start_pos
    
    for line in instructions.split('\n'):
        if line.strip():
            direction, distance = line[0], int(line[1:])
            gap = 100 if pos == 0 else (100 - pos if direction == 'R' else pos)
            zero_count += (distance - gap) // 100 + 1 if distance >= gap else 0
            pos = (pos + distance if direction == 'R' else pos - distance) % 100
    
    return zero_count





