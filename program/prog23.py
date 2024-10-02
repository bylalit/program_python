
start = int(input("How many var add data: "))

dic = {}
while start > 0:
    key = input("Enter the Keys: ").capitalize()

    val = input("Enter the value: ")

    dic[key] = val

    start -= 1
print(dic)
