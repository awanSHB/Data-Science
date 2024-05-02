import numpy as np

##11) Positions of two matching elements

ar1 = np.array([1, 2, 3, 4, 5, 6, 7])
ar2 = np.array([1, 4, 3, 6, 5, 8, 7])
res = np.where(ar1==ar2)
print(res)
print("--------------------------------\n\n")

##12) Extract numbers

a1 = np.arange(11)
res = a1[(a1>=5) & (a1<=8)]
print(res)
print("--------------------------------\n\n")

##13) Scalars function on numpy arrays

def maxx(ar1, ar2):
    return np.maximum(ar1, ar2)

ar1 = np.array([1, 2, 3])
ar2 = np.array([2, 1, 0])
print(maxx(ar1, ar2))
print("--------------------------------\n\n")

##14) Swap columns 

a = np.array([[1, 2], [3, 4], [5, 6]])
for k in range(a.size//2):
    t = a[k][0]
    a[k][0] = a[k][1]
    a[k][1] = t
print(a)
print()
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

a[:, [0, 1]] = a[:, [1, 0]]
print(a)
print()
a = np.arange(9).reshape(3, 3)
a = a[:, [1, 0, 2]]
print(a)
print("--------------------------------\n\n")

##15) Swap Two rows

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

a = a[[1, 2, 0], :]
print(a)
print()
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

a[[0, 1], :] = a[[1, 0], :]
print(a)
print("--------------------------------\n\n")

##16) Reverse Row

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

a = a[::-1, :]                      #Reversing rows arrangement
print(a)
print()

a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

a[0, :] = a[0, ::-1]                #Reversing only first row
print(a)
print()
print("--------------------------------\n\n")

##17) Reversing coloumns
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])

a = a[:, ::-1]                      #Reversing all elements in all rows
print(a)
print("--------------------------------\n\n")

##18)Random Values in 2d array b/w 5 and 20

a = np.random.uniform(5, 10, size=(5, 3))
a = a.astype(int)                   #Converting them to int
print(a)

a = np.arange(9)
b = np.arange(11)
r = np.concatenate(((a), (b)))
print(r)