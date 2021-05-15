#  program to reverse an array or string

# method 1
# 1) Initialize start and end indexes as start = 0, end = n-1 
# 2) In a loop, swap arr[start] with arr[end] and change start and end as follows : 
# start = start + 1, end = end - 1


def reverse_list(arr, start, end):
	while start < end:
		arr[start], arr[end] = arr[end], arr[start]
		start += 1
		end -= 1


# method 2

# 1) Initialize start and end indexes as start = 0, end = n-1 
# 2) Swap arr[start] with arr[end] 
# 3) Recursively call reverse for rest of the array.

def reverseList(arr, start, end):
	if start >= end:
		return
	arr[start], arr[end] = arr[end], arr[start]
	reverseList(arr, start+1, end-1)


# Method 3 

# Using Python List slicing


def reverse_list_slice(arr):
	return( A[::-1])


arr = [1,2,3,4,5,6,7,8,9]

reverse_list(arr, 0,9)
reverseList(arr, 0, 5)
reverse_list_slice()


