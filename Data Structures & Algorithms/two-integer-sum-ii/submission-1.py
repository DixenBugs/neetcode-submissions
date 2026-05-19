
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        l = len(numbers)-1
        while s < l:
            if numbers[s]+numbers[l] == target:
                return [s+1,l+1]
            elif numbers[s]+numbers[l] > target:
                l-=1
            else:
                s+=1