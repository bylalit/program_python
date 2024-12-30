# def hel():
    # print("hello")
    
# hel()

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
    
# print(fac(5))  # Output: 120


def evenodd(a):
    if a % 2 == 0:
        print("even")
    else:
        print("odd")
        
# evenodd(8)

# def show(n):
#     if n == 0:
#         return
#     print(n)
#     show(n-1)
    
# show(5)













menu = {
    'tave': 20,
    'paneer': 30,
    'pizaa': 40,
    'burger': 80
}

menu['dosha'] = 90

print(menu)

# if "dosha" not in menu:
#     print("Byy")
# else:
#     print('Hello')
#     menu['mendu'] = 20
# print(menu)


# for i,a in menu.items():
    # print(i,a)
    
# for i in menu:
#     print(menu[i])

# print(menu.keys())
# print(menu.values())
# print(menu.items())
# print(menu.get('tave'))
# print(menu['pizaa'])

