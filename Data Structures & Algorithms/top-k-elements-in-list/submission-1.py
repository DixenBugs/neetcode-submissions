class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        bucket_sort = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num]  = 1 + count.get(num, 0)
        
        for key, value in count.items():
            bucket_sort[value].append(key)
            
        ans = []

        for i in range(len(bucket_sort) - 1, 0, -1 ):
            for j in bucket_sort[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans