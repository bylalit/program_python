print("------------------To do App------------------")
print("1. Enter 'list' to show all tasks \n2. Enter 'add' to add task \n3. 'delete' to remove a task \n4. Enter 'quit' to quit todo: ")


item = []

while True:
    input_data = input("Please Enter Your request: ")
    if input_data == 'quit':
        print("Quit Task")
        break
    
    if input_data == 'list':
        print("--------------")
        for i in item:
            print(f"{i} {item[i]}")
        # print(item)
        print("--------------")
    elif input_data == 'add':
        add = input("Enter your task to add: ")
        item.append(add)
        print("Task added")