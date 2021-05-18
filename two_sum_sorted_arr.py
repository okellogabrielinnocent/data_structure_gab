#	Two Sum II - Input array is sorted

# Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
# You may assume that each input would have exactly one solution and you may not use the same element twice.

# Method 1 Hash Map

class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		prevDict = {}
		for i,n in enumerate(numbers):
			diff = target - n
			if diff in prevDic:
				return [prevDic[diff], i+1]
			prevDic[n] = i+1


# Method 2 Pointers
class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		l,r = 0, len(numbers) - 1
		
		while l < r:
			curSam = numbers[l] + numbers[r]
		if curSam > target:
			r -= 1 # decrease right

		elif curSam < target:
			l += 1	# increase left

		else:
			return [l + 1, r + 1]

