# Question = https://leetcode.com/problems/container-with-most-water/

#-----Time Complexity-----> O(n)
#-----Space Complexity----> O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        beg  = 0
        end = len(height) - 1
        max_Area = 0
        
        while beg < end:
            max_Area = max(max_Area, min(height[beg], height[end])*(end-beg))
            if height[beg] >= height[end]:
                end -= 1
            else:
                beg += 1
        return max_Area