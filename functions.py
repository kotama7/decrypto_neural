import random
import warnings

def shuffle_lines(filename: str):

    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
    
    random.shuffle(lines)
    
    with open(filename, 'w', encoding="utf-8") as file:
        file.writelines(lines)


def string_as_binary(string: str, shape= 48):

    binary_string = ""
    
    for char in string:
        binary = bin(ord(char))[2:].zfill(8)  # 文字をASCIIコードに変換し、8ビットのバイナリ文字列に変換
        binary_string += binary
    
    binary_string = binary_string.ljust(48,"0")

    if len(binary_string) > shape:
        warnings.warn(f"Unconstant Shape: The returned shape is unconstant. expected {shape}, but {len(binary_string)}")

    return binary_string



if __name__ == "__main__":

    print(string_as_binary("Hello"))

    # filename = "./password_data/rockyou.txt"
    # shuffle_lines(filename)