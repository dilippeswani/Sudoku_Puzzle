row = {"r1": (0, 1, 2, 3, 4, 5, 6, 7, 8), "r2": (9, 10, 11, 12, 13, 14, 15, 16, 17),
       "r3": (18, 19, 20, 21, 22, 23, 24, 25, 26), "r4": (27, 28, 29, 30, 31, 32, 33, 34, 35),
       "r5": (36, 37, 38, 39, 40, 41, 42, 43, 44), "r6": (45, 46, 47, 48, 49, 50, 51, 52, 53),
       "r7": (54, 55, 56, 57, 58, 59, 60, 61, 62), "r8": (63, 64, 65, 66, 67, 68, 69, 70, 71),
       "r9": (72, 73, 74, 75, 76, 77, 78, 79, 80)}

column = {"c1": (0, 9, 18, 27, 36, 45, 54, 63, 72), "c2": (1, 10, 19, 28, 37, 46, 55, 64, 73),
          "c3": (2, 11, 20, 29, 38, 47, 56, 65, 74), "c4": (3, 12, 21, 30, 39, 48, 57, 66, 75),
          "c5": (4, 13, 22, 31, 40, 49, 58, 67, 76), "c6": (5, 14, 23, 32, 41, 50, 59, 68, 77),
          "c7": (6, 15, 24, 33, 42, 51, 60, 69, 78), "c8": (7, 16, 25, 34, 43, 52, 61, 70, 79),
          "c9": (8, 17, 26, 35, 44, 53, 62, 71, 80)}

small_square = {"ss1": (0, 1, 2, 9, 10, 11, 18, 19, 20), "ss2": (3, 4, 5, 12, 13, 14, 21, 22, 23),
                "ss3": (6, 7, 8, 15, 16, 17, 24, 25, 26), "ss4": (27, 28, 29, 36, 37, 38, 45, 46, 47),
                "ss5": (30, 31, 32, 39, 40, 41, 48, 49, 50), "ss6": (33, 34, 35, 42, 43, 44, 51, 52, 53),
                "ss7": (54, 55, 56, 63, 64, 65, 72, 73, 74), "ss8": (57, 58, 59, 66, 67, 68, 75, 76, 77),
                "ss9": (60, 61, 62, 69, 70, 71, 78, 79, 80)}

universal_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

c_small_squares = {
    "A": (0, 1, 2, 9, 10, 11, 18, 19, 20, 3, 4, 5, 12, 13, 14, 21, 22, 23, 6, 7, 8, 15, 16, 17, 24, 25, 26),
    "B": (27, 28, 29, 36, 37, 38, 45, 46, 47, 30, 31, 32, 39, 40, 41, 48, 49, 50, 33, 34, 35, 42, 43, 44, 51, 52, 53),
    "C": (54, 55, 56, 63, 64, 65, 72, 73, 74, 57, 58, 59, 66, 67, 68, 75, 76, 77, 60, 61, 62, 69, 70, 71, 78, 79, 80),
    "D": (0, 1, 2, 9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38, 45, 46, 47, 54, 55, 56, 63, 64, 65, 72, 73, 74),
    "E": (3, 4, 5, 12, 13, 14, 21, 22, 23, 30, 31, 32, 39, 40, 41, 48, 49, 50, 57, 58, 59, 66, 67, 68, 75, 76, 77),
    "F": (6, 7, 8, 15, 16, 17, 24, 25, 26, 33, 34, 35, 42, 43, 44, 51, 52, 53, 60, 61, 62, 69, 70, 71, 78, 79, 80)}

# 3
# sudoku_puzzle = [4, 0, 0, 0, 0, 0, 6, 5, 0,
#                  0, 3, 1, 6, 7, 0, 0, 0, 0,
#                  0, 0, 0, 0, 9, 0, 8, 0, 7,
#                  3, 0, 9, 2, 0, 0, 0, 0, 0,
#                  0, 5, 0, 0, 0, 0, 0, 3, 0,
#                  0, 0, 0, 0, 0, 1, 4, 0, 5,
#                  7, 0, 3, 0, 1, 0, 0, 0, 0,
#                  0, 0, 0, 0, 8, 7, 1, 2, 0,
#                  0, 1, 2, 0, 0, 0, 0, 0, 8]

# ##4
# sudoku_puzzle = [0, 2, 5, 3, 0, 6, 9, 0, 4,
#                  9, 6, 4, 2, 0, 1, 5, 3, 0,
#                  3, 0, 8, 5, 9, 4, 2, 6, 0,
#                  2, 4, 0, 0, 5, 3, 1, 0, 0,
#                  0, 5, 0, 4, 6, 7, 3, 0, 2,
#                  0, 3, 7, 0, 0, 2, 0, 0, 5,
#                  0, 9, 2, 0, 4, 8, 7, 5, 3,
#                  4, 0, 0, 0, 3, 5, 8, 2, 9,
#                  5, 8, 3, 0, 2, 9, 0, 0, 0]

##5
# sudoku_puzzle = [0, 8, 0, 0, 1, 3, 0, 6, 0,
#                  0, 0, 5, 6, 9, 2, 7, 8, 0,
#                  0, 0, 0, 0, 0, 0, 0, 9, 0,
#                  8, 2, 0, 1, 5, 0, 0, 3, 0,
#                  0, 0, 0, 3, 2, 6, 0, 4, 0,
#                  0, 5, 3, 9, 0, 0, 0, 1, 2,
#                  5, 4, 1, 2, 3, 9, 0, 7, 0,
#                  3, 6, 8, 4, 7, 5, 1, 2, 9,
#                  0, 9, 0, 8, 6, 1, 0, 5, 0]
##6
# sudoku_puzzle = [0, 8, 0, 7, 1, 3, 2, 6, 5,
#                  1, 3, 5, 6, 9, 2, 7, 8, 4,
#                  0, 7, 0, 5, 0, 0, 3, 9, 1,
#                  8, 2, 0, 1, 5, 0, 9, 3, 0,
#                  0, 1, 0, 3, 2, 6, 5, 4, 0,
#                  0, 5, 3, 9, 0, 0, 0, 1, 2,
#                  5, 4, 1, 2, 3, 9, 0, 7, 0,
#                  3, 6, 8, 4, 7, 5, 1, 2, 9,
#                  0, 9, 0, 8, 6, 1, 4, 5, 3]

##6o
sudoku_puzzle = [0, 8, 0, 0, 1, 3, 0, 6, 0,
                 0, 0, 5, 0, 9, 2, 7, 8, 4,
                 0, 0, 0, 0, 0, 0, 0, 9, 0,
                 8, 2, 0, 0, 0, 0, 0, 3, 0,
                 0, 1, 0, 3, 0, 6, 0, 0, 0,
                 0, 5, 0, 0, 0, 0, 0, 1, 2,
                 0, 4, 0, 0, 0, 0, 0, 0, 0,
                 0, 6, 8, 4, 7, 0, 1, 0, 0,
                 0, 9, 0, 8, 6, 0, 0, 5, 0]

print(sudoku_puzzle.count(0))


def paste_sudoku_puzzle_in_matrix(sudoku_list):
    for index, values in enumerate(sudoku_list, start=1):
        if index % 9 == 0:
            print(values, end="\n")
        else:
            print(values, end=" ")


list_index_value_0 = []


def find_index_for_value_0_sudoku_puzzle(sudoku_puzzle):
    for index, value in enumerate(sudoku_puzzle):
        if value == 0:
            list_index_value_0.append(index)
    return list_index_value_0


list_associate_r_c_ss_number_as_index = []


def find_r_c_ss_number_as_index_value_0(list_index_value_0):
    for index in list_index_value_0:
        list_of_rows = [key for key, list_of_values in row.items() if index in list_of_values]
        # print (list_of_rows)
        list_of_columns = [key for key, list_of_values in column.items() if index in list_of_values]
        list_of_small_squares = [key for key, list_of_values in small_square.items() if index in list_of_values]
        list_associate_r_c_ss_number_as_index.append(list_of_rows + list_of_columns + list_of_small_squares)
    return list_associate_r_c_ss_number_as_index


# print (list_associate_r_c_ss_number_as_index)

dict_index_value_zero_r_c_ss = dict()


def zip_to_create_dict(list_index_value_0, list_associate_r_c_ss_number_as_index):
    zip_operator = zip(list_index_value_0, list_associate_r_c_ss_number_as_index)
    dict_index_value_zero_r_c = dict(zip_operator)
    for key, value in dict_index_value_zero_r_c.items():
        dict_index_value_zero_r_c_ss[key] = value
        # print (dict_index_value_zero_r_c_ss)
    return dict_index_value_zero_r_c_ss


dict_possible_value = dict()


def dict_possible_zero_values(dict_index_value_zero_r_c_ss):
    for key, value in dict_index_value_zero_r_c_ss.items():
        row_ind = row.get(value[0])
        column_ind = column.get(value[1])
        ss_ind = small_square.get(value[2])
        row_lst = []
        for x in row_ind:
            if sudoku_puzzle[x] != 0:
                row_lst.append(sudoku_puzzle[x])
        column_lst = []
        for x in column_ind:
            if sudoku_puzzle[x] != 0:
                column_lst.append(sudoku_puzzle[x])
        ss_lst = []
        for x in ss_ind:
            if sudoku_puzzle[x] != 0:
                ss_lst.append(sudoku_puzzle[x])
        row_set = set(row_lst)
        column_set = set(column_lst)
        ss_set = set(ss_lst)
        final_set = (row_set | column_set | ss_set)
        value_set = universal_set - final_set
        dict_possible_value[key] = value_set
        # for index, val in enumerate(sudoku_puzzle):
        #     if val != 0:
        #         for keys, values in dict_possible_value.items():
        #             if keys == index:
        #                 del dict_possible_value[keys]
    return dict_possible_value
# dict_possible_value = dict()
# def del_key_filled_values (dict_possible_value , sudoku_puzzle):
#     for index, value in enumerate(sudoku_puzzle):
#         if value != 0:
#             for keys,values in dict_possible_values.items():
#                 if keys == index:
#                     dict_possible_value = dict_possible_values.pop[keys]
#     return dict_possible_value

def update_missing_value(sudoku_puzzle):
    for index, value in enumerate(sudoku_puzzle):
        if value == 0:
            for key, val in dict_possible_value.items():
                if key == index:
                    if len(val) == 1:
                        sudoku_puzzle.pop(key)
                        value_int = set.pop(val)
                        sudoku_puzzle.insert(index, value_int)


def update_ss(sudoku_puzzle):
    for index, value in enumerate(sudoku_puzzle):
        if value == 0:
            for keys, values in small_square.items():
                if index in values:
                    my_dict = dict()
                    for y in values:
                        for key_s, value_s in dict_possible_value.items():
                            if key_s == y:
                                my_dict[y] = value_s
                    possible_value_for_index = []
                    for k, v in my_dict.items():
                        possible_value_for_index.append(list(my_dict.get(k)))
                    res = []
                    for nested_list in possible_value_for_index:
                        for z in nested_list:
                            res.append(z)
                    for valu in res:
                        repetition_count_of_value = res.count(valu)
                        if repetition_count_of_value == 1:
                            # print (valu)
                            for keyy, valuee in my_dict.items():
                                if valu in valuee:
                                    # print (keyy)
                                    sudoku_puzzle.pop(keyy)
                                    sudoku_puzzle.insert(keyy, valu)


def find_indentical_three_index_in_row_with_value_zero(sudoku_puzzle):
    # for index in range(0,80):
    for index, value in enumerate(sudoku_puzzle):
        values = []
        if value == 0:
            index2 = index + 1
            if sudoku_puzzle[index2] == 0:
                index3 = index2 + 1
                if sudoku_puzzle[index3] == 0:
                    values.append(index)
                    values.append(index2)
                    values.append(index3)
                    print(values)
                    my_dict = dict()
                    for y in values:
                        for key_s, value_s in dict_possible_value.items():
                            if key_s == y:
                                my_dict[y] = value_s
                    possible_value_for_index = []
                    for k, v in my_dict.items():
                        possible_value_for_index.append(list(my_dict.get(k)))
                    res = []
                    for nested_list in possible_value_for_index:
                        for z in nested_list:
                            res.append(z)
                    for valu in res:
                        repetition_count_of_value = res.count(valu)
                        if repetition_count_of_value == 1:
                            # print (valu)
                            for keyy, valuee in my_dict.items():
                                if valu in valuee:
                                    # print (keyy)
                                    sudoku_puzzle.pop(keyy)
                                    sudoku_puzzle.insert(keyy, valu)
        else:
            continue





# paste_sudoku_puzzle_in_matrix(sudoku_puzzle)

find_index_for_value_0_sudoku_puzzle(sudoku_puzzle)

for x in range(11):
    list_associate_r_c_ss_number_as_index = find_r_c_ss_number_as_index_value_0(list_index_value_0)
    dict_index_value_zero_r_c_ss = zip_to_create_dict(list_index_value_0, list_associate_r_c_ss_number_as_index)
    # dict_possible_zero_values(dict_index_value_zero_r_c_ss)
    print(dict_possible_zero_values(dict_index_value_zero_r_c_ss))
    # del_key_filled_values(dict_possible_value, sudoku_puzzle)
    update_ss(sudoku_puzzle)
    update_missing_value(sudoku_puzzle)

find_indentical_three_index_in_row_with_value_zero(sudoku_puzzle)
paste_sudoku_puzzle_in_matrix(sudoku_puzzle)
print(sudoku_puzzle.count(0))

# def compare_ss(sudoku_puzzle):
#     for index, value in enumerate(sudoku_puzzle):
#         if value == 0:
#             list_of_c_ss_keys = []
#             for keys, values in c_small_squares.items():
#                 if index in values:
#                     list_of_c_ss_keys.append(keys)
#             common_list_c_ss_index = (
#                     (c_small_squares.get(list_of_c_ss_keys[0])) + (c_small_squares.get(list_of_c_ss_keys[1])))
#             common_list_c_ss_value = []
#             for val in common_list_c_ss_index:
#                 if sudoku_puzzle[val] != 0:
#                     common_list_c_ss_value.append(sudoku_puzzle[val])
#                     for key_s, value_s in dict_possible_value.items():
#                         if key_s == index:
#                             possible_value_for_index = dict_possible_value.get(key_s)
#                             for valu in possible_value_for_index:
#                                 repetition_count_of_value = common_list_c_ss_value.count(valu)
#                                 if repetition_count_of_value == 4:
#                                     sudoku_puzzle.pop(index)
#                                     sudoku_puzzle.insert(index, valu)
#                                     # del dict_possible_value[key_s]
