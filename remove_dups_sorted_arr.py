

# Description:

# If nums is empty, we return 0. Otherwise, Initialize length = 1, which is the length of the sorted array without duplicates. 
# Initialize two pointers i = 0, j = 1. 
# Iterate j over range(1, len(nums)), and if nums[j] != nums[i], we increment i by 1, and swap nums[i] and nums[j]. 
# It is easy to see the loop invariant that nums[:i+1] is always the sorted array nums[:j+1] with duplicates removed. 
# Hence when j reaches len(nums)-1, nums[:i+1] is nums with duplicates removed.


class Solution(object):
	def removeDuplicates(self,nums):
		'''
		:type nums: List[int]
		:rtype: int
		
		if not nums:
			return 0
		length = 1 # sorted array length
		i = 0
		for j in range(1, len(nums)):
			if nums[j] != nums[i]:
				i += 1
			nums[j],nums[i] = nums[i], nums[j]
			length += 1
		return length


