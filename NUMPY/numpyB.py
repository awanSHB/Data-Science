import numpy as np

##1) 1D array

a1 = np.arange(10)
a2 = np.array([1, 2 , 3, 4, 5, 6])
a3 = np.zeros(10)
print(a1)
print(a2)
print(a3)
print("--------------------------------\n\n")


##2) Boolean array

a1 = np.full((3, 3), True, dtype=bool)
print(a1)
print()

a2 = np.zeros((3, 3), dtype=bool)
print(a2)
print()

a3 = np.array([1, 2, 3, 4, 5, 6])
bool_array = a3 > 3
print(bool_array)

print("--------------------------------\n\n")


##3) Extract items

a1 = np.arange(11)
a2 = []
for k in a1:
    if k%2 == 0:
        a2.append(k)
print(a2)

print(a1[a1%2==0])
print("--------------------------------\n\n")


##4) Replace items

a1 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
a1[a1%2==0] = -1
print(a1)

for m in range(a1.size):
    if a1[m]%2==0:
        a1[m] = -1
print(a1)
print("--------------------------------\n\n")


##5) Reshape Array

ar = np.arange(10).reshape(2, -1)
print(ar)
print("--------------------------------\n\n")

##6) Stack two arrays vertically

ar1 = np.array([1, 2, 3, 4])		
ar2 = np.array([5, 6, 7, 8])
res = np.stack((ar1, ar2), axis=1)
print(res)

ar1 = np.array([[1, 2, 3], [4, 5, 6]])
ar2 = np.array([[7, 8, 9], [10, 11, 12]])
res = np.vstack((ar1, ar2))
print(res)
print("--------------------------------\n\n")

##7) Stack two arrays horizontally

ar1 = np.array([1, 2, 3, 4])
ar2 = np.array([4, 5, 6, 7])
res = np.stack((ar1, ar2), axis=0)
print(res)

ar1 = np.array([[1, 2, 3], [4, 5, 6]])
ar2 = np.array([[7, 8, 9], [10, 11, 12]])
res = np.hstack((ar1, ar2))
print(res)

print("--------------------------------\n\n")

##8) Custom sequences
# Input: a = np.array([1,2,3])
# Output: array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])

ar1 = np.array([1, 2, 3])
ar2 = np.hstack((np.repeat(ar1, 3), np.tile(ar1, 3)))
print(ar2)

print("--------------------------------\n\n")

##9) Common Elements
ar1 = np.arange(1, 11)
ar2 = np.linspace(1, 9, 5)
res = np.intersect1d(ar1, ar2)
print(res)

print("--------------------------------\n\n")

##10) Remove Items

ar1 = np.arange(1, 6)
ar2 = np.arange(5, 11)
res = np.setdiff1d(ar1, ar2)
print(res)