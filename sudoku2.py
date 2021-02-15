rows = {"r1": (0, 1, 2, 3, 4, 5, 6, 7, 8), "r2": (9, 10, 11, 12, 13, 14, 15, 16, 17),
        "r3": (18, 19, 20, 21, 22, 23, 24, 25, 26), "r4": (27, 28, 29, 30, 31, 32, 33, 34, 35),
        "r5": (36, 37, 38, 39, 40, 41, 42, 43, 44), "r6": (45, 46, 47, 48, 49, 50, 51, 52, 53),
        "r7": (54, 55, 56, 57, 58, 59, 60, 61, 62), "r8": (63, 64, 65, 66, 67, 68, 69, 70, 71),
        "r9": (72, 73, 74, 75, 76, 77, 78, 79, 80)}

columns = {"c1": (0, 9, 18, 27, 36, 45, 54, 63, 72), "c2": (1, 10, 19, 28, 37, 46, 55, 64, 73),
           "c3": (2, 11, 20, 29, 38, 47, 56, 65, 74), "c4": (3, 12, 21, 30, 39, 48, 57, 66, 75),
           "c5": (4, 13, 22, 31, 40, 49, 58, 67, 76), "c6": (5, 14, 23, 32, 41, 50, 59, 68, 77),
           "c7": (6, 15, 24, 33, 42, 51, 60, 69, 78), "c8": (7, 16, 25, 34, 43, 52, 61, 70, 79),
           "c9": (8, 17, 26, 35, 44, 53, 62, 71, 80)}

small_squares = {"ss1": (0, 1, 2, 9, 10, 11, 18, 19, 20), "ss2": (3, 4, 5, 12, 13, 14, 21, 22, 23),
                 "ss3": (6, 7, 8, 15, 16, 17, 24, 25, 26), "ss4": (27, 28, 29, 36, 37, 38, 35, 46, 47),
                 "ss5": (30, 31, 32, 39, 40, 41, 48, 49, 50), "ss6": (33, 34, 35, 42, 43, 44, 51, 52, 53),
                 "ss7": (54, 55, 56, 63, 64, 65, 72, 73, 74), "ss8": (57, 58, 59, 66, 67, 68, 75, 76, 77),
                 "ss9": (60, 61, 62, 69, 70, 71, 78, 79, 80)}

x = [1, 2, 0, 4, 5, 0, 7, 8, 9, 0, 5, 6, 7, 8, 0, 1, 2, 3, 7, 0, 9, 1, 2, 3, 4, 0, 6, 3, 1, 2, 6, 0, 5, 9, 7, 8, 6, 4,
     0, 9, 7, 8, 3, 0, 2, 9, 7, 8, 3, 1, 0, 6, 4, 5, 0, 3, 1, 5, 6, 4, 8, 0, 7, 8, 9, 7, 2, 0, 1, 5, 6, 0, 5, 6, 4, 8,
     0, 7, 2, 0, 1]

universal_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}


def get_values(indexes):
    values = list()
    for index in indexes:
        if x[index]:
            values.append(x[index])
    return values
# row_values = get_values(row_indexes)


my_list = [i for i, z in enumerate(x) if z == 0]
print(my_list)

cell_info = {}
for value in my_list:
    row = [key for key, list_of_values in rows.items() if value in list_of_values]
    column = [key for key, list_of_values in columns.items() if value in list_of_values]
    ss = [key for key, list_of_values in small_squares.items() if value in list_of_values]
    info = row + column + ss
    cell_info[value] = info

print(cell_info)

for key, values in cell_info.items():
    row_indexes = rows.get(values[0])
    row_values = get_values(row_indexes)

    col_indexes = columns.get(values[1])
    col_values = get_values(col_indexes)

    ss_indexes = small_squares.get(values[2])
    ss_values = get_values(ss_indexes)

    # print(row_values)
    # print(col_values)
    # print(ss_values)
    my_set = universal_set - (set(row_values) | set(col_values) | set(ss_values))
    print(key, "-", my_set)
