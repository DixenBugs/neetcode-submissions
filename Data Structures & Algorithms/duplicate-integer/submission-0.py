class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_numbers = []
        for number in nums:
            if number in duplicate_numbers: 
                return True
            else:
                duplicate_numbers.append(number)
        return False