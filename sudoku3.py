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

un_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

x = [1, 2, 0, 4, 5, 0, 7, 8, 9, 0, 5, 6, 7, 8, 0, 1, 2, 3, 7, 0, 9, 1, 2, 3, 4, 0, 6, 3, 1, 2, 6, 0, 5, 9, 7, 8, 6, 4,
     0, 9, 7, 8, 3, 0, 2, 9, 7, 8, 3, 1, 0, 6, 4, 5, 0, 3, 1, 5, 6, 4, 8, 0, 7, 8, 9, 7, 2, 0, 1, 5, 6, 0, 5, 6, 4, 8,
     0, 7, 2, 0, 1]


def index (sudoku_lst):
    my_lists = [index for index,value in enumerate(sudoku_lst) if value == 0]
    return my_lists


def update_values (var):
    details = []
    # details = [val for val in var if x[val]]
    for val in var:
        if x[val]:
            details.append(x[val])
    return details


def row_val (valu):
    row_lt = [key for key, list_of_values in row.items() if valu in list_of_values]
    return row_lt


def column_val (valu):
    column_lt = [key for key, list_of_values in column.items() if valu in list_of_values]
    return column_lt


def ss_val (valu):
    ss_lt = [key for key, list_of_values in small_square.items() if valu in list_of_values]
    return ss_lt

my_list = index (x)

lst = []
for value in my_list:
    list_of_rows = row_val(value)
    list_of_column = column_val(value)
    list_of_ss = ss_val(value)
    list_index = list_of_rows + list_of_column + list_of_ss
    lst.append(list_index)
print(lst)

for values in lst:
    row_value = row.get(values[0])
    column_value = column.get(values[1])
    ss_value = small_square.get(values[2])
    row_lst = update_values(row_value)
    column_lst = update_values(column_value)
    ss_lst = update_values(ss_value)
    my_lst = row_lst + column_lst + ss_lst
    my_set = set(my_lst)
    final_set = un_set - my_set
    print(final_set)
