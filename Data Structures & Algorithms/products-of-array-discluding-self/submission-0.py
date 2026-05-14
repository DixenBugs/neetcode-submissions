class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixSum = [1]
        for i in range(len(nums)-1):
            prefixSum.append(prefixSum[-1] * nums[i])
        post = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            prefixSum[i] *= post
            post *= nums[i]
        return prefixSum
