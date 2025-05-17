#numpy (numerical python) is kind of a module which containts the number of funcitons to work on the data
#Simply numpy is concept to work on Arrays in python
# To know properties of array we have predefined variables can be called using object(size,data type, dimensional, shape)
# To create empty arry use- ndarray()
# Example for array creation and properties display

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.vstack((arr1, arr2))

print(arr)
import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=0)

print(arr)

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)

import numpy as np
print(np.__version__)  # to know the version of numpy installed

my_list = [10,20,45,65,67,24,99]
my_array = np.array(my_list)  # to create an array
print('Array is:\n', my_array)
print('Size of the array is: ', my_array.size)
print('Data Type of the array is:', my_array.dtype)
print('Dimension of the array is:', my_array.ndim)
print('Shape of the array is:', my_array.shape)

#Two dimensional Array/matrix creation

import numpy as np
my_list1 = [[10,20,30],[40,50,60],[70,80,90]]
matrix = np.array(my_list1)
print(matrix)
print('size of the matrix is:', matrix.size)          # total elements in the matrix is 9
print('Data type of the matrix is:', matrix.dtype)    # all the elements are integers
print('dimension of the matrix is:', matrix.ndim)     # this is 2-dimensional matrix, rows and columns
print('shape of the matrix is :',matrix.shape)        # this is 3 *3 matrix ( 3 rows and 3 columns)


# Using for loop print the elements in the array

import numpy as np
list2 = [15,25,35,45,55,65,75,85]
my_array_list= np.array(list2)

print('Elements in the array is:')
for elements in my_array_list:
    print(elements)

# Create matrix and print the elements using for loop

import numpy as np
list3 = [[11,22,33],[44,55,66],[77,88,99]]
arr3 = np.array(list3)

print('All elements at once as is:')
print(arr3)     # This prints with the [] brackets with inside the elements

print('Prints row wise elements:')
for row in arr3:
    print(row)   # prints row wise elements without any [] brackets outside

print('Each and Every single element:')
for elements in arr3:
    for row in elements:
        print(row)     # prints single element one by one

print('print elements as same as matrix:')

for elements in arr3:
    for matrix in elements:
        print(matrix , end=' ')
    print()

# matrix slicing concept- to get the sub matrix data slicing can be used
# syntax- [rows-lower_bound:upper_bound , Columns:lower_bound:upper_bound]

import numpy as np
list4 = [[21,31,41],[51,61,71],[81,91,101]]
matrix = np.array(list4)
print(matrix)
result = matrix[:,:]   # :,: prints all the rows and columns
print(result)

res = matrix[0:3,0:3]  # prints all the 3 rows and 3 columns
print(res)

result = matrix[0:2,0:2]# this prints only 2 rows, and 2 columns till the 2nd element 21 31, 51 61
print(result)

#print only 2 rows and 3 columns
res = matrix[0:2,0:3]
print(res)

#print 3 rows and only 2 columns
print(matrix[0:3,0:2])
#print only first element
print(matrix[0,0])

print(matrix[1:3,1:3])  # excludes 1st row and 1st column
print(matrix[1:3,0:3])  # excluded 1st row
print(matrix[0:2,0:3])  # excludes 3rd row
print(matrix[0:3,0:2])  # excludes 3rd columns
print(matrix[0:3,1:3])  # excludes 1st column


# construct an empty array using ndarray() [ndimensional array- ndarray]
# create a single dimensional array with size of 6 integer data type elements
# syntax- ndarray(shape=(),dtype)

import numpy as np
empty_array = np.ndarray(shape=(5),dtype=int)
print('size is :', empty_array.size)
print('data type is:', empty_array.dtype)
print('shape is:', empty_array.shape)
print('dimension is:', empty_array.ndim)

# create an array , read elements into that array and finally print them

import numpy as np
# create an empty array with size 5 elements
array5 = np.ndarray(shape=(5),dtype=int)
n= array5.size
#read the elements
for i in range(n):
    array5[i] = int(input('enter the number:'))
print('Elements:', array5)

# Create one dimensional array by user input

import numpy as np

n = int(input('Enter the size of the Array:')) # user input to form the size of the array
array=np.ndarray(shape=(n),dtype=int)

print('Enter the %d elements:' %n)
for i in range(n):                             # Read all the enter elements
     array[i]=int(input('Enter the array elements:'))
print(array)

# Creating Two dimensional array

import numpy as np

# Specify the required number of rows and columns to form the matrix
m =int(input('Enter the number of rows:'))
n =int(input('Enter the number of columns:'))

# create an empty array using ndarray()
matrix=np.ndarray(shape=(m,n),dtype=int)

print('size of the matrix:', matrix.size)
print('Shape of the matrix:', matrix.shape)
print('Dimension of the matrix:', matrix.ndim)

print('Enter the %d elements of %d*%d matrix:' %(m*n,m,n))
#Read the rows and columns and store them in the matrix
for i in range(m):
    for j in range(n):
        matrix[i][j]=int(input('Enter the number:'))
# Print the matrix
print('%d*%d matrix is:' %(m,n))
print(matrix)

# create multi-dimensional array and print the matrix

import numpy as np
arr=np.ndarray(shape=(3,3,3),dtype=int)

var = 1
x =arr.shape[0]
y =arr.shape[1]
z= arr.shape[2]

for i in range(x):
    for j in range(y):
        for k in range(z):
            arr[i][j][k]=var
            var=var+1
print('print the array elements:')
print(arr)

# Numpy Reshape - array.reshape()
# this will heps to convert the dimensions from one to double/multi

import numpy as np

list = [10,20,30,40,50,60]
arr = np.array(list)

print(arr)
print('size of the array:', arr.size)
print('dimension of array:', arr.ndim)

result= arr.reshape(3,2)  # 3 rows and 2 columns which results 2-dimensional array
print(result)
print('dimension of the reshaped array is:', result.ndim)

result= arr.reshape(2,3)  # 2 rows and 3 columns which results 2-dimensional array
print(result)
print('dimension of the reshaped array is:', result.ndim)

############################################################
import numpy as np
list1= [10,20,35,45,55,65,85,90]
arr=np.array(list1)

print(list1)
print('dimension of array is :', arr.ndim)

result = arr.reshape(2,2,2)  #  2 rows and 2 columns , with 3 dimensional array
print(result)
print('dimension of array is :', result.ndim)

result = arr.reshape(4,2)  #  4 rows and 2 columns , with 2 dimensional array
print(result)
print('dimension of array is :', result.ndim)

result = arr.reshape(2,4)  #  2 rows and 4 columns , with 2 dimensional array
print(result)
print('dimension of array is :', result.ndim)

result = arr.reshape(8,1)  #  8 rows and 1 column , with 2 dimensional array
print(result)
print('dimension of array is :', result.ndim)

result = arr.reshape(1,8)  #  1 row and 8 columns , with 2 dimensional array
print(result)
print('dimension of array is :', result.ndim)

# Numpy vs list-
#occupies less memory, faster than list, easy to access and use

# Prove that numpy takes less memory when compare to list-

import numpy as np
import time
import sys

list = range(1000)
print(sys.getsizeof(5)*len(list))  # this will gives the total memory 28000 occupied for 1000 elements

Array = np.arange(1000)  #arange is function
print(Array.size * Array.itemsize)  # stores less memory compared to lists 8000

# Prove numpy array is faster than lists-

import numpy as np
import time
import sys

size = 1000000

list1 = range(size)
list2 = range(size)

array1 = np.arange(size)
array2 = np.arange(size)

#sum the two lists

start = time.time()  # to calculate the time
result = [(x,y) for x,y in zip(list1,list2)] # can't directly sum the lists, we should use for loop with variables
print('Time taken to sum of the lists:',(time.time() - start)*1000) # gives the time milli seconds taken to sum of the lists

start = time.time()
res = array1 + array2

print('Time taken to sum of the arrays:', (time.time()-start)*1000)  # gives the time in milli seconds taken to sum of the arrays

# Numpy operations-
# Dimension- np.ndim, size- np.size, shape- np.shape, data type- np.dtype( default is float)
# reshape,slicing,min,max,sum,axis,ravel,linspace,square root, standard deviation, vertical and horizontal stacking
import numpy as np

array = np.array([(1,2,3),(4,5,6)])
print('Array is:\n',array)
print('Dimension of array:', array.ndim)
print('Size of array:', array.size)
print('Shape of array:', array.shape)
print('Data type of array:', array.dtype)
print('Each item size of array:', array.itemsize)   # prints the byte size of each element
print('Reshape the array:\n', array.reshape(3,2)) #this reshapes array as 3 rows and 2 columns
print('Slicing the array:',array[1][1]) # this prints the number 5
print('Slicing the array:',array[1,1]) # this prints the number 5
print('Slicing the array:',array[0][2]) # this prints the number 3
print('Slicing the array:',array[1][0]) # this prints the number 4
print('Slicing the array:',array[0][0]) # this prints first the number 1
print('Slicing the array:',array[1][2]) # this prints last the number 6
print('Slicing the array:',array[0][1]) # this prints the number 2
print('Slicing the array:',array[0:,2]) # this prints the numbers 3 and 6
print('Slicing the array:',array[0:2,2]) # this also prints the number 3 and 6
print('Slicing the array:',array[0:2,1]) # this prints the number 2 and 5
#Line Space of array numpy operation- This is equally prints the in between values with that specified range

import numpy as np
a = np.linspace(1,10,10)  # this prints all the 10 equal values between 1 to 10
print(a)
a= np.linspace(1,100,10)
print(a)
a = np.linspace(2,10,5)  # this prints 5 equal values between 2 to 10.
print(a)

# min,max and sum functions on numpy operations

import numpy as np
a = np.array([1,2,3,4,5])
print('max number of array is:',a.max())
print('min number of array is:',a.min())
print('sum of the array is:', a.sum())

# axis0 and axis1 to sum the rows and sum the columns in the array numpy operations

import numpy as np
a = np.array([(1,2,3),(5,6,7)])
print(a)
print('The sum of the columns:', a.sum(axis=0)) # sums all the columns , 6(1+5) 8(2+6) 10(3+7)
print('The sum of the rows:', a.sum(axis=1)) # sums the rows, 6(1+2+3) and 18(5+6+7)

# square root, standard deviation numpy operations

import numpy as np
a = np.array([2,4,9])
print('Square root of each element is:', np.sqrt(a))
print('Standard deviation is:', np.std(a))

# addition, sub, multiplication and division using numpy operations
# Vertical stacking and Horizontal stacking of arrays using numpy operations

import numpy as np
a= np.array ([(1,2,3),(4,5,6)])
print(a)
b= np.array([(1,2,3),(4,5,6)])
print(b)

print('Addition of two arrays:\n',a+b)
print('Subtraction of two arrays:\n',a-b)
print('Multy of two arrays:\n',a*b)
print('Div of two arrays:\n',a/b)

print('Vertical stacking of 2 arrays:\n',np.vstack((a,b)))
print('Horizontal stacking of 2 arrays:\n',np.hstack((a,b)))

# print the array to single colum- ravel() numpy operation

import numpy as np

a= np.array([(1,2,3),(9,8,10)])
print(a.ravel())


# Numpy special functions-  sine,cosine,tan using matplot lib

import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0,3*np.pi, 0.1)
y= np.sin(x)
plt.plot(x,y)
plt.show()

z= np.cos(x)
plt.plot(x,z)
plt.show()

i=np.tan(x)
plt.plot(x,i)
plt.show()

# exponential and log special functions

import numpy as np
a =np.array([1,2,3])

print('Exponential of each element is :',np.exp(a))
print('Logarithm of each element is :',np.log(a))
print('Logarithm of each element with base 10 is :',np.log10(a))   # log base10

# (startindex:endindex:stepvalue)
import numpy as np
a= np.array([(1,2,3,4,5,6,7),(8,9,10,11,12,13,14)])
print(a)
print(a[0:, 1:6:2])
print(a[0:, 2:5])
print(a[1:, 2:5]) #gets only 10,11,12
print(a[1:, 2:-2]) #gets only 10,11,12. Negative -2 from last index counts


