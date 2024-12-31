# import array
from array import *


vals = array('i', [5,9,-7,5,2,8])
# vals.reverse()

# for i in range(len(vals)):
#     print(vals[i])


new_array = array(vals.typecode, (i*i for i in vals))

new_array.append(89)
# for e in new_array:
#     print(e)
    
a = sorted(new_array)

print(a)
a.reverse()
print(a)

sum = 0
for i in a:
    # print(i)
    sum += i
    
print(sum)