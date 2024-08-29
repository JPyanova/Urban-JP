my_list = [42, 69, 322, 13, 0, 69, -5, 9, 8, 7, -6, 5]
len_list = len(my_list)
index_list = 0
while index_list != len_list:
    if my_list[index_list] > 0:
        print(my_list[index_list])
    elif my_list[index_list] < 0:
        break
    index_list += 1


