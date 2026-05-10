class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            if (target - nums[x]) in nums[x+1:]: 
                return [x, nums[x+1:].index(target - nums[x])+1+x]