# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# sort the array to help with duplicates
# Use pointers use right pointer to shift and reduce space 
# Shifting left shift the sum
# Complexity O(1) or O(n)

# return list of list
# Sort input array
# use each number in array as possible first value
# Interate through index and value
# Don't reuse the value in the same position twice
# Use 2 pointer solution 
# if sum > 0 decrease the pointer
# if sum < 0 increase left to the right
# return result by appending all three numbers
# Update the pointere 

class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		result = []
		nums.sort()
		
		for i,v in enumerate(nums):
            		# check that the value is not in the same position
            		if i > 0 and v == nums[i - 1]:
                		continue
            		l,r = i + 1, len(nums) - 1
            		
			while l < r:
                		threeSum = v + nums[l] + nums[r]
                		if threeSum > 0:
                    			r -= 1
                		elif threeSum < 0:
                    			l += 1
                		else:
                    			result.append([v,nums[l],nums[r]])
                    			l += 1
                    			while nums[l] == nums[l-1] and l < r:
                        			l += 1
        	return result
        


