import time
import psutil
from collections import deque
from typing import Any, List, Dict


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")

    def peek(self) -> Any:
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")

    def is_empty(self) -> bool:
        return len(self.items) == 0

    @property
    def size(self) -> int:
        return len(self.items)

    def get_at_index(self, index: int) -> Any:
        if 0 <= index < len(self.items):
            return self.items[index]
        raise IndexError("Index out of range")

    def display(self) -> None:
        print(self.items)


class Queue:

    def __init__(self):
        self.items = deque()

    def enqueue(self, item: Any) -> None:
        self.items.append(item)

    def dequeue(self) -> Any:
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError("Queue is empty")

    def peek(self) -> Any:
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Queue is empty")

    def is_empty(self) -> bool:
        return len(self.items) == 0

    @property
    def size(self) -> int:
        return len(self.items)

    def get_at_index(self, index: int) -> Any:
        if 0 <= index < len(self.items):
            return self.items[index]
        raise IndexError("Index out of range")


class HashTable:
    def __init__(self, initial_capacity: int = 10000):
        self._capacity = initial_capacity
        self.table = [[] for _ in range(initial_capacity)]
        self._items_count = 0
        self._items_list = []

    def _hash(self, key: str) -> int:
        return sum(ord(c) for c in key) % self._capacity

    def insert(self, key: str) -> None:
        hash_value = self._hash(key)
        if not any(item[0] == key for item in self.table[hash_value]):
            self.table[hash_value].append((key, self._items_count))
            self._items_list.append(key)
            self._items_count += 1

    def get(self, key: str) -> Any:
        hash_value = self._hash(key)
        for item_key, _ in self.table[hash_value]:
            if item_key == key:
                return item_key
        raise KeyError("Key not found")

    def remove(self, key: str) -> None:
        hash_value = self._hash(key)
        for i, (item_key, _) in enumerate(self.table[hash_value]):
            if item_key == key:
                self.table[hash_value].pop(i)
                self._items_list.remove(key)
                self._items_count -= 1
                return
        raise KeyError("Key not found")

    def get_at_index(self, index: int) -> Any:
        if 0 <= index < len(self._items_list):
            return self._items_list[index]
        raise IndexError("Index out of range")

    @property
    def size(self) -> int:
        return self._items_count


class DataStructureAnalyzer:
    def __init__(self, filename: str):
        self.filename = filename
        self.data = self._load_data()
        self.positions_to_check = [0, 99, 999, 4999, -1]

    def _load_data(self) -> List[str]:
        with open(self.filename, 'r') as file:
            return [line.strip() for line in file.readlines()]

    def _measure_execution(self, func, *args) -> Dict:
        process = psutil.Process()
        memory_start = process.memory_info().rss / 1024 / 1024
        start_time = time.time()

        result = func(*args)

        end_time = time.time()
        memory_end = process.memory_info().rss / 1024 / 1024  # MB

        return {
            'time': end_time - start_time,
            'memory': memory_end - memory_start,
            'result': result
        }

    def _populate_structure(self, structure) -> Dict:
        def populate():
            for item in self.data:
                if isinstance(structure, HashTable):
                    structure.insert(item)
                elif isinstance(structure, (Stack, Queue)):
                    structure.push(item) if isinstance(structure, Stack) else structure.enqueue(item)

        return self._measure_execution(populate)

    def _get_positions(self, structure) -> Dict:
        def check_positions():
            results = {}
            for pos in self.positions_to_check:
                try:
                    index = pos if pos >= 0 else structure.size + pos
                    results[f"position_{index + 1}"] = structure.get_at_index(index)
                except IndexError:
                    results[f"position_{pos + 1}"] = "N/A"
            return results

        return self._measure_execution(check_positions)

    def _test_operations(self, structure) -> Dict:
        def operations():
            results = {}

            add_items = ["test_item_" + str(i) for i in range(5)]
            for item in add_items:
                if isinstance(structure, HashTable):
                    structure.insert(item)
                elif isinstance(structure, Stack):
                    structure.push(item)
                else:
                    structure.enqueue(item)

            for _ in range(3):
                if isinstance(structure, HashTable):
                    structure.remove(add_items[_])
                elif isinstance(structure, Stack):
                    structure.pop()
                else:  # Queue
                    structure.dequeue()

            return "Operations completed successfully"

        return self._measure_execution(operations)

    def analyze_all(self) -> Dict:
        structures = {
            'HashTable': HashTable(),
            'Stack': Stack(),
            'Queue': Queue()
        }

        results = {}

        for name, structure in structures.items():
            print(f"\nAnalyzing {name}...")

            pop_results = self._populate_structure(structure)

            pos_results = self._get_positions(structure)

            op_results = self._test_operations(structure)

            results[name] = {
                'population': pop_results,
                'positions': pos_results,
                'operations': op_results
            }

            print(f"\nResults for {name}:")
            print(f"Populating time: {pop_results['time']:.6f} secs")
            print(f"Used memory on population: {pop_results['memory']:.2f} MB")
            print("\nFound positions:")
            for pos, value in pos_results['result'].items():
                print(f"{pos}: {value}")
            print(f"\nOperations execution time: {op_results['time']:.6f} secs")
            print(f"Used memory on operations: {op_results['memory']:.2f} MB")

        return results


def main():
    analyzer = DataStructureAnalyzer('/Users/gtauber/Documents/Development/College/2024/T4/PB/tp1/list_files.txt')
    results = analyzer.analyze_all()


if __name__ == "__main__":
    main()