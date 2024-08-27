name = "Lalit"
age = 20

print("My name is", name, "and i am", age, "years old", sep="|")

print("Hello world", end=" | ")
print("I am", name)

help(print)


def test_fun(a,b):
    """
    a: value 1
    b: value 2
    
    returns: int
    """
    
    return a + b

help(test_fun)

print(test_fun(12,5))

rng = range(10,-10, -2)

print(list(rng))