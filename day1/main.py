import day1
if __name__ == '__main__':    
    start_position = 50
    instruction = ''
    with open('day1/data.txt','r') as f:
        instruction = f.read()
    result = day1.zero_cnt(str_pos=start_position, instruction=instruction)
    print(result)

    result2 = day1.zero_cnt_with_rotation(start_position, instruction)
    print(result2)

    test_instr = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

    test_data = day1.zero_cnt(start_position, test_instr)
    print(test_data)
    test_data2 = day1.zero_cnt_with_rotation(start_position, test_instr)
    print(test_data2)