# Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# It introduces the following ideas: Loop Invariant, Linear Search, Sorting and Hash Table.

# we could check the lenght of set of the arr

# len(arr) != len(set(arr)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d =dict()
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                return True
        return False



