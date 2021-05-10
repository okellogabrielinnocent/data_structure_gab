# Python program for implementation of Insertion Sort
/*
 * Precondition:  len(arr) is the number of items that are
 *    stored in arr.  These items must be in increasing order
 *    (arr[0] <= arr[1] <= ... <= arr[len(arr-1]).
 *    The array size is at least one greater than len(arr).
 * Postcondition:  The number of items has increased by one,
 *    newItem has been added to the array, and all the items
 *    in the array are still in increasing order.
 * Note:  To complete the process of inserting an item in the
 *    array, the variable that counts the number of items
 *    in the array must be incremented, after calling this
 *    subroutine.
 */

# Algorithm
# To sort an array of size n in ascending order: 
# 1: Iterate from arr[1] to arr[n] over the array. 
# 2: Compare the current element (key) to its predecessor. 
# 3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

 
# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1,len(arr):
		key =arr[i]
		# Move elements of arr[0..i-1], that are
        	# greater than key, to one position ahead
        	# of their current position

		#Start at the end of the array
		loc = i-1

		while loc>=0 and key < arr[j]:
			arr[loc + 1] = arr[loc]
			j -= 1
		arr[loc + 1] = key

# Developer code to test above
arr = [12, 11, 13, 5, 6,10]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
 

