from module import paste_sudoku_puzzle_in_matrix, sudoku_puzzle, universal_set, small_square, column, row

list_index_value_0 = []
def find_index_for_value_0_sudoku_puzzle(sudoku_puzzle):
    for index, value in enumerate(sudoku_puzzle):
        if value == 0:
            list_index_value_0.append(index)
    return list_index_value_0


list_associate_r_c_ss_number_as_index = []
def find_r_c_ss_number_as_index_value_0(list_index_value_0):
    # list_of_associate_r_c_ss = []
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
