def star(x):
    print (f"{x} stars are there")
    def cube():
        print (x*x*x)
    return cube ()

f = star (5)
print (f)




# def cube(x):
#     return x*x*x
#
#
# def map(func , d_list):
#     result = []
#     for i in d_list:
#         result.append(func(i))
#     return result
#
# f = map(cube , [1,2,3,4])
# print (f)