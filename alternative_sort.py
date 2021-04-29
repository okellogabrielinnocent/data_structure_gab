# Given an array of integers, 
# - print the array in such a way that the first element is first maximum and second element is first minimum and so on.
# Input : arr[] = {7, 1, 2, 3, 4, 5, 6}
# Output : 7 1 6 2 5 3 4

#	Solution
# - Sort input array using a O(n Log n) algorithm. 
# - Maintain two pointers, one from beginning and one from end in sorted array. 
# - Alternatively print elements pointed by two pointers and move them toward each other.

def alternateSort(arr, n):
	# sort arr
	arr.sort()
	i = 0
	j = n-1
	# check if last is not beyond the first
	while(i < j):
		print(arr[j])
		j -= 1
		print(arr[i])
		i += 1
	if (n % 2 != 0):
		print(arr[i])

# Developer test code
arr = [7, 1, 2, 3, 4, 5, 6]
n = len(arr)

alternateSort(arr, n)

