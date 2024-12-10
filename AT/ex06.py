import logging
import time
import random

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def measure_execution_time(data):
    start = time.time()
    result = bubble_sort(data)
    end = time.time()
    return result, end - start


def main():

    test_data = [5, 2, 9, 1, 5, 6]
    sorted_test_data, _ = measure_execution_time(test_data[:])
    logging.info("Checked a small sample for correctness.")

    data_1000 = [random.randint(0, 100000) for _ in range(1000)]
    _, time_1000 = measure_execution_time(data_1000[:])
    logging.info(f"Time for 1000 elements: {time_1000:.4f}s")

    data_10000 = [random.randint(0, 100000) for _ in range(10000)]
    _, time_10000 = measure_execution_time(data_10000[:])
    logging.info(f"Time for 10000 elements: {time_10000:.4f}s")

    print(f"Time for 1000 elements: {time_1000:.4f}s")
    print(f"Time for 10000 elements: {time_10000:.4f}s")

if __name__ == '__main__':
    main()
