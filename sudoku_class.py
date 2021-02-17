class solve_sudoku:

    def __init__(self, puzzle):

        self.sudoku_puzzle = puzzle

        self.rows = {"r1": (0, 1, 2, 3, 4, 5, 6, 7, 8), "r2": (9, 10, 11, 12, 13, 14, 15, 16, 17),
                     "r3": (18, 19, 20, 21, 22, 23, 24, 25, 26), "r4": (27, 28, 29, 30, 31, 32, 33, 34, 35),
                     "r5": (36, 37, 38, 39, 40, 41, 42, 43, 44), "r6": (45, 46, 47, 48, 49, 50, 51, 52, 53),
                     "r7": (54, 55, 56, 57, 58, 59, 60, 61, 62), "r8": (63, 64, 65, 66, 67, 68, 69, 70, 71),
                     "r9": (72, 73, 74, 75, 76, 77, 78, 79, 80)}

        self.columns = {"c1": (0, 9, 18, 27, 36, 45, 54, 63, 72), "c2": (1, 10, 19, 28, 37, 46, 55, 64, 73),
                        "c3": (2, 11, 20, 29, 38, 47, 56, 65, 74), "c4": (3, 12, 21, 30, 39, 48, 57, 66, 75),
                        "c5": (4, 13, 22, 31, 40, 49, 58, 67, 76), "c6": (5, 14, 23, 32, 41, 50, 59, 68, 77),
                        "c7": (6, 15, 24, 33, 42, 51, 60, 69, 78), "c8": (7, 16, 25, 34, 43, 52, 61, 70, 79),
                        "c9": (8, 17, 26, 35, 44, 53, 62, 71, 80)}

        self.small_squares = {"ss1": (0, 1, 2, 9, 10, 11, 18, 19, 20), "ss2": (3, 4, 5, 12, 13, 14, 21, 22, 23),
                              "ss3": (6, 7, 8, 15, 16, 17, 24, 25, 26), "ss4": (27, 28, 29, 36, 37, 38, 45, 46, 47),
                              "ss5": (30, 31, 32, 39, 40, 41, 48, 49, 50), "ss6": (33, 34, 35, 42, 43, 44, 51, 52, 53),
                              "ss7": (54, 55, 56, 63, 64, 65, 72, 73, 74), "ss8": (57, 58, 59, 66, 67, 68, 75, 76, 77),
                              "ss9": (60, 61, 62, 69, 70, 71, 78, 79, 80)}

        self.c_small_squares = {
            "A": (0, 1, 2, 9, 10, 11, 18, 19, 20, 3, 4, 5, 12, 13, 14, 21, 22, 23, 6, 7, 8, 15, 16, 17, 24, 25, 26),
            "B": (
                27, 28, 29, 36, 37, 38, 45, 46, 47, 30, 31, 32, 39, 40, 41, 48, 49, 50, 33, 34, 35, 42, 43, 44, 51, 52,
                53),
            "C": (
                54, 55, 56, 63, 64, 65, 72, 73, 74, 57, 58, 59, 66, 67, 68, 75, 76, 77, 60, 61, 62, 69, 70, 71, 78, 79,
                80),
            "D": (
                0, 1, 2, 9, 10, 11, 18, 19, 20, 27, 28, 29, 36, 37, 38, 45, 46, 47, 54, 55, 56, 63, 64, 65, 72, 73, 74),
            "E": (
                3, 4, 5, 12, 13, 14, 21, 22, 23, 30, 31, 32, 39, 40, 41, 48, 49, 50, 57, 58, 59, 66, 67, 68, 75, 76,
                77),
            "F": (
                6, 7, 8, 15, 16, 17, 24, 25, 26, 33, 34, 35, 42, 43, 44, 51, 52, 53, 60, 61, 62, 69, 70, 71, 78, 79,
                80)}

        self.universal_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        self.list_index_value_zero_in_sudoku_puzzle = []
        self.list_of_matching_row_col_ss_number_as_index_of_value_zero = []
        self.dict_of_index_value_zero_and_matching_row_col_ss_number = dict()
        self.possible_values_can_be_filled_for_zero_values = dict()

    def paste_sudoku_puzzle_in_form_of_matrix(self):
        for index, values in enumerate(self.sudoku_puzzle, start=1):
            if index % 9 == 0:
                print(values, end="\n")
            else:
                print(values, end=" ")
        print(self.sudoku_puzzle.count(0))

    def find_index_for_value_zero_in_sudoku_puzzle(self):
        for index, value in enumerate(self.sudoku_puzzle):
            if value == 0:
                self.list_index_value_zero_in_sudoku_puzzle.append(index)
        return self.list_index_value_zero_in_sudoku_puzzle

    def find_associate_r_c_ss_number_as_index_of_value_zero(self):
        for index in self.list_index_value_zero_in_sudoku_puzzle:
            rows_list = [key for key, list_of_values in self.rows.items() if index in list_of_values]
            columns_list = [key for key, list_of_values in self.columns.items() if index in list_of_values]
            small_squares_list = [key for key, list_of_values in self.small_squares.items() if index in list_of_values]
            self.list_of_matching_row_col_ss_number_as_index_of_value_zero.append(
                rows_list + columns_list + small_squares_list)
        return self.list_of_matching_row_col_ss_number_as_index_of_value_zero

    def zip_to_create_dict_of_two_list(self):
        zip_operator = zip(self.list_index_value_zero_in_sudoku_puzzle,
                           self.list_of_matching_row_col_ss_number_as_index_of_value_zero)
        dict_of_index_value_zero_and_matching_r_c_ss = dict(zip_operator)
        for key, value in dict_of_index_value_zero_and_matching_r_c_ss.items():
            self.dict_of_index_value_zero_and_matching_row_col_ss_number[key] = value
        return self.dict_of_index_value_zero_and_matching_row_col_ss_number

    def possible_match_numeric_values_for_zero_values(self):
        for key, value in self.dict_of_index_value_zero_and_matching_row_col_ss_number.items():
            row_ind = self.rows.get(value[0])
            column_ind = self.columns.get(value[1])
            ss_ind = self.small_squares.get(value[2])
            row_lst = []
            for x in row_ind:
                if self.sudoku_puzzle[x] != 0:
                    row_lst.append(self.sudoku_puzzle[x])
            column_lst = []
            for x in column_ind:
                if self.sudoku_puzzle[x] != 0:
                    column_lst.append(self.sudoku_puzzle[x])
            ss_lst = []
            for x in ss_ind:
                if self.sudoku_puzzle[x] != 0:
                    ss_lst.append(self.sudoku_puzzle[x])
            row_set = set(row_lst)
            column_set = set(column_lst)
            ss_set = set(ss_lst)
            final_set = (row_set | column_set | ss_set)
            value_set = self.universal_set - final_set
            self.possible_values_can_be_filled_for_zero_values[key] = value_set
        return self.possible_values_can_be_filled_for_zero_values

    def compare_ss(self):
        for index, value in enumerate(self.sudoku_puzzle):
            if value == 0:
                list_of_c_ss_keys = []
                for keys, values in self.c_small_squares.items():
                    if index in values:
                        list_of_c_ss_keys.append(keys)
                common_list_c_ss_index = (
                        (self.c_small_squares.get(list_of_c_ss_keys[0])) + (
                    self.c_small_squares.get(list_of_c_ss_keys[1])))
                common_list_c_ss_value = []
                for val in common_list_c_ss_index:
                    if self.sudoku_puzzle[val] != 0:
                        common_list_c_ss_value.append(self.sudoku_puzzle[val])
                        for key_s, value_s in self.possible_values_can_be_filled_for_zero_values.items():
                            if key_s == index:
                                possible_value_for_index = self.possible_values_can_be_filled_for_zero_values.get(key_s)
                                for valu in possible_value_for_index:
                                    repetition_count_of_value = common_list_c_ss_value.count(valu)
                                    if repetition_count_of_value == 4:
                                        self.sudoku_puzzle.pop(index)
                                        self.sudoku_puzzle.insert(index, valu)

    def update_ss(self):
        for index, value in enumerate(self.sudoku_puzzle):
            if value == 0:
                for keys, values in self.small_squares.items():
                    if index in values:
                        my_dict = dict()
                        for y in values:
                            for key_s, value_s in self.possible_values_can_be_filled_for_zero_values.items():
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
                                for keyy, valuee in my_dict.items():
                                    if valu in valuee:
                                        self.sudoku_puzzle.pop(keyy)
                                        self.sudoku_puzzle.insert(keyy, valu)

    def find_identical_three_index_in_row_with_value_zero(self):
        # for index in range(0,80):
        for index, value in enumerate(self.sudoku_puzzle):
            values = []
            if value == 0 or value != 0:
                if index <= 78:
                    index2 = index + 1
                    if self.sudoku_puzzle[index2] == 0:
                        index3 = index2 + 1
                        if self.sudoku_puzzle[index3] == 0:
                            values.append(index)
                            values.append(index2)
                            values.append(index3)
                            print(values)
                            my_dict = dict()
                            for y in values:
                                for key_s, value_s in self.possible_values_can_be_filled_for_zero_values.items():
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
                                    for keyy, valuee in my_dict.items():
                                        if valu in valuee:
                                            self.sudoku_puzzle.pop(keyy)
                                            self.sudoku_puzzle.insert(keyy, valu)
                else:
                    break

    def update_missing_value(self):
        for index, value in enumerate(self.sudoku_puzzle):
            if value == 0:
                for key, val in self.possible_values_can_be_filled_for_zero_values.items():
                    if key == index:
                        if len(val) == 1:
                            self.sudoku_puzzle.pop(key)
                            value_int = set.pop(val)
                            self.sudoku_puzzle.insert(index, value_int)
                            # del self.possible_values_can_be_filled_for_zero_values[key]


sudoku = [0, 8, 0, 0, 1, 3, 0, 6, 0,
          0, 0, 5, 0, 9, 2, 7, 8, 4,
          0, 0, 0, 0, 0, 0, 0, 9, 0,
          8, 2, 0, 0, 0, 0, 0, 3, 0,
          0, 1, 0, 3, 0, 6, 0, 0, 0,
          0, 5, 0, 0, 0, 0, 0, 1, 2,
          0, 4, 0, 0, 0, 0, 0, 0, 0,
          0, 6, 8, 4, 7, 0, 1, 0, 0,
          0, 9, 0, 8, 6, 0, 0, 5, 0]

# sudoku = [0, 0, 0, 3, 0, 0, 0, 0, 4,
#           0, 6, 4, 2, 0, 0, 0, 0, 0,
#           3, 0, 8, 5, 0, 0, 2, 6, 0,
#           2, 0, 0, 0, 0, 0, 1, 0, 0,
#           0, 0, 0, 4, 6, 7, 0, 0, 0,
#           0, 0, 7, 0, 0, 0, 0, 0, 5,
#           0, 9, 2, 0, 0, 8, 7, 0, 3,
#           0, 0, 0, 0, 0, 5, 8, 2, 0,
#           5, 0, 0, 0, 0, 9, 0, 0, 0]

new_puzzle = solve_sudoku(sudoku)
new_puzzle.paste_sudoku_puzzle_in_form_of_matrix()
new_puzzle.find_index_for_value_zero_in_sudoku_puzzle()

for value in range(10):
    new_puzzle.find_associate_r_c_ss_number_as_index_of_value_zero()
    new_puzzle.zip_to_create_dict_of_two_list()
    print(new_puzzle.possible_match_numeric_values_for_zero_values())
    new_puzzle.compare_ss()
    new_puzzle.update_ss()
    new_puzzle.update_missing_value()



# new_puzzle.find_identical_three_index_in_row_with_value_zero()
#
# for value in range(10):
#     new_puzzle.find_associate_r_c_ss_number_as_index_of_value_zero()
#     new_puzzle.zip_to_create_dict_of_two_list()
#     print(new_puzzle.possible_match_numeric_values_for_zero_values())
#     new_puzzle.compare_ss()
#     new_puzzle.update_ss()
#     new_puzzle.update_missing_value()

print("\n")
new_puzzle.paste_sudoku_puzzle_in_form_of_matrix()
