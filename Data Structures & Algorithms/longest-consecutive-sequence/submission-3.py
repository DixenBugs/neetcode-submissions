class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums.sort()
        max = 1
        count = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif abs(nums[i + 1] - nums[i]) == 1:
                count += 1
            else:
                max = max if max >= count else count
                count = 1
            max = max if max >= count else count
        return max