def order_list(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j

        list[i], list[min_index] = list[min_index], list[i]

    return list

number_list = [64, 25, 12, 22, 11]
print("Original List:", number_list)

Ordered_list = order_list(number_list)
print("Ordered List:", Ordered_list)
