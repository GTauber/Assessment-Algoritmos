import random
import time
from typing import List, Optional


class Stack:

    def __init__(self):
        self.items: List[float] = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item: float) -> None:
        self.items.append(item)

    def pop(self) -> Optional[float]:
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self) -> Optional[float]:
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self) -> int:
        return len(self.items)

    def get_items(self) -> List[float]:
        return self.items.copy()


def sort_stack(stack: Stack) -> Stack:
    temp_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()

        while not temp_stack.is_empty() and temp_stack.peek() > temp:
            stack.push(temp_stack.pop())

        temp_stack.push(temp)

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return stack


def generate_test_grades(size: int, min_grade: float = 0.0, max_grade: float = 100.0) -> Stack:
    stack = Stack()
    for _ in range(size):
        grade = round(random.uniform(min_grade, max_grade), 1)
        stack.push(grade)
    return stack


def print_stack_sample(stack: Stack, sample_size: int = 5) -> None:
    items = stack.get_items()
    print("Bottom grades:", items[:sample_size])
    print("Top grades:", items[-sample_size:])


def main():
    # Configuration
    STACK_SIZE = 1000
    MIN_GRADE = 0.0
    MAX_GRADE = 100.0

    print(f"Generating stack with {STACK_SIZE:,} random grades...")
    start_time = time.time()
    original_stack = generate_test_grades(STACK_SIZE, MIN_GRADE, MAX_GRADE)
    generation_time = time.time() - start_time
    print(f"Data generation completed in {generation_time:.2f} seconds")

    print("\nOriginal Stack Sample:")
    print_stack_sample(original_stack)

    print("\nSorting stack...")
    start_time = time.time()
    sorted_stack = sort_stack(original_stack)
    sorting_time = time.time() - start_time

    print(f"\nSorting completed in {sorting_time:.2f} seconds")
    print("\nSorted Stack Sample:")
    print_stack_sample(sorted_stack)

    print("\nPerformance:\n")
    print(f"Data Generation Time: {generation_time:.2f} seconds")
    print(f"Sorting Time: {sorting_time:.2f} seconds")
    print(f"Total Time: {generation_time + sorting_time:.2f} seconds")


if __name__ == "__main__":
    main()