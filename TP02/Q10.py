def count_odd_books(queue_book):
    counter = 0

    for number in queue_book:
        if number % 2 != 0:
            counter += 1

    return counter

book_queue = [101, 204, 303, 450, 501, 602, 705]
odd_qty= count_odd_books(book_queue)
print("Qty of books with odd id", odd_qty)
