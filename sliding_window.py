# 121. Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Solution
# We need to find out the maximum difference (which will be the maximum profit) between two numbers in the given array. Also, the second number (selling price) must be larger than the first one (buying price).

# In formal terms, we need to find \max(\text{prices[j]} - \text{prices[i]})max(prices[j] prices[i]), for every i and j such that j > i.

# Possible approaches are brute force and one pass
# Use two pointers updating left and right
# Only 

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		l,r = 0,1 # left-=buy, right = sell
		maxProf = 0
		
		if len(prices) < 2:
			return 0

		while r < len(prices):
			#profitable
			if prices[l] < prices[r]:
				profit = prices[r] - prices[l]
				maxProf = max(maxProf, profit)
			else:
				l = r
			r += 1
		return maxProf






