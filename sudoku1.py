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

a =x[:9]
b=x[9:18]
c=x[18:27]
d=x[27:36]
e=x[36:45]
f=x[45:54]
g=x[54:63]
h=x[63:72]
i=x[72:81]
print (a)
print (b)
print (c)
print (d)
print (e)
print (f)
print (g)
print (h)
print (i)

my_list = []
for i, z in enumerate(x):
    if z == 0:
        my_list.append(i)
print(my_list)

lst = []
for value in my_list:
    list_of_rows = []
    for key , list_of_values in row.items():
        if value in list_of_values:
            list_of_rows.append(key)
    list_of_column = []
    for key , list_of_values in column.items():
        if value in list_of_values:
            list_of_column.append(key)
    list_of_ss = []
    for key , list_of_values in small_square.items():
        if value in list_of_values:
            list_of_ss.append(key)
    list_index = list_of_rows + list_of_column + list_of_ss
    lst.append(list_index)
print(lst)

for values in lst:
    row_value = row.get(values[0])
    column_value = column.get(values[1])
    ss_value = small_square.get(values[2])
    row_lst = []
    for index in row_value:
        if x[index]:
            row_lst.append(x[index])
    column_lst = []
    for index in column_value:
        if x[index]:
            column_lst.append(x[index])
    ss_lst = []
    for index in ss_value:
        if x[index]:
            ss_lst.append(x[index])
    row_set = set(row_lst)
    column_set = set(column_lst)
    ss_set = set(ss_lst)
    final_set = un_set - (row_set or column_set or ss_set)
    print(final_set)

'''

# print (list_of_column)
    # print (list_of_rows)
    # list_of_rows = [key for key, list_of_values in row.items() if value in list_of_values]
    # list_of_column = [key for key, list_of_values in column.items() if value in list_of_values]
    # list_of_ss = [key for key, list_of_values in small_square.items() if value in list_of_values]
    # print (list_of_ss)
    # print(row_lst)
    # print(column_lst)
    # print (ss_lst)
    # print(row_set)
    # print(column_set)
    # print (ss_set)
    
# def get_values(indexes):
#     values = list()
#     for u in indexes:
#         if x[u]:
#             values.append(x[u])
#     return values
# def get_value (z):
#     j_lst = []
#     for t in z:
#         if x[t]:
#             j_lst.append(x[t])
#     return j_lst

# for index, p in enumerate(x):
#     print (index , p)

# my_list = [i for i , z in enumerate(x) if z == 0]
# print (my_list)


# cell_value = {}

    # print (list)
    # cell_value [value] = list
# print(cell_value , type(cell_value))

# def get (ind):
#     for x in ind:

r_lst = []
# c_lst = []
# ss_lst = []
for y in lst:
    r_ind = row.get(y[0])
    # row_values = get_values(r_ind)
    # print (row_values)
    # print (r_ind , type(r_ind))
    # r_list = list(r_ind)
#     print (r_list)
    for u in r_ind:
        if x[u]:
            r_lst.append(x[u])

    r_set = set(r_lst)
    print (r_set)






#     c_ind = column.get(x[1])
#     print (c_ind , type(c_ind))
#     c_lst.append(c_ind)
#     ss_ind = small_square.get(x[2])
#     print (ss_ind , type(ss_ind))
#     ss_lst.append(ss_ind)

# print (c_lst)
# print (ss_lst)
#
# z0 = [x for x in r_lst[0] if x in c_lst[0] and x in ss_lst[0]]
# z1 = [x for x in r_lst[1] if x in c_lst[1] and x in ss_lst[1]]
# z2 = [x for x in r_lst[2] if x in c_lst[2] and x in ss_lst[2]]
# z3 = [x for x in r_lst[3] if x in c_lst[3] and x in ss_lst[3]]
# z4 = [x for x in r_lst[4] if x in c_lst[4] and x in ss_lst[4]]
# z5 = [x for x in r_lst[5] if x in c_lst[5] and x in ss_lst[5]]
# z6 = [x for x in r_lst[6] if x in c_lst[6] and x in ss_lst[6]]
# z7 = [x for x in r_lst[7] if x in c_lst[7] and x in ss_lst[7]]
# z8 = [x for x in r_lst[8] if x in c_lst[8] and x in ss_lst[8]]
# print (z0 , z1 , z2 , z3 , z4 , z5 , z6 , z7 , z8)


# r_sets = r_set()
# for x in r_lst:
#     x.r_set()
# print (r_sets)
# r_set = set(r_lst)
# print (r_set , type(r_set))


for key , values in cell_value.items():
    row_indexes = row.get(values[0])
    # row_final = row_indexes
    print (row_indexes , type (row_indexes))
    column_indexes = column.get(values[1])
    print (column_indexes)
    ss_indexes = small_square.get(values[2])
    print (ss_indexes)
    final_set = un_set - (set(row_indexes) | set(column_indexes) | set(ss_indexes))
    print (final_set)

print ()
# print (row_final)




# print (cell_value[2][0][0])



# for key , values in row.keys():
#     if valuess in cell_value.values():
#         print ("true")
#     else:
#         print ("false")








# list_of_ro = []
# for value in my_list:
#     for key , values  in row.items():
#         if value in values:
#             list_of_ro = row.keys()
#             print (list_of_ro)
'''
