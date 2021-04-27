# Given an array of n elements, where each element is at most k away from its target position, 
# Devise an algorithm that sorts in O(n log k) time. 
# For example, let us consider k is 2, 
# An element at index 7 in the sorted array, 
# Can be at indexes 5, 6, 7, 8, 9 in the given array.

# Input : arr[] = {6, 5, 3, 2, 8, 10, 9} , k = 3 
# arr[] = {2, 3, 5, 6, 8, 9, 10}

# this uses insertion sort
# where K in the target element

def insertionSort(arr, n):

	i = j = k = 0

	for i in range(n):
		k = arr[i]
		j = i-1
		

		while j >= 0 and arr[j] > k:
			arr[j + 1] = arr[j]
			j = j - 1

		arr[j + 1] = k

# Developers Test Code

arr = [12, 11, 13, 5, 6,10]
k=5
insertionSort(arr,k)
for i in range(len(arr)):
	print ("% d" % arr[i])



# NOTE: We can sort such arrays more efficiently with the help of Heap data structure as insertion sort isn't efficient
#	This will be done after we have leveraged heap sort

