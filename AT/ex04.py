import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def linear_search(isbn_list, target):
    iterations = 0
    for isbn in isbn_list:
        iterations += 1
        if iterations % 100 == 0:
            print(f"Linear search: Iterations so far: {iterations}")
        if isbn == target:
            logging.info(f"Linear search: found {target} after {iterations} iterations.")
            return True, iterations
    logging.info(f"Linear search: did not find {target}, total iterations: {iterations}")
    return False, iterations

def binary_search(isbn_list, target):
    left = 0
    right = len(isbn_list) - 1
    iterations = 0
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if isbn_list[mid] == target:
            logging.info(f"Binary search: found {target} after {iterations} iterations.")
            return True, iterations
        elif isbn_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    logging.info(f"Binary search: did not find {target}, total iterations: {iterations}")
    return False, iterations

def main():
    isbn_list = list(range(100000))
    target = 50000

    print("\nRunning Linear Search...")
    found_lin, lin_iters = linear_search(isbn_list, target)

    print("\nRunning Binary Search...")
    found_bin, bin_iters = binary_search(isbn_list, target)

    print("\n=== Exercise 4 Results ===")
    print(f"Linear Search - Found: {found_lin}, Iterations: {lin_iters}")
    print(f"Binary Search - Found: {found_bin}, Iterations: {bin_iters}")

if __name__ == '__main__':
    main()
