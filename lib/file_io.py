def write_file(file_name, file_content):
    with open(f'{file_name}.txt', mode="w") as new_file:
        new_file.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode="a") as new_file:
        new_file.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt') as new_file:
        return new_file.read()

