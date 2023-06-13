import pandas as pd

def cutting(max_len, path):
    """
        This functio makes the length of each of lines of file indicated by path max_len.
        Encoding is UTF-8
    """

    with open(path, "r", encoding="utf-8") as f:
        
        writer = [string for string in f.readlines() if len(string) <= max_len + 1]

        # print(max(writer, key=lambda x:len(x)))

    with open(path, "w", encoding="utf-8") as f:

        f.writelines(writer)


if __name__ == "__main__":