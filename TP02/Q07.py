def count_even_orders(order_stack):
    counter = 0

    for order in order_stack:
        if order % 2 == 0:
            counter += 1

    return counter

order_stack = [101, 204, 303, 450, 501]
order_count = count_even_orders(order_stack)
print("Qty of order with even id", order_count)
