# Question -> https://leetcode.com/problems/maximum-subarray/
# Hint:- pattern: prev subarray cant be negative, dynamic programming: compute max sum for each prefix

class Solution:
	def maxSubArray(self, nums: list[int]) -> int:
		maxSub = nums[0]
		curSub = 0

		for i in nums:
			if curSub < 0:
				curSub = 0
			curSub += i
			maxSub = max(maxSub, curSub)
		return maxSub