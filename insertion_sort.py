# Python program for implementation of Insertion Sort

# Algorithm
# To sort an array of size n in ascending order: 
# 1: Iterate from arr[1] to arr[n] over the array. 
# 2: Compare the current element (key) to its predecessor. 
# 3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

 
# Function to do insertion sort
def insertionSort(arr):

	# Traverse through 1 to len(arr)
	for i in range(1,len(arr):
		key =arr[1]
		# Move elements of arr[0..i-1], that are
        	# greater than key, to one position ahead
        	# of their current position
		
		j=i-1
		while j>=0 and key < arr[j]:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key

# Developer code to test above
arr = [12, 11, 13, 5, 6,10]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
 

