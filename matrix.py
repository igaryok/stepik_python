import numpy as np

class np1():
    ndarray = list()

count = 0
for i in range(3):
    np1.ndarray.append(list())
    for j in range(4):
        if j == count:
            np1.ndarray[i].append(2)
            #print(2, end=" ")
        elif j == count+1:
            np1.ndarray[i].append(1)
            #print(1, end=" ")
        else:
            np1.ndarray[i].append(0)
            #print(0, end=" ")
    count += 1
    #print("")

a = np.array(np1.ndarray)
print(a)