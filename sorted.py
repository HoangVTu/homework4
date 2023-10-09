def reverse_sort_dictionary(d):
    sorted_list = []

    for name, (phone_number, age) in sorted(d.items(), key = lambda x: x[1], reverse = True):
        sorted_list.append((name, phone_number))

    return sorted_list
