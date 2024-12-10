def reverse_string(string):
    if len(string) <= 1:
        return string
    return string[-1] + reverse_string(string[:-1])


if __name__ == "__main__":
    print("Reverse of 'recursao':", reverse_string("recursao"))
    print("Reverse of 'python':", reverse_string("python"))
