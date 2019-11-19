def NotIn(list1, list2):
    not_list = []
    for i in range(len(list1)):
        if list1[i] not in list2:
            not_list.append(list1[i])
    return not_list
