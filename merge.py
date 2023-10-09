def merge_list(list1, list2):
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError("The inputs must be list type.")
    
    my_List = list1 + list2
    
    for variables in list1 + list2:
        if not isinstance(variables, int):
            raise TypeError("Both lists need to contain integers!")
        
    for i in range(len(my_List) - 1):    
        for j in range(0, len(my_List) - i - 1):  
            if my_List[j] > my_List[j+1]:   
                my_List[j], my_List[j+1] = my_List[j+1], my_List[j]

    return my_List
