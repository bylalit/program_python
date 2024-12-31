# # import array
# from array import *


# vals = array('i', [5,9,-7,5,2,8])
# # vals.reverse()

# # for i in range(len(vals)):
# #     print(vals[i])


# new_array = array(vals.typecode, (i*i for i in vals))

# new_array.append(89)
# # for e in new_array:
# #     print(e)
    
# a = sorted(new_array)

# print(a)
# a.reverse()
# print(a)

# sum = 0
# for i in a:
#     # print(i)
#     sum += i
    
# print(sum)





# import numpy
from numpy import *
# import numpy

# arr = array([[[2,3,5,7,9,6,20], [3,5,6,7,4,6,8]], [[45,4,5,6,7,3], [2,4,5,6,7,8]]])

# arr = arange(0,15,2)

# print(arr)

# li = [[[1,2,3,4,5,6,7,8], [2,3,5,6,7,8],[23,4,5,6,7,8,9]], [[1,2,4,5,6], [2,3,4,5,6,6]]]

# for i in li:
#     print(i)
#     for j in i:
#         print(j)
#         for k in j:
            # print(k)



# for i in arr:
#     print(i)
#     for j in i:
#         print(j)
#         for k in j:
#             print(k)



# i = 0


# def greet():
#     # global i
#     i += 1
#     print('hello', i)
#     # greet()

# greet()
# print(i)


# def fact(n):
#     if n == 0:
#         return 1
#     return n * (fact(n-1))

# result = fact(5)
# print(result)





f = lambda a,b: (a*a) + b

# print(f(12,56))


# num = [2,3,5,7,0,7,8,1,6]
num = (2,3,4,8,5,6,3,2)

f = list(filter(lambda a: a % 2 == 0, num))

# f = list(map(lambda a: a*a, num))

from functools import reduce

# f = reduce(lambda a,b: a + b, f)

print(f)