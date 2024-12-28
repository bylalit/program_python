arr = [12,56,89,42,88,45,78]
min = arr[0]

for i in arr:
    if i > min:
        min = i
        
print(min)


# fibonacci series
prev1 = 0
prev2 = 1

print(prev1, end=" ")
print(prev2, end=" ")
for i in range(20):
    new = prev1 + prev2
    print(new, end = " ")
    prev1 = prev2
    prev2 = new