# Merge an array of size n into another array of size m+n

# There are two sorted arrays. First one is of size m+n containing only m elements
# Another one is of size n and contains n elements.
# Merge these two arrays into the first array of size m+n such that the output is sorted.
# Algorithm: 
# Let first array be mPlusN[] and other array be N[]
# -> Move m elements of mPlusN[] to end.
# -> Start from nth element of mPlusN[] and 0th element of N[] and merge them into mPlusN[].


# Python program to Merge an array of
# size n into another array of size m + n

NA = -1

# Lets move the elements to end of mPlusN

def moveToEnd(mPlusN, size):
	i = 0
	j = size - 1
	for  in range(size - 1, -1, -1):
		if mPlusN !=NA):
			#swap the two values
			mPlusN[j] = mPlusN[i]
			j -= 1

	# Merges array N[]
	# of size n into array mPlusN[]
	# of size m+n


def merge(mPlusN, N, m, n):
	i = n  # Current index of i/p part of mPlusN[]
	j = 0  # Current index of N[]
	k = 0  # Current index of output mPlusN[]

	while (k < (m+n)):
		# take element of mPlusN if 
		# -> value of picked element is smaller than the reached end of it
		# -> we have reached the end of N
		
		if ((j==n) or (i < (m + n) and mPlusN[i] <= N[j])):
			
			mPlusN[k] = mPlusN[i]
			k += 1
			i += 1
		else: # Otherwise take element from N[]
			mPlusN[k] = N[j]
			k += 1
			j += 1

			


