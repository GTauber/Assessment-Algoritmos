def reverse_queue(queue):
    stack = []

    while queue:
        stack.append(queue.pop(0))

    while stack:
        queue.append(stack.pop())

    return queue

patients_queue = ["Pat 1", "Pat 2", "Pat 3", "Pat 4"]
print("Original queue:", patients_queue)

reversed_queue = reverse_queue(patients_queue)
print("Reverse Queue:", reversed_queue)
