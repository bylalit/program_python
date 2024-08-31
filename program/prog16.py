# f = open("D:\program_py\program_python\program\demo.txt", "a")


#   reading a file mode! 

# data = f.read()
# data = f.readline()
# print(data)
# print(type(data))

# f.close()




# writting  a file mode! 

# f.write("\n Then  we are going to write some text in this. \n")
# f.write("Hello the new one line. 22")
# f.close()





# new file create when no file is hear

# w = open("sample.txt", "a")
# w.write("Hello")
# f.close()




# syntex  of open() function and with () function

# new  file create when no file is hear and  if file is hear then it will delete the file and write new one 




# with open("sample.txt", "r") as f:
#     data = f.read()
#     print(data)
    
# with open("sample.txt", "w") as f:
#     f.write("Hello world")





# deleting the file for delete the file we use os module

# import os
# os.remove("sample.txt")



# with open("practice.txt", "a") as f:
#     f.write("Hi everyone  \n")
#     f.write("We are learing File I/O \n")
#     f.write("using  Java \n")
#     f.write("I like programming in Java.")

    



# with open("practice.txt", "r") as f:
#     data = f.read()
    
# new_data = data.replace("Java", "Python")
# print(new_data)


# with open("practice.txt", "w") as f:
#     f.write(new_data)


    
    

# def check_for_word():
#     word = "learing"
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if word in data:
#             print(f"{word} is found in the file")
#         else:
#             print("Not found!")


# check_for_word()


# def cheak_for_line():
#     word = "learing"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if word in data:
#                 print(line_no)
#                 return
#             line_no += 1
        
#     return -1

# cheak_for_line()


