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
    
show(5)