def sum_recursive(numbers):
    if not numbers:
        return 0
    return numbers[0] + sum_recursive(numbers[1:])


if __name__ == "__main__":
    # Example usage
    print("Sum of [1, 2, 3, 4]:", sum_recursive([1, 2, 3, 4]))
