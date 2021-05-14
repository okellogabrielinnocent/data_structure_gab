# 2 D array or a square array (an array of n rows and n columns)

# Two-dimensional arrays are basically array within arrays. 
# Here, the position of a data item is accessed by using two indices. 
# It is represented as a table of rows and columns of data items.

# array-name = [ [d1, d2, .... dn], [e1, e2, .... en] ]


array_input = [ [10,12,14] ,[0,1,2] ]

print(array_input[0]) # printing elements of row 0
print(array_input[1]) # printing elements of row 1

# Input to a 2-D Array

# Input to a 2-D array is provided in the form of rows and columns.

# Insert size of array eg 2
# insert row 
# insert column
# save it in array_input


# with list comprehesion one step

n = int(input())
arr = []
for i in range(n):
	arr.append([int(j) for j in input().split()])
	print(arr)

# with list comprehesion second step

n = int(input())
a = [[int(j) for j in input().split()] for i in range(n)]


# OR without list comprehension
# the first line of input is the number of rows of the array
n = int(input()) 
a = []
for i in range(n):
	row = input().split()
	for i in range(len(row)):
		row[i] = int(row[i])
	a.append(row)

# Insert to a 2-D array

from array import *

input = [[1,1,1,1], [12,12,12,12]]

input.insert(1, [1,3,5,7,9])
print([y for y in input])

# Procesing 2-D array


#  Suppose you are given a square array (an array of n rows and n columns). 
#  And suppose you have to set elements of the main diagonal equal to 1 (that is, those elements a[i][j] for which i==j), 
#  to set elements above than that diagonal equal to 0, and to set elements below that diagonal equal to 
#  - That is, you need to produce such an array (example for n==4):

n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i < j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 2
        else:
            a[i][j] = 1
for row in a:
    print(' '.join([str(elem) for elem in row]))

