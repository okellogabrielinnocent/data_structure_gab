# QuickSort is a Divide and Conquer algorithm.
# It picks an element as pivot and partitions the given array around the picked pivot
# Always pick first element as pivot.
# Always pick last element as pivot (implemented below)
# Pick a random element as pivot.
# Pick median as pivot.
# Target of partitions is, 
# - given an array and an element x of array as pivot, 
# - put x at its correct position in sorted array and put all smaller elements (smaller than x) before x,
#-  and put all greater elements (greater than x) after x. 
# All this should be done in linear time.



# Python3 implementation of QuickSort 
 
# This Function handles sorting part of quick sort
# start and end points to first and last element of
# an array respectively

def partition(arr, start,end):
	# Initializing pivot's index to start
	pivot_index = start
	pivot = array[pivot_index]

	# Tranverse from start to end and swap the pointer with element at end

	while start < end:
		# Increment the start pointer till it finds an element greater than  pivot
		# Decrement the end pointer till it finds an element less than pivot
		# If start and end have not crossed each other, swap the numbers on start and end
		
		while start < len(arr) and arr[start] <= pivot:
			start += 1
		while arr[end] > pivot:
			end -= 1
		if(start < end):
			array[start], array[end] = array[end], array[start]

	# Swap pivot element with element on end pointer.
	array[end], array[pivot_index] = array[pivot_index], array[end]
	return end

# The main function that implements QuickSort
def quick_sort(start, end, array):
	if (start < end):
		# p is partitioning index, array[p] is at right place
		p = partition(start, end, array)

		# Sort elements before partition and after partition
		quick_sort(start, p - 1, array)
		quick_sort(p + 1, end, array)

