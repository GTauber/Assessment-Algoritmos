def order_stack(stack):
    aux_stack = []

    while stack:
        tmp = stack.pop()
        while aux_stack and aux_stack[-1] > tmp:
            stack.append(aux_stack.pop())
        aux_stack.append(tmp)

    while aux_stack:
        stack.append(aux_stack.pop())

    return stack

notes_stack = [70, 85, 60, 90, 50]
print("Original Stack:", notes_stack)
ordered_stack = order_stack(notes_stack)
print("Ordered Stack:", ordered_stack)
