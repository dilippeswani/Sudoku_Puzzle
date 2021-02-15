class SudokuPuzzle:
    def __init__(self, puzzle, level="Easy"):
        self.puzzle = puzzle
        self.level = level
        self.zero_values = {}
        self.possible_valid_values = {}

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
                              "ss3": (6, 7, 8, 15, 16, 17, 24, 25, 26), "ss4": (27, 28, 29, 36, 37, 38, 35, 46, 47),
                              "ss5": (30, 31, 32, 39, 40, 41, 48, 49, 50), "ss6": (33, 34, 35, 42, 43, 44, 51, 52, 53),
                              "ss7": (54, 55, 56, 63, 64, 65, 72, 73, 74), "ss8": (57, 58, 59, 66, 67, 68, 75, 76, 77),
                              "ss9": (60, 61, 62, 69, 70, 71, 78, 79, 80)}
        self.universal_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def __str__(self):
        return f"Puzzle of {self.level} difficulty level"

    def print_puzzle(self):
        for index, values in enumerate(self.puzzle, start=1):
            if index % 9 == 0:
                print(values, end="\n")
            else:
                print(values, end=" ")

    def find_index_of_zero_values(self):
        for index, cell_value in enumerate(self.puzzle):
            if not cell_value:
                row = self.get_key_from_dict(self.rows, index)
                col = self.get_key_from_dict(self.columns, index)
                ss = self.get_key_from_dict(self.small_squares, index)
                self.zero_values[index] = (row + col + ss)

    def get_key_from_dict(self, dict_, index):
        result = [key for key, values in dict_.items() if index in values]
        return result

    def find_possible_valid_values_from_row_column_and_ss(self):
        for index, values in self.zero_values.items():
            values_list_for_index = self.collect_row_col_and_ss_values_for_this_index(values)
            values_set = set(values_list_for_index)
            possible_values = self.universal_set - values_set
            self.possible_valid_values[index] = possible_values

    def collect_row_col_and_ss_values_for_this_index(self, values):
        row_indexes = self.rows.get(values[0])
        col_indexes = self.columns.get(values[1])
        ss_indexes = self.small_squares.get(values[2])
        values = []
        for index in row_indexes:
            values.append(self.puzzle[index])

        for index in col_indexes:
            values.append(self.puzzle[index])

        for index in ss_indexes:
            values.append(self.puzzle[index])
        return values

    def update_puzzle(self):
        for index, value in self.possible_valid_values.items():
            if len(value) == 1:
                self.puzzle[index] = value.pop()


if __name__ == '__main__':
    sudoku_puzzle1 = [1, 0, 0, 4, 0, 0, 7, 0, 0,
                      0, 5, 6, 7, 8, 0, 1, 2, 3,
                      7, 0, 9, 1, 2, 3, 4, 0, 6,
                      3, 1, 2, 6, 0, 5, 9, 7, 8,
                      6, 4, 0, 9, 7, 8, 3, 0, 2,
                      9, 7, 8, 3, 1, 0, 6, 4, 5,
                      0, 3, 1, 5, 6, 4, 8, 0, 7,
                      8, 9, 7, 2, 0, 1, 5, 6, 0,
                      5, 6, 4, 8, 0, 7, 2, 3, 1]

    sudoku_puzzle2 = [1, 0, 0, 4, 0, 0, 7, 0, 0,
                      0, 5, 6, 7, 8, 0, 1, 2, 3,
                      7, 0, 9, 1, 2, 3, 4, 0, 6,
                      3, 1, 2, 6, 0, 5, 9, 7, 8,
                      6, 4, 0, 9, 7, 8, 3, 0, 2,
                      9, 7, 8, 0, 1, 0, 6, 4, 5,
                      0, 3, 1, 5, 0, 4, 8, 0, 7,
                      8, 9, 0, 2, 0, 1, 5, 6, 0,
                      5, 6, 0, 8, 0, 7, 0, 3, 1]


    puzzle1 = SudokuPuzzle(sudoku_puzzle1)
    puzzle1.print_puzzle()
    puzzle1.find_index_of_zero_values()
    # print(puzzle1.zero_values)
    puzzle1.find_possible_valid_values_from_row_column_and_ss()
    print(puzzle1.possible_valid_values)
    puzzle1.update_puzzle()
    puzzle1.print_puzzle()
    puzzle1.find_possible_valid_values_from_row_column_and_ss()
    print(puzzle1.possible_valid_values)
    puzzle1.update_puzzle()
    puzzle1.print_puzzle()
    puzzle1.find_possible_valid_values_from_row_column_and_ss()
    print(puzzle1.possible_valid_values)
    puzzle1.update_puzzle()
    puzzle1.print_puzzle()

    print("Puzzle- 2")
    puzzle2 = SudokuPuzzle(sudoku_puzzle2)
    puzzle2.find_index_of_zero_values()
    puzzle2.print_puzzle()
    puzzle2.find_possible_valid_values_from_row_column_and_ss()
    print(puzzle2.possible_valid_values)
    puzzle2.update_puzzle()
    puzzle2.find_possible_valid_values_from_row_column_and_ss()
    print(puzzle2.possible_valid_values)
    puzzle2.update_puzzle()
    puzzle2.find_possible_valid_values_from_row_column_and_ss()
    print(puzzle2.possible_valid_values)
    puzzle2.update_puzzle()
    puzzle2.print_puzzle()
