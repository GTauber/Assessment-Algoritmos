def greatest_number(array):
    greatest = float('-inf')
    for i in array:
        if i > greatest:
            greatest = i

    return greatest
