import random
import time
from typing import List


def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)


def generate_random_numbers(size: int, min_value: int = 1, max_value: int = 5000000) -> List[int]:
    return [random.randint(min_value, max_value) for _ in range(size)]


def main():
    LIST_SIZE = 5_000_000

    print(f"Generating {LIST_SIZE:,} random numbers...")
    start_time = time.time()
    numbers = generate_random_numbers(LIST_SIZE)
    generation_time = time.time() - start_time
    print(f"Generation completed in {generation_time:.2f} seconds")

    print("\nStarting QuickSort...")
    start_time = time.time()
    sorted_numbers = quicksort(numbers)
    sorting_time = time.time() - start_time
    print(f"Sorting completed in {sorting_time:.2f} seconds")

    print("\nSample of sorted numbers:")
    print("First 5:", sorted_numbers[:5])
    print("Last 5:", sorted_numbers[-5:])

    print("\nPerformance:")
    print(f"Data Generation: {generation_time:.2f} seconds")
    print(f"Sorting Time: {sorting_time:.2f} seconds")
    print(f"Total Time: {generation_time + sorting_time:.2f} seconds")


if __name__ == "__main__":
    main()