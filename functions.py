import random

def shuffle_lines(filename: str):

    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
    
    random.shuffle(lines)
    
    with open(filename, 'w', encoding="utf-8") as file:
        file.writelines(lines)


def string_as_binary(string: str):

    binary_string = ""
    
    for char in string:
        binary = bin(ord(char))[2:].zfill(8)  # 文字をASCIIコードに変換し、8ビットのバイナリ文字列に変換
        binary_string += binary
    
    return binary_string

if __name__ == "__main__":

    filename = "./password_data/rockyou.txt"
    shuffle_lines(filename)

