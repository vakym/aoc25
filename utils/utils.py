def read_from_file_input(file_name):
    instruction = ''
    with open(file_name,'r') as f:
        instruction = f.read()
    return instruction