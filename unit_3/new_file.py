# arr = [12,56,89,42,88,45,78]
# min = arr[0]

# for i in arr:
#     if i > min:
#         min = i
        
# print(min)


# # fibonacci series
# prev1 = 0
# prev2 = 1

# print(prev1, end=" ")
# print(prev2, end=" ")
# for i in range(20):
#     new = prev1 + prev2
#     print(new, end = " ")
#     prev1 = prev2
#     prev2 = new
    
    
    
    
# print(0)
# print(1)
# count = 2

# def fibonacci(prev1, prev2):
#     global count
#     if count <= 19:
#         newFibo = prev1 + prev2
#         print(newFibo, end = " ")
#         prev2 = prev1
#         prev1 = newFibo
#         count += 1
#         fibonacci(prev1, prev2)
#     else:
#         return

# fibonacci(1,0)



# print(0,1, end=" ")
count = 2
sum = 0

def fibo(prev1, prev2):
    global count
    global sum
    if count < 20:
        new = prev1 + prev2
        sum += new
        # print(new, end = " ")
        prev1 = prev2
        prev2 = new
        count += 1
        fibo(prev1, prev2)
    else:
        return
    # print(sum)
    
# fibo(0,1)
# print(sum)




# my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# n = len(my_array)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if my_array[j] > my_array[j+1]:
#             my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

# print("Sorted array:", my_array)



# arr = [15,89,34,2,56,45,78,56]

# n = len(arr)
# for i in range(n-1):
#     swapped = False
#     for j in range(n-i-1):
#         if arr[j] < arr[j+1]:
#             # arr[j], arr[j+1] = arr[j+1], arr[j]
#             temp = arr[j]
#             arr[j] = arr[j+1]
#             arr[j+1] = temp
#             swapped = True

#     if not swapped:
#         break

# print("Sorted array:", arr)    




# selection sort


# def sort(arr):
#     for i in range(len(arr)):
#         min = i
#         for j in range(i+1, len(arr)):
#             if arr[j] < arr[min]:
#                 min = j
#         arr[i], arr[min] = arr[min], arr[i]
#     return arr

# arr = [15,89,34,2,56,45,78,56]

# print(sort(arr))










# class Parent:
#     def __init__(self):
#         self.data = []

#     def show_data(self):
#         print("Parent data:", self.data)


# class Child(Parent):
#     def add_data(self, value):
#         self.data.append(value)

#     def clear_data(self):
#         self.data.clear()

# child_instance = Child()

# child_instance.add_data(10)
# child_instance.add_data(20)

# child_instance.show_data() 
# # [10, 20]

# child_instance.clear_data()

# child_instance.show_data()


class parent1:
    def __init__(self):
        self.data = []
    
    def show_data(self):
        print('The Data is: ', self.data)        

class child1(parent1):
    print('hello')
    def add_data(self, val):
        self.data.append(val)
        
    def remove_data(self):
        self.data.pop()


obj = child1()

obj.add_data(5)
obj.add_data(10)
obj.add_data(15)
obj.show_data()
obj.remove_data()
obj.show_data()
