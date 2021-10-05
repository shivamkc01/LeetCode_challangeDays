class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Method -1"""
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1
        
        """Method -2"""
        # nums = [-1, 3, 4, 6, 8, 9,12, 15, 18],    target = 10
        # start = 0
        # end = 8
        # middle = (start + end)/2 = 4
        
        # start = 4
        # end = 8
        # mid = 6
        
        # start = 4
        # end = 6
        # mid = 5
        
        # start = 5
        # end = 6
        low = 0
        high = len(nums) - 1        
        while low <= high:
            mid = (high + low) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
        # Time complexity is O(log N).
        
        
    
        