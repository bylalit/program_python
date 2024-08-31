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




with open("sample.txt", "r") as f:
    data = f.read()
    print(data)
    
with open("sample.txt", "w") as f:
    f.write("Hello world")