# 3Sum Closest

# Given an array nums of n integers and an integer target, 
# find three integers in nums such that the sum is closest to target. 
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 

# Constraints:

# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4

# Solution

# No cobination of three no's sums to the number but sum to closet to number
# Sort the array
# Loop through the sorted array
# Use pointers at eaither end
# Add the three together and comapare with target value
# shift upper pointer to the left
# Sum is compared to number instead of zero


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # return list of list
        # Sort input array
        # use each number in array as possible first value
        # Interate through index and value
        # Don't reuse the value in the same position twice
        # Use 2 pointer solution
        # if sum > target decrease the pointer
        # if sum < target increase left to the right
        # Update the pointer
        best_three_sum_closet = 10000
        nums.sort()
        
        for i,v in enumerate(nums):
            # check that the value is not in the same position
            if i > 0 and v == nums[i - 1]:
                continue
            l,r = i + 1, len(nums) - 1
            while l < r:
                # check sum = number
                three_sum_closet = v + nums[l] + nums[r]
                
                if three_sum_closet == target:
                    return three_sum_closet
                
                if abs(target - three_sum_closet) < abs(target - best_three_sum_closet):
                    best_three_sum_closet = three_sum_closet
                    
                if three_sum_closet > target:
                    r -= 1
                    
                if three_sum_closet < target:
                    l += 1
                    
        return best_three_sum_closet
        
