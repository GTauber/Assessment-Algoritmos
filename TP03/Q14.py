def sum_list(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_list(numbers[1:])


if __name__ == "__main__":
    print("Sum of [5, 10, 15]:", sum_list([1, 2, 3, 4]))
