def cutting():
    with open("./password_data/rockyou.txt", "r", encoding="utf-8") as f:
        
        MAX_LEN = 48
        
        writer = [ string for string in f.readlines() if len(string) <= MAX_LEN + 1]

        # print(max(writer, key=lambda x:len(x)))

    with open("./password_data/rockyou.txt", "w", encoding="utf-8") as f:

        f.writelines(writer)

if __name__ == "__main__":
    cutting()