class solve_sudoku:
    max_count_of_value_in_common_ss = 4
    occurrence_of_value_in_list_of_possible_value = 1

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
        self.common_list_c_ss_value = []
        self.list_of_possible_value_for_one_ss = []
        self.dictionary_for_one_ss = dict()
        self.list_for_index_of_three_identical_zeros_in_row = []

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

    def find_associate_r_c_ss_number_as_index_of_value_zero(self):
        for index in self.list_index_value_zero_in_sudoku_puzzle:
            rows_list = [key for key, list_of_values in self.rows.items() if index in list_of_values]
            columns_list = [key for key, list_of_values in self.columns.items() if index in list_of_values]
            small_squares_list = [key for key, list_of_values in self.small_squares.items() if index in list_of_values]
            self.list_of_matching_row_col_ss_number_as_index_of_value_zero.append(
                rows_list + columns_list + small_squares_list)

    def zip_to_create_dict_of_two_list(self):
        zip_operator = zip(self.list_index_value_zero_in_sudoku_puzzle,
                           self.list_of_matching_row_col_ss_number_as_index_of_value_zero)
        dict_of_index_value_zero_and_matching_r_c_ss = dict(zip_operator)
        for key, value in dict_of_index_value_zero_and_matching_r_c_ss.items():
            self.dict_of_index_value_zero_and_matching_row_col_ss_number[key] = value

    def possible_match_numeric_values_for_zero_values(self):
        for key, value in self.dict_of_index_value_zero_and_matching_row_col_ss_number.items():
            row_ind = self.rows.get(value[0])
            column_ind = self.columns.get(value[1])
            ss_ind = self.small_squares.get(value[2])
            row_lst = [self.sudoku_puzzle[x] for x in row_ind if self.sudoku_puzzle[x] != 0]
            column_lst = [self.sudoku_puzzle[x] for x in column_ind if self.sudoku_puzzle[x] != 0]
            ss_lst = [self.sudoku_puzzle[x] for x in ss_ind if self.sudoku_puzzle[x] != 0]
            row_set = set(row_lst)
            column_set = set(column_lst)
            ss_set = set(ss_lst)
            final_set = (row_set | column_set | ss_set)
            value_set = self.universal_set - final_set
            self.possible_values_can_be_filled_for_zero_values[key] = value_set
        return self.possible_values_can_be_filled_for_zero_values

    def list_common_ss_value_as_per_index(self):
        for index in self.list_index_value_zero_in_sudoku_puzzle:
            list_of_c_ss_keys = [keys for keys, values in self.c_small_squares.items() if index in values]
            common_list_c_ss_index = ((self.c_small_squares.get(list_of_c_ss_keys[0])) + (
                self.c_small_squares.get(list_of_c_ss_keys[1])))
            self.common_list_c_ss_value = [self.sudoku_puzzle[value] for value in common_list_c_ss_index if
                                           self.sudoku_puzzle[value] != 0]

    def compare_common_ss_as_per_index_value(self):
        for key, value in self.possible_values_can_be_filled_for_zero_values.items():
            possible_value_for_index = self.possible_values_can_be_filled_for_zero_values.get(key)
            for values in possible_value_for_index:
                repetition_count_of_value = self.common_list_c_ss_value.count(values)
                if repetition_count_of_value == self.max_count_of_value_in_common_ss:
                    self.sudoku_puzzle.pop(key)
                    self.sudoku_puzzle.insert(key, values)

    def list_of_possible_value_for_one_small_square(self):
        for index in self.list_index_value_zero_in_sudoku_puzzle:
            for keys, values in self.small_squares.items():
                if index in values:
                    self.dictionary_for_one_ss = {key: value for key, value in
                                                  self.possible_values_can_be_filled_for_zero_values.items()
                                                  if key in values}
                    possible_value_for_index = list(self.dictionary_for_one_ss.values())
                    self.list_of_possible_value_for_one_ss = [z for nested_list in possible_value_for_index for z in
                                                              nested_list]
        return self.list_of_possible_value_for_one_ss

    def find_value_by_comparing_possible_value_in_one_ss(self):
        for values in self.list_of_possible_value_for_one_ss:
            repetition_count_of_value = self.list_of_possible_value_for_one_ss.count(values)
            if repetition_count_of_value == self.occurrence_of_value_in_list_of_possible_value:
                for key, value in self.dictionary_for_one_ss.items():
                    if values in value:
                        self.sudoku_puzzle.pop(key)
                        self.sudoku_puzzle.insert(key, values)

    def list_of_identical_three_index_in_row_with_value_zero(self):
        for index in self.list_index_value_zero_in_sudoku_puzzle:
            self.list_for_index_of_three_identical_zeros_in_row = []
            if index <= 78:
                index2 = index + 1
                if self.sudoku_puzzle[index2] == 0:
                    index3 = index2 + 1
                    if self.sudoku_puzzle[index3] == 0:
                        self.list_for_index_of_three_identical_zeros_in_row.append(index)
                        self.list_for_index_of_three_identical_zeros_in_row.append(index2)
                        self.list_for_index_of_three_identical_zeros_in_row.append(index3)
            # return self.list_for_index_of_three_identical_zeros_in_row
            else:
                break

    def find_value_by_comparing_possible_value_of_three_index_in_row_with_value_zero(self):
        dictionary_for_three_identical_zeros_in_row = {key: value for key, value in
                                                       self.possible_values_can_be_filled_for_zero_values.items()
                                                       if
                                                       key in self.list_for_index_of_three_identical_zeros_in_row}
        possible_value_for_index_of_three_identical_zeros_in_row = list(
            dictionary_for_three_identical_zeros_in_row.values())
        list_possible_value_for_index_of_three_identical_zeros_in_row = [value for nested_list_value in
                                                                         possible_value_for_index_of_three_identical_zeros_in_row
                                                                         for value in nested_list_value]
        for value in list_possible_value_for_index_of_three_identical_zeros_in_row:
            repetition_count_of_value = list_possible_value_for_index_of_three_identical_zeros_in_row.count(value)
            if repetition_count_of_value == self.occurrence_of_value_in_list_of_possible_value:
                for keys, values in dictionary_for_three_identical_zeros_in_row.items():
                    if value in values:
                        self.sudoku_puzzle.pop(keys)
                        self.sudoku_puzzle.insert(keys, value)

    def update_missing_value(self):
        for index in self.list_index_value_zero_in_sudoku_puzzle:
            for key, val in self.possible_values_can_be_filled_for_zero_values.items():
                if key == index:
                    if len(val) == self.occurrence_of_value_in_list_of_possible_value:
                        self.sudoku_puzzle.pop(key)
                        value_int = set.pop(val)
                        self.sudoku_puzzle.insert(index, value_int)


sudoku = [0, 8, 0, 0, 1, 3, 0, 6, 0,
          0, 0, 5, 0, 9, 2, 7, 8, 4,
          0, 0, 0, 0, 0, 0, 0, 9, 0,
          8, 2, 0, 0, 0, 0, 0, 3, 0,
          0, 1, 0, 3, 0, 6, 0, 0, 0,
          0, 5, 0, 0, 0, 0, 0, 1, 2,
          0, 4, 0, 0, 0, 0, 0, 0, 0,
          0, 6, 8, 4, 7, 0, 1, 0, 0,
          0, 9, 0, 8, 6, 0, 0, 5, 0]

new_puzzle = solve_sudoku(sudoku)
new_puzzle.paste_sudoku_puzzle_in_form_of_matrix()
new_puzzle.find_index_for_value_zero_in_sudoku_puzzle()

for value in range(12):
    new_puzzle.find_associate_r_c_ss_number_as_index_of_value_zero()
    new_puzzle.zip_to_create_dict_of_two_list()
    print(new_puzzle.possible_match_numeric_values_for_zero_values())
    new_puzzle.update_missing_value()
    new_puzzle.list_common_ss_value_as_per_index()
    new_puzzle.compare_common_ss_as_per_index_value()
    print(new_puzzle.list_of_possible_value_for_one_small_square())
    print(new_puzzle.list_of_identical_three_index_in_row_with_value_zero())
    # new_puzzle.find_value_by_comparing_possible_value_in_one_ss()
    # new_puzzle.find_value_by_comparing_possible_value_of_three_index_in_row_with_value_zero()

print("\n")
new_puzzle.paste_sudoku_puzzle_in_form_of_matrix()
