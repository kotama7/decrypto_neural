import pandas as pd

def cutting(max_len, path):
    """
        This function makes the length of each of lines of file indicated by path max_len.
        Encoding is UTF-8
    """

    with open(path, "r", encoding="utf-8") as f:
        
        writer = [string for string in f.readlines() if len(string) <= max_len + 1]

        # print(max(writer, key=lambda x:len(x)))

    with open(path, "w", encoding="utf-8") as f:

        f.writelines(writer)


def selecting(path):

    with open(path, "r", encoding="utf-8") as f:
        
        writer = [string for string in f.readlines() if string.isascii()]

        # print(max(writer, key=lambda x:len(x)))

    with open(path, "w", encoding="utf-8") as f:

        f.writelines(writer)

if __name__ == "__main__":

    n = int(input("Please input cutting limit>>>"))
    path = input("Please input cutting path>>>")

    # cutting(n, path)
    selecting(path)
