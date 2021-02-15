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
                "ss3": (6, 7, 8, 15, 16, 17, 24, 25, 26), "ss4": (27, 28, 29, 36, 37, 38, 35, 46, 47),
                "ss5": (30, 31, 32, 39, 40, 41, 48, 49, 50), "ss6": (33, 34, 35, 42, 43, 44, 51, 52, 53),
                "ss7": (54, 55, 56, 63, 64, 65, 72, 73, 74), "ss8": (57, 58, 59, 66, 67, 68, 75, 76, 77),
                "ss9": (60, 61, 62, 69, 70, 71, 78, 79, 80)}

universal_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

sudoku_puzzle = [1, 2, 0, 4, 5, 0, 7, 8, 9,
                 0, 5, 6, 7, 8, 0, 1, 2, 3,
                 7, 0, 9, 1, 2, 3, 4, 0, 6,
                 3, 1, 2, 6, 0, 5, 9, 7, 8,
                 6, 4, 0, 9, 7, 8, 3, 0, 2,
                 9, 7, 8, 3, 1, 0, 6, 4, 5,
                 0, 3, 1, 5, 6, 4, 8, 0, 7,
                 8, 9, 7, 2, 0, 1, 5, 6, 0,
                 5, 6, 4, 8, 0, 7, 2, 3, 1]


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
        list_of_rows = associate_row_value_0_in_puzzle(index)
        list_of_columns = associate_column_value_0_in_puzzle(index)
        list_of_small_squares = associate_small_square_value_0_in_puzzle(index)
        list_associate_r_c_ss_number_as_index.append(list_of_rows + list_of_columns + list_of_small_squares)
    return list_associate_r_c_ss_number_as_index


def associate_row_value_0_in_puzzle(index_of_value_0):
    row_list = [key for key, list_of_values in row.items() if index_of_value_0 in list_of_values]
    return row_list


def associate_column_value_0_in_puzzle(index_of_value_0):
    column_list = [key for key, list_of_values in column.items() if index_of_value_0 in list_of_values]
    return column_list


def associate_small_square_value_0_in_puzzle(index_of_value_0):
    ss_list = [key for key, list_of_values in small_square.items() if index_of_value_0 in list_of_values]
    return ss_list


combine_list_values_r_c_ss_associate_value0 = []


def list_values_r_c_ss(list_associate_r_c_ss_as_index):
    for row_column_ss_value in list_associate_r_c_ss_as_index:
        row_value = row.get(row_column_ss_value[0])
        column_value = column.get(row_column_ss_value[1])
        ss_value = small_square.get(row_column_ss_value[2])
        row_lst = value_in_sudoku_puzzle_mapping_to_r_c_ss_value_as_index(row_value)
        column_lst = value_in_sudoku_puzzle_mapping_to_r_c_ss_value_as_index(column_value)
        ss_lst = value_in_sudoku_puzzle_mapping_to_r_c_ss_value_as_index(ss_value)
        combine_list_values_r_c_ss_associate_value0.append(row_lst + column_lst + ss_lst)
    return combine_list_values_r_c_ss_associate_value0


def value_in_sudoku_puzzle_mapping_to_r_c_ss_value_as_index(row_column_ss_list):
    list_of_values = []
    # details = [val for val in var if sudoku_puzzle[val]]
    for value in row_column_ss_list:
        if sudoku_puzzle[value]:
            list_of_values.append(sudoku_puzzle[value])
    return list_of_values


list_values_can_be_filled_missing_place = []


def find_approx_value_tobe_filled_missing_values(combine_list_values_r_c_ss_associate_value0):
    for values in combine_list_values_r_c_ss_associate_value0:
        covert_list_set = set(values)
        final_set = universal_set - covert_list_set
        convert_final_set_to_list = list(final_set)
        list_values_can_be_filled_missing_place.append(convert_final_set_to_list)
    return list_values_can_be_filled_missing_place


def insert_value_sudoku_puzzle(sudoku_puzzle):
    index_number = 0
    for index, value in enumerate(sudoku_puzzle):
        if value == 0:
            sudoku_puzzle.pop(index)
            sudoku_puzzle.insert(index, list_values_can_be_filled_missing_place[index_number])
            index_number = index_number + 1


dict_index_value_zero_r_c_ss = dict()


def zip_to_create_dict(lis1, list2):
    zip_operator = zip(lis1, list2)
    dict_index_value_zero_r_c = dict(zip_operator)
    for key, value in dict_index_value_zero_r_c.items():
        dict_index_value_zero_r_c_ss[key] = value
    return dict_index_value_zero_r_c_ss


dict_possible_value = dict()


def dict_possible_zero_values(dict_index_value_zero_r_c_ss):
    # dict_possible_values = dict()
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
    return dict_possible_value

def update_missing_value(sudoku_puzzle):
    for index, value in enumerate(sudoku_puzzle):
        if value == 0:
            # sudoku_puzzle = [my_dct.get(key, key) for key in a]
            for key, val in dict_possible_value.items():
                if key == index:
                    if len(val) == 1:
                        sudoku_puzzle.pop(key)
                        value_int = set.pop(val)
                        sudoku_puzzle.insert(index, value_int)


if __name__ == '__main__':
    def solve_sudoku(sudoku_puzzle):
        paste_sudoku_puzzle_in_matrix(sudoku_puzzle)

        find_index_for_value_0_sudoku_puzzle(sudoku_puzzle)

        find_r_c_ss_number_as_index_value_0(list_index_value_0)

        list_values_r_c_ss(list_associate_r_c_ss_number_as_index)

        find_approx_value_tobe_filled_missing_values(combine_list_values_r_c_ss_associate_value0)

        insert_value_sudoku_puzzle(sudoku_puzzle)
        print("\n")
        paste_sudoku_puzzle_in_matrix(sudoku_puzzle)


    solve_sudoku(sudoku_puzzle)

# def row_column_small_square_values(index_of_value_0):
#     row_list = [key for key, list_of_values in row.items() if index_of_value_0 in list_of_values]
#     column_list = [key for key, list_of_values in column.items() if index_of_value_0 in list_of_values]
#     small_square_list = [key for key, list_of_values in small_square.items() if index_of_value_0 in list_of_values]
#     return row_list, column_list, small_square_list

# lst = []
# for value in my_list:
#     list_of_rows = row_column_small_square_values(value)
#     list_of_column = row_column_small_square_values(value)
#     list_of_ss = row_column_small_square_values(value)
#     list_index = list(list_of_rows + list_of_column + list_of_ss)
#     print (list_index)
#     lst.append(list_index)
# print(lst)
# def paste_sudoku_puzzle_in_matrix(sudoku_list):
#     # matrix = []
#     i = 0
#     for values in sudoku_list:
#         i = i + 1
#         print(values, end=" ")
#         if i == 9:
#             print()
#         if i == 18:
#             print()
#         if i == 27:
#             print()
#         if i == 36:
#             print()
#         if i == 45:
#             print()
#         if i == 54:
#             print()
#         if i == 63:
#             print()
#         if i == 72:
#             print()
#     # return