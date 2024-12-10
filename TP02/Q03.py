import random
import time
from typing import List

def find_duplicates_bruteforce(arr):
    duplicates = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j] and arr[i] not in duplicates:
                duplicates.append(arr[i])
    return duplicates


def find_duplicates(arr):
    seen_numbers = set()
    duplicates = set()

    for num in arr:
        if num in seen_numbers:
            duplicates.add(num)
        else:
            seen_numbers.add(num)

    return list(duplicates)

def generate_random_numbers(size: int, min_value: int = 1, max_value: int = 10000) -> List[int]:
    return [random.randint(min_value, max_value) for _ in range(size)]

def main():
    LIST_SIZE = 50_000

    print(f"Generating {LIST_SIZE:,} random numbers...")
    start_time = time.time()
    arr = generate_random_numbers(LIST_SIZE)
    generation_time = time.time() - start_time
    print(f"Generation completed in {generation_time:.2f} seconds")

    print("\nStarting BruteForce...")
    start_time = time.time()
    duplicates = find_duplicates_bruteforce(arr)
    bruteforce_time = time.time() - start_time
    print(f"Find duplicates (bruteforce) completed in {bruteforce_time:.2f} seconds")

    print("\nStarting Performance find duplicates...")
    start_time = time.time()
    duplicates_performance = find_duplicates(arr)
    performance_time = time.time() - start_time
    print(f"Find duplicates (performance) completed in {performance_time:.2f} seconds")

    print("\nFirst 5 duplicates in each method")
    print("First 5 (Bruteforce):", duplicates[:5])
    print("First 5 (Performance):", duplicates_performance[:5])

    print("\nPerformance:")
    print(f"Data Generation: {generation_time:.2f} seconds")
    print(f"BruteForce time: {bruteforce_time:.2f} seconds")
    print(f"Find duplicates (performance: {performance_time:.2f} seconds")


if __name__ == "__main__":
    main()