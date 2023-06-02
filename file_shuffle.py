import random

def shuffle_lines_in_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    random.shuffle(lines)
    
    with open(filename, 'w') as file:
        file.writelines(lines)

# テキストファイルのパスを指定してください
filename = "./password_data/rockyou.txt"

shuffle_lines_in_file(filename)
