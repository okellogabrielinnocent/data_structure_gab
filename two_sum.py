# Leet code Two sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Going through the array isn't good idea since it gives n*n = n2
# Use hash map
# map each value to index value
# Check the difference rather than saving the whole arr to has map
# No reusing the same value twice
# target - 1 = given number
# Inital hashmap is empty and map index to value
# Add entire array into hash map and do mapping without reusing
# Target - inital value 
#  -  indexes aren't used
# only values which are existing are added to hash map
# So w e iterate through the algorathim with one pass


class TwoSum:
	def twoSum(self, nums: List[int], target[int]) -> List[int]:
		preMap = {} # value : index
		
		# iterate through every value in array by index(i) and number(n)
		for i, n enuerate(nums):

			diff = target - n
			if diff in prevMap:
				return [prevMap[diff], i] # return solution
			
			prevMap[n] = i # update index
