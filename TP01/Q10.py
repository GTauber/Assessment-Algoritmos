def bubble_sort_strings(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j].lower() > arr[j + 1].lower():
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

def test_bubble_sort_strings(test_case):
    print(f"\nTest #{test_case[0]}")
    print(f"Original Array: {test_case[1]}")
    sorted_array = bubble_sort_strings(test_case[1].copy())
    print(f"Sorted Array: {sorted_array}")

test_cases = [
    (1, ["banana", "maçã", "laranja", "uva", "pera"]),
    (2, ["Zebra", "abacaxi", "Laranja", "banana"]),
    (3, ["casa", "carro", "cachorro", "cavalo"]),
    (4, ["ana", "beatriz", "carlos", "david"]),
    (5, ["zeus", "yuri", "xavier", "wagner"]),
    (6, ["teste"]),
    (7, []),
    (8, ["joão", "maría", "andré", "josé"]),
    (9, ["a", "abc", "ab", "abcd"]),
    (10, ["casa", "casa", "bola", "bola", "arte"])
]

for test_case in test_cases:
    test_bubble_sort_strings(test_case)