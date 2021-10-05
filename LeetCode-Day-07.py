class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """ Method #1"""
        # out = []
        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if j != i and nums[j] < nums[i]:
        #             count += 1        
        #     out.append(count)
        # return out
        # # Order of Complexity = O(n^2)
        
        """Faster runtime: Method #2"""
        sorted_nums = sorted(nums, reverse=True)
        smaller_count = {}
        for i in range(len(sorted_nums) -1):
            cur_nums = sorted_nums[i]
            next_nums = sorted_nums[i+1]
            if next_nums < cur_nums:
                remaining_values = len(sorted_nums)-(i+1)
                smaller_count[cur_nums] = remaining_values
        # for last index values
        smaller_count[sorted_nums[-1]] = 0
        output = []
        for num in nums:
            output.append(smaller_count[num])
        return output
        
        # Order of Complexity = O(n.logn)
            
        
        
        