print("------------------To do App------------------")
print("1. Enter 'list' to show all tasks \n2. Enter 'add' to add task \n3. 'delete' to remove a task \n4. Enter 'quit' to quit todo: ")


item = []

while True:
    input_data = input("Please Enter Your request: ")
    count = 0
    if input_data == 'quit':
        print("Quit Task")
        break
    
    if input_data == 'list':
        print("--------------")
        for i in item:
            count += 1
            print(f"{count}. {i}")
        print("--------------")
    elif input_data == 'add':
        add = input("Enter your task to add: ")
        item.append(add)
        print("Task added")
    