def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(middle):
        return middle[0]
    else:
        return quickselect(right, k - len(left) - len(middle))


if __name__ == "__main__":
    arr = [3, 2, 1, 5, 4]
    k = 3
    print(f"The {k}-th smallest element is:", quickselect(arr, k - 1))
