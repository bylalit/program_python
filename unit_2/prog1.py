
# 22 program
# def fun(d):
#     for key in d:
#         print("Key: ", key, " " ,"Value: ", d[key])
        
# D = {'a':1, 'b':2, 'c':3, 'd': 4}

# fun(D)




# 21 program
# keys = ['Cricket', 'BasketBall', 'Hockey']
# valus = ['11', '5', '11']

# combine_dic = dict(zip(keys, valus))
# print(combine_dic)



# 20 program
# my_dict = {'name': 'Jack', 'age': 26}
# print(my_dict['name'])
# print()
# print(my_dict.get('age'))
# print()
# print(my_dict.get('address'))




# 19 program





# 18 program
# tup = (1,2,3,4,5,6,7,8)

# print("Max: ", max(tup))
# print("Max: ", min(tup))
# print("Max: ", sum(tup))
# print("Max: ", sum(tup)/len(tup))






# 17 program
# list1 = [[1,2,3], [4,5,6,7], [8,9,0]]
# 1 method
# for i in list1:
#     print(i)
#     for j in i:
#         print(j)

2 method
for x in list1:
    print(" ".join(map(str, x)))





# 14 program
# list1 = [i for i in range(0,9)]
# print(list1)
# list1.append(12)
# print(list1)

# list1.insert(1, 15)
# print(list1)

# list1.reverse()
# print(list1)

# list1.remove(7)
# print(list1)





# 15 program
# list1 = [i for i in range(1,6)]
# list2 = [i for i in range(7,11)]
# print(list1)
# print(list2)
# print()
# list3 = list1 + list2
# print(list3)

# new_list = [i for i in list3 for x in (0,1)]
# print(new_list)

# list_cloneing = list3[:]
# print(list_cloneing)








# 16 program
list1 = [i for i in range(1,8)]
print(list1)
print()

list1.append(12)
print(list1)
print()

list1.insert(1,10)
print(list1)
print()

list2 = list1.copy()
print(list2)
print()


c = list1.count(5)
print(c)