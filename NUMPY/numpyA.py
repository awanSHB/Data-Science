import numpy as np

#1) Create a NumPy array with values ranging from 0 to 9.

vals = []

for k in range(10):
    vals.append(k**2)

arr = np.array(vals)
print(arr)

array1 = np.array([0, 1 , 2, 3, 4, 5, 6, 7, 8, 9])
print(array1)

array2 = np.arange(0, 10)
print(array2)
print()

#2) Create a NumPy array of zeros with shape (2, 3).


array3 = np.zeros([2, 3])
print(array3)
print()

#3) Create a NumPy array of ones with shape (4, 2).


array4 = np.ones([4, 2])
print(array4)
print()

#4) Create a NumPy array with 5 evenly spaced values between 0 and 1.


array5 = np.linspace(0, 1, 5)
print(array5)
print()

#5) Create a NumPy array with 5 evenly spaced values between 1 and 10.


array6 = np.linspace(1, 10, 5)
print(array6)
print()

#6) Create a NumPy array of 10 random integers between 0 and 100.


array7 = np.random.randint(0, 100, 10)
print(array7)
print()

#7) Create a NumPy array of 5 random floats between 0 and 1.


array8 = np.random.uniform(0, 1, 5)
print(array8)
print()

#8) Create a 3x3 NumPy array with values ranging from 0 to 8 and print its transpose.


array9 = np.arange(0, 9).reshape(3, 3)
print(array9)
array10 = np.transpose(array9)
print(array10)
print()


#9) Create a NumPy array with shape (3, 2) and reshape it to (2, 3).


array11 = np.array([[1, 2, 3], [4, 5, 6]])
array12 = array11.reshape((3, 2))
print(array11)
print(array12)
print()


#10) Create a NumPy array with shape (2, 2) and perform element-wise multiplication 
#####with another NumPy array of the same shape.

array13 = np.arange(1, 5).reshape(2, 2)
array14 = np.arange(5, 9).reshape(2, 2)
res = np.multiply(array13, array14)
print(array13)
print(array14)
print(res)
print("\n\n")

#### 3D array using a for loop

a = 3
b = 5
c = 7

array15 = np.zeros((a, b, c))
for i in range(a):
    for j in range(b):
        for k in range(c):
            array15[i][j][k] = i+j+k

print(array15)