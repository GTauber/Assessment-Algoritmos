def count_occurrences(string, char):
    if not string:
        return 0
    count = 1 if string[0] == char else 0
    return count + count_occurrences(string[1:], char)


if __name__ == "__main__":
    print("Occurrences of 'a' in 'banana':", count_occurrences("banana", "a"))
    print("Occurrences of 'x' in 'example':", count_occurrences("example", "x"))
