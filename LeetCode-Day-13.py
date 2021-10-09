# Ouestion -> https://leetcode.com/problems/product-of-array-except-self/

# Hint :- make two passes, first in-order, second in-reverse, to compute products

#[1,2,3,4] -> Our orginal list
#[1,1,2,6] -> left prefix
#[1,4, 12, 24] -> right postfix
#[24, 12, 4, 1] -> reverse right postfix list
# multiply reverse right with left prefix list
#[24*1, 12*1, 4*2, 6*1]
#[24, 12, 8, 6] -> Our Output list->return

##################################################################
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
###################################################################
#################### Other method is:##############################
class Solution:
    def productExceptSelf(nums: list[int]) -> list[int]:
	output = [1]
	for i in range(len(nums)-1, 0, -1):
		output.append(output[-1]*nums[i])
		print(output)
	output = output[::-1]
	print(output)
	left = 1
	for i in range(len(nums)):
		output[i] = output[i]*left
		print(output[i])
		left *= nums[i]
		print(left)
	return output
        
