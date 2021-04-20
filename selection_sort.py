			# Selection Sort

# The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.
# The algorithm maintains two subarrays in a given array.

# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.

arr[] = 64 25 12 22 11

# // Find the minimum element in arr[0...4]
# // and place it at beginning

11 25 12 22 64

# Find the minimum element in arr[1...4]
# and place it at beginning of arr[1...4]

11 12 25 22 64

# Find the minimum element in arr[2...4]
# and place it at beginning of arr[2...4]

11 12 22 25 64


# Python program for implementation of Selection
# Sort

import sys


arr = [64, 25, 12, 22, 11]

# Traverse through all array elements in sequencial order

for i in len(arr):
	# Find the minimum element in remaining unsorted array
	
	min_idx = i
	for j in range(i+1,len(arr)):
		# if array at position arr[j] < arr[i] then position j becomes min_index
		if arr[min_idx] > arr[j]:
			min_idx = j
	# Swap the found minimum element with the first element
	arr[i],arr[min_idx] = arr[min_idx],arr[i]


# Developer code to test above

print ("Sorted array")
for i in range(len(A)):
	print("%d" %A[i])

# NOTE: 
# - This sorting algorithm is an in-place comparison-based algorithm in which the list is divided into two parts, 
# - the sorted part at the left end and the unsorted part at the right end. 
# - Initially, the sorted part is empty and the unsorted part is the entire list.
