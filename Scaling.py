import numpy as np
dimensions = np.array([[0,4,0],[0,4,4],[4,4,0],[4,4,4],[4,0,0],[0,0,4],[4,0,4],[0,0,0]])
s = [‘A’,’B’,’C’,’D’,’E’,’F’,’G’,’H’]
Sx = 2
Sy = 4
Sz = 6
a = []
a.append(Sx)
a.append(Sy)
a.append(Sz)
for i in range(len(dimensions)):
    for j in range(len(dimensions[0])):
        dimensions[i][j] = dimensions[i][j]*a[j]
for i in range(len(dimensions)):
    print(s[i],end=” coordinates are : ( “)
    for j in range(len(dimensions[0])):
        print(dimensions[i][j],end=” “)
    print(‘)’,end=””)
    print(‘\t’)
