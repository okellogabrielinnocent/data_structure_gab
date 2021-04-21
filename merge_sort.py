# Merge sort is a sorting technique based on divide and conquer technique. 
# With worst-case time complexity being O(n log n), it is one of the most respected algorithms.
# Merge sort first divides the array into equal halves and then combines them in a sorted manner.

# Step 1 - if it is only one element in the list it is already sorted, return.
# 	Find the middle point to divide the array into two halves:  
#            middle m = l+ (r-l)/2

# Step 2 - divide the list recursively into two halves until it can no more be divided.
#	Call mergeSort for first half:   
#            Call mergeSort(arr, l, m)
# Step 3 - merge the smaller lists into new list in sorted order.
#	Call mergeSort for second half:
#            Call mergeSort(arr, m+1, r)

# Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)



def merg_sort(arr):
	
	# Finding the mid of the array
	mid = len(arr)//2

	# Dividing the array elements into two halves L and R
	L = arr[:mid]
	R = arr[mid:]
	
	# Sorting the halves by calling merge_sort on each array
	merge_sort(R)
	merge_sort(L)

	i = j = k = 0

	# Copy data to temp arrays L[] and R[]
	while i < len(L) and j < len(R):
		if L[i] < R[j]:
			arr[k] = L[i]
			i +=1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
		
	# Checking if any element was left
	while i < len(L):
		arr(K) = L(i)
		i += 1
		k += 1
	while j < len(R):
		arr(K) = R(j)
		j += 1
		k += 1


def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()
 
 
# Developers Code

if __name__ == '__main__':
	arr = [12, 11, 13, 5, 6, 7]
	print("Given array is", end="\n")
	printList(arr)
	mergeSort(arr)
	print("Sorted array is: ", end="\n")
	printList(arr)

# Application
# - Merge Sort is useful for sorting linked lists in O(nLogn) time.
# - Count Inversions in an array ( how far (or close) the array is from being sorted.)
# - Used in External Sorting
