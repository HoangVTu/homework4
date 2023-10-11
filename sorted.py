def sort_dictionary(d):
    if not isinstance(d, dict):
        raise TypeError("Input must be a dictionary.")
    
    sorted_list = sorted(d.items(), key = lambda x: x[0], reverse = True)

    revers_list = [(name, phone[0]) for name, phone in sorted_list]

    return revers_list