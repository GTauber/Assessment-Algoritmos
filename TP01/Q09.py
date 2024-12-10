def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def test_bubble_sort(arr):
    print(f"\nTest #{arr[0]}")
    print(f"Array original: {arr[1]}")
    sorted_array = bubble_sort(arr[1].copy())
    print(f"sorted array: {sorted_array}")

test_cases = [
    (1, [64, 34, 25, 12, 22, 11, 90]),
    (2, [5, 2, 8, 1, 9, 3]),
    (3, [1, 2, 3, 4, 5]),
    (4, [5, 4, 3, 2, 1]),
    (5, [1]),
    (6, []),
    (7, [1, 1, 1, 1, 1]),
    (8, [-5, 12, 0, -21, 8, -1])
]

for test_case in test_cases:
    test_bubble_sort(test_case)